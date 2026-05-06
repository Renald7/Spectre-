FROM python:3.13-slim

WORKDIR /app

# Install system dependencies
RUN apt-get update && apt-get install -y \
    && rm -rf /var/lib/apt/lists/*

# Copy project files
COPY pyproject.toml ./
COPY uv.lock ./
COPY src/ ./src/
COPY api/ ./api/

# Install Python dependencies
RUN pip install uv && uv sync

# Expose port
EXPOSE 8000

# Run the application
CMD ["uv", "run", "python", "-m", "uvicorn", "api.main:app", "--host", "0.0.0.0", "--port", "8000"]