"""
Quantum Deep Learning Configuration Module
========================================
Production-ready configuration management with pydantic.
"""

from pydantic import Field
from pydantic_settings import BaseSettings, SettingsConfigDict
from typing import Literal
from functools import lru_cache


class QuantumConfig(BaseSettings):
    """Quantum circuit configuration."""
    model_config = SettingsConfigDict(env_prefix="QUANTUM_")
    
    num_qubits: int = Field(default=4, ge=2, le=16, description="Number of qubits")
    num_layers: int = Field(default=2, ge=1, le=10, description="Variational layers")
    ansatz_type: Literal["EfficientSU2", "RealAmplitudes", "TwoLocal", "ZZFeatureMap"] = "EfficientSU2"
    entanglement: Literal["full", "linear", "sca", "pairwise"] = "full"
    repetitions: int = Field(default=1, ge=1, le=5)
    rotation_blocks: Literal["ry", "rz", "rx", "u"] = "ry"
    seed: int = 42


class ModelConfig(BaseSettings):
    """Model architecture configuration."""
    model_config = SettingsConfigDict(env_prefix="MODEL_")
    
    input_dim: int = Field(default=8, ge=1, description="Input feature dimension")
    output_dim: int = Field(default=1, ge=1, description="Output dimension")
    hidden_dims: list[int] = Field(default=[32, 16])
    dropout_rate: float = Field(default=0.3, ge=0.0, le=1.0)
    learning_rate: float = Field(default=0.001, gt=0)
    batch_size: int = Field(default=32, ge=1)
    epochs: int = Field(default=100, ge=1)
    early_stopping_patience: int = Field(default=10, ge=1)


class APIConfig(BaseSettings):
    """API server configuration."""
    model_config = SettingsConfigDict(env_prefix="API_")
    
    host: str = "0.0.0.0"
    port: int = Field(default=8000, ge=1024, le=65535)
    workers: int = 1
    reload: bool = False
    log_level: Literal["trace", "debug", "info", "warning", "error"] = "info"


class AppConfig(BaseSettings):
    """Main application configuration."""
    model_config = SettingsConfigDict(env_file=".env", env_file_encoding="utf-8")
    
    app_name: str = "Quantum Deep Learning API"
    debug: bool = False
    environment: Literal["development", "staging", "production"] = "development"
    
    quantum: QuantumConfig = Field(default_factory=QuantumConfig)
    model: ModelConfig = Field(default_factory=ModelConfig)
    api: APIConfig = Field(default_factory=APIConfig)


@lru_cache
def get_app_config() -> AppConfig:
    """Get cached application configuration."""
    return AppConfig()