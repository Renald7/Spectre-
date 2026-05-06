# =============================================================================
# QUANTUM DL DOCKERFILES - BILLIONS OF USERS SCALE
# Multi-stage builds for minimal image size and maximum security
# =============================================================================

# -----------------------------------------------------------------------------
# BASE IMAGE - Common dependencies
# -----------------------------------------------------------------------------
FROM python:3.13-slim AS base

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1 \
    PYTHONFAULTHANDLER=1 \
    PIP_NO_CACHE_DIR=1 \
    PIP_DISABLE_PIP_VERSION_CHECK=1

# Install system dependencies
RUN apt-get update && apt-get install -y --no-install-recommends \
    # Networking
    curl \
    # Utilities
    dumb-init \
    # Security
    gpg \
    # Monitoring
    telnet \
    # Build tools
    && rm -rf /var/lib/apt/lists/* \
    && useradd -m -u 1000 -r -s /bin/false appuser

WORKDIR /app

# Copy dependency files
COPY pyproject.toml pyproject.toml
COPY uv.lock uv.lock

# -----------------------------------------------------------------------------
# BUILDER IMAGE - Install Python dependencies
# -----------------------------------------------------------------------------
FROM base AS builder

RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential \
    pkg-config \
    libffi-dev \
    libssl-dev \
    && rm -rf /var/lib/apt/lists/*

# Install uv
RUN curl -LsSf https://astral.sh/uv/install.sh | sh
ENV PATH="/root/.local/bin:$PATH"

# Sync dependencies
RUN uv sync --no-dev

# -----------------------------------------------------------------------------
# API IMAGE - FastAPI application
# -----------------------------------------------------------------------------
FROM base AS api

# Copy builder dependencies
COPY --from=builder /app/.venv /app/.venv

# Copy application
COPY src/ /app/src/
COPY api/ /app/api/

# Set Python path
ENV PATH="/app/.venv/bin:$PATH" \
    PYTHONPATH=/app \
    PYTHONUNBUFFERED=1

# Create log directory
RUN mkdir -p /var/log/quantum-dl

# Switch to non-root user
USER appuser
USER 1000

# Expose ports
EXPOSE 8000 8443

# Health check
HEALTHCHECK --interval=30s --timeout=10s --start-period=30s --retries=3 \
    CMD curl -f http://localhost:8000/health || exit 1

# Entrypoint
ENTRYPOINT ["dumb-init", "--"]
CMD ["python", "-m", "uvicorn", "api.main:app", "--host", "0.0.0.0", "--port", "8000", "--workers", "4"]

# -----------------------------------------------------------------------------
# WORKER IMAGE - Celery worker
# -----------------------------------------------------------------------------
FROM base AS worker

# Copy builder dependencies
COPY --from=builder /app/.venv /app/.venv

# Copy worker code
COPY src/ /app/src/

# Set Python path
ENV PATH="/app/.venv/bin:$PATH" \
    PYTHONPATH=/app \
    WORKER_CONCURRENCY=8 \
    WORKER_PREFETCH_MULTIPLIER=4

# Switch to non-root user
USER appuser
USER 1000

# Entrypoint
ENTRYPOINT ["dumb-init", "--"]
CMD ["celery", "-A", "src.quantum_dl.worker.main", "worker", "--loglevel=info", "--concurrency=8"]

# -----------------------------------------------------------------------------
# MODEL SERVER IMAGE - ML model serving
# -----------------------------------------------------------------------------
FROM nvidia/cuda:12.2-runtime-ubuntu22.04 AS model-server-base

ENV DEBIAN_FRONTEND=noninteractive

RUN apt-get update && apt-get install -y --no-install-recommends \
    python3.11 \
    python3-pip \
    curl \
    && rm -rf /var/lib/apt/lists/*

# -----------------------------------------------------------------------------
# TensorRT builder from base
# -----------------------------------------------------------------------------
FROM model-server-base AS trt-builder

RUN apt-get update && apt-get install -y --no-install-recommends \
    libnvinfer-dev \
    libnvparsers12 \
    libnvonnxparsers12 \
    && rm -rf /var/lib/apt/lists/*

# Install Python packages with TensorRT support
RUN pip3 install --no-cache-dir \
    torch==2.1.0 \
    torch Tensor==2.1.0 \
    tensorrt

# -----------------------------------------------------------------------------
# Model server from builder
# -----------------------------------------------------------------------------
FROM model-server-base AS model-server

# Copy builder dependencies
COPY --from=builder /app/.venv /app/.venv
COPY --from=trt-builder /usr/lib/python3.11/dist-packages /usr/lib/python3.11/dist-packages

# Copy model server code
COPY src/ /app/src/
COPY model_server/ /app/model_server/

# Set Python path
ENV PATH="/app/.venv/bin:$PATH" \
    PYTHONPATH=/app \
    MODEL_CACHE_DIR=/models \
    TENSORRT_ENABLED=1 \
    GPU_MEMORY_FRACTION=0.9

# Expose ports
EXPOSE 9000 8080

# Health check
HEALTHCHECK --interval=30s --timeout=10s --start-period=60s --retries=3 \
    CMD curl -f http://localhost:9000/health || exit 1

# Entrypoint
ENTRYPOINT ["dumb-init", "--"]
CMD ["python", "-m", "model_server.main", "--host", "0.0.0.0", "--port", "9000"]

# -----------------------------------------------------------------------------
# TEST IMAGE - For running tests
# -----------------------------------------------------------------------------
FROM base AS test

# Copy all dependencies
COPY pyproject.toml pyproject.toml
COPY uv.lock uv.lock

RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential \
    pkg-config \
    libffi-dev \
    libssl-dev \
    && rm -rf /var/lib/apt/lists/*

RUN curl -LsSf https://astral.sh/uv/install.sh | sh
ENV PATH="/root/.local/bin:$PATH"

RUN uv sync --no-dev

COPY src/ /app/src/
COPY tests/ /app/tests/

ENV PYTHONPATH=/app
ENV COVERAGE_FILE=/app/.coverage

CMD ["pytest", "tests/", "-v", "--cov=src", "--cov-report=xml", "-p", "no:warnings"]

# -----------------------------------------------------------------------------
# DEVELOPMENT IMAGE - For local development
# -----------------------------------------------------------------------------
FROM base AS dev

# Copy builder dependencies
COPY --from=builder /app/.venv /app/.venv

# Copy application
COPY src/ /app/src/
COPY api/ /app/api/
COPY tests/ /app/tests/

# Set Python path
ENV PATH="/app/.venv/bin:$PATH" \
    PYTHONPATH=/app \
    PYTHONUNBUFFERED=1 \
    DEBUG=1

WORKDIR /app

# Development tools
CMD ["bash"]