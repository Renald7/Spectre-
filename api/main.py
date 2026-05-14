"""
FastAPI Production Application
=============================
Production-ready API for quantum deep learning.
"""

from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel, Field
from typing import List, Optional
import numpy as np
from contextlib import asynccontextmanager

from quantum_dl.config import get_app_config, AppConfig
from quantum_dl.models.quantum_model import QuantumDeepLearningModel, HybridModelConfig
from quantum_dl.utils.logging import logger, setup_logging

# Load configuration
config = get_app_config()

# Setup logging
setup_logging(level=config.api.log_level.upper())


@asynccontextmanager
async def lifespan(app: FastAPI):
    """Application lifespan manager."""
    logger.info("Starting Quantum Deep Learning API")
    logger.info(f"Configuration: {config}")
    
    # Initialize model on startup
    model_config = HybridModelConfig(
        num_qubits=config.quantum.num_qubits,
        num_quantum_layers=config.quantum.num_layers,
        input_dim=config.model.input_dim,
        output_dim=config.model.output_dim,
        hidden_dims=config.model.hidden_dims,
        dropout_rate=config.model.dropout_rate,
        learning_rate=config.model.learning_rate,
        embedding_method="angle",
        ansatz_type=config.quantum.ansatz_type,
        seed=config.quantum.seed,
    )
    
    try:
        app.state.model = QuantumDeepLearningModel(model_config)
        logger.info(f"Model initialized: {app.state.model}")
    except Exception as e:
        logger.error(f"Failed to initialize model: {e}")
        app.state.model = None
    
    yield
    
    logger.info("Shutting down Quantum Deep Learning API")


# Create FastAPI app
app = FastAPI(
    title=config.app_name,
    description="Production Quantum Deep Learning API",
    version="1.0.0",
    lifespan=lifespan,
)

# Add CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


# ============================================================================
# Pydantic Models
# ============================================================================

class PredictionRequest(BaseModel):
    """Request model for predictions."""
    data: List[List[float]] = Field(..., description="Input features")
    batch_size: Optional[int] = Field(default=32, ge=1)


class PredictionResponse(BaseModel):
    """Response model for predictions."""
    predictions: List[List[float]]
    model_info: str


class TrainingRequest(BaseModel):
    """Request model for training."""
    X_train: List[List[float]]
    y_train: List[List[float]]
    X_val: Optional[List[List[float]]] = None
    y_val: Optional[List[List[float]]] = None
    epochs: int = Field(default=100, ge=1)
    batch_size: int = Field(default=32, ge=1)


class TrainingResponse(BaseModel):
    """Response model for training."""
    status: str
    history: dict


class KernelRequest(BaseModel):
    """Request model for kernel computation."""
    X: List[List[float]]


class KernelResponse(BaseModel):
    """Response model for kernel computation."""
    kernel_matrix: List[List[float]]


class HealthResponse(BaseModel):
    """Response model for health check."""
    status: str
    model_loaded: bool


# ============================================================================
# API Endpoints
# ============================================================================

@app.get("/", tags=["Root"])
async def root():
    """Root endpoint."""
    return {
        "name": app_config.app_name,
        "version": "1.0.0",
        "status": "running",
    }


@app.get("/health", response_model=HealthResponse, tags=["Health"])
async def health():
    """Health check endpoint."""
    return HealthResponse(
        status="healthy",
        model_loaded=app.state.model is not None,
    )


@app.post("/predict", response_model=PredictionResponse, tags=["Prediction"])
async def predict(request: PredictionRequest):
    """
    Make predictions using the quantum deep learning model.
    """
    if app.state.model is None:
        raise HTTPException(status_code=503, detail="Model not initialized")
    
    try:
        X = np.array(request.data, dtype=np.float32)
        predictions = app.state.model.predict(X)
        
        return PredictionResponse(
            predictions=predictions.tolist(),
            model_info=str(app.state.model),
        )
    except Exception as e:
        logger.error(f"Prediction error: {e}")
        raise HTTPException(status_code=500, detail=str(e))


@app.post("/train", response_model=TrainingResponse, tags=["Training"])
async def train(request: TrainingRequest):
    """
    Train the quantum deep learning model.
    """
    if app.state.model is None:
        raise HTTPException(status_code=503, detail="Model not initialized")
    
    try:
        X_train = np.array(request.X_train, dtype=np.float32)
        y_train = np.array(request.y_train, dtype=np.float32)
        
        X_val = None
        y_val = None
        if request.X_val is not None and request.y_val is not None:
            X_val = np.array(request.X_val, dtype=np.float32)
            y_val = np.array(request.y_val, dtype=np.float32)
        
        history = app.state.model.train(
            X_train, y_train,
            X_val, y_val,
            epochs=request.epochs,
            batch_size=request.batch_size,
            verbose=0,
        )
        
        return TrainingResponse(
            status="trained",
            history=history.history,
        )
    except Exception as e:
        logger.error(f"Training error: {e}")
        raise HTTPException(status_code=500, detail=str(e))


@app.post("/kernel", response_model=KernelResponse, tags=["Kernel"])
async def compute_kernel(request: KernelRequest):
    """
    Compute quantum kernel matrix.
    """
    if app.state.model is None:
        raise HTTPException(status_code=503, detail="Model not initialized")
    
    try:
        X = np.array(request.X, dtype=np.float32)
        kernel_matrix = app.state.model.compute_kernel_matrix(X)
        
        return KernelResponse(
            kernel_matrix=kernel_matrix.tolist(),
        )
    except Exception as e:
        logger.error(f"Kernel computation error: {e}")
        raise HTTPException(status_code=500, detail=str(e))


# ============================================================================
# Main
# ============================================================================

if __name__ == "__main__":
    import uvicorn
    
    uvicorn.run(
        "main:app",
        host=config.api.host,
        port=config.api.port,
        reload=config.api.reload,
        log_level=config.api.log_level,
    )