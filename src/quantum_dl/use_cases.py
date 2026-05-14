"""
Real-World Use Cases for Quantum Deep Learning
============================================
Production-ready implementations for practical problems.
"""

import numpy as np
from dataclasses import dataclass
from typing import Tuple, Optional
from abc import ABC, abstractmethod

from quantum_dl.models.quantum_model import QuantumDeepLearningModel, HybridModelConfig
from quantum_dl.layers.quantum_layer import QuantumCircuitConfig
from quantum_dl.embedding.quantum_embedding import EmbeddingConfig
from quantum_dl.kernel.quantum_kernel import KernelConfig
from quantum_dl.utils.logging import logger


# =============================================================================
# Base Use Case
# =============================================================================

class QuantumUseCase(ABC):
    """Base class for quantum deep learning use cases."""
    
    @abstractmethod
    def prepare_data(self, n_samples: int = 1000) -> Tuple[np.ndarray, np.ndarray]:
        """Prepare training data with specified number of samples."""
        pass
    
    @abstractmethod
    def evaluate(self, predictions: np.ndarray, actual: np.ndarray) -> dict:
        """Evaluate predictions."""
        pass


# =============================================================================
# Financial Prediction Use Case
# =============================================================================

@dataclass
class FinancialConfig:
    """Configuration for financial prediction."""
    lookback_days: int = 30
    prediction_horizon: int = 1
    num_features: int = 10


class FinancialPrediction(QuantumUseCase):
    """
    Stock Price Prediction using Quantum Deep Learning.
    
    This use case demonstrates:
    - Time series forecasting
    - Technical indicator features
    - Risk-adjusted predictions
    """
    
    def __init__(
        self,
        config: Optional[FinancialConfig] = None,
        model_config: Optional[HybridModelConfig] = None,
    ):
        self.config = config or FinancialConfig()
        self.model_config = model_config or HybridModelConfig(
            input_dim=self.config.num_features,
            output_dim=1,
            num_qubits=4,
            num_quantum_layers=2,
        )
        self.model: Optional[QuantumDeepLearningModel] = None
    
    def generate_synthetic_data(
        self,
        n_samples: int = 1000,
        initial_price: float = 100.0,
    ) -> Tuple[np.ndarray, np.ndarray]:
        """
        Generate synthetic stock data with technical indicators.
        
        Features:
        - Returns (log returns)
        - Moving averages
        - Volatility
        - RSI, MACD indicators
        - Volume changes
        """
        np.random.seed(42)
        
        # Generate price series
        prices = [initial_price]
        for _ in range(n_samples + self.config.lookback_days):
            change = np.random.randn() * 0.02
            prices.append(prices[-1] * (1 + change))
        prices = np.array(prices)
        
        # Generate features
        X, y = [], []
        
        for i in range(len(prices) - self.config.lookback_days - self.config.prediction_horizon):
            # Lookback window
            window = prices[i:i + self.config.lookback_days]
            
            # Technical indicators
            returns = np.diff(np.log(window + 1e-10))
            
            features = [
                np.mean(returns),  # Mean return
                np.std(returns),  # Volatility
                window[-1] / np.mean(window) - 1,  # Momentum
                np.percentile(returns, 25),  # Downside risk
                np.percentile(returns, 75),  # Upside potential
                # Moving averages ratio
                window[-1] / np.mean(window[-5:]) - 1 if len(window) >= 5 else 0,
                window[-1] / np.mean(window[-10:]) - 1 if len(window) >= 10 else 0,
                # RSI-like
                np.mean(returns > 0) if len(returns) > 0 else 0.5,
                # Volume proxy
                np.random.rand(),
                np.random.rand(),
            ][:self.config.num_features]
            
            X.append(features)
            
            # Target: next period return
            next_return = (prices[i + self.config.lookback_days + self.config.prediction_horizon] 
                         / prices[i + self.config.lookback_days] - 1)
            y.append([next_return])
        
        return np.array(X, dtype=np.float32), np.array(y, dtype=np.float32)
    
    def prepare_data(self, n_samples: int = 1000) -> Tuple[np.ndarray, np.ndarray]:
        """Prepare training data."""
        return self.generate_synthetic_data(n_samples=n_samples)
    
    def train(
        self,
        X_train: np.ndarray,
        y_train: np.ndarray,
        epochs: int = 50,
    ) -> QuantumDeepLearningModel:
        """Train the financial prediction model."""
        logger.info(f"Training financial model on {len(X_train)} samples")
        
        self.model = QuantumDeepLearningModel(self.model_config)
        self.model.train(X_train, y_train, epochs=epochs, verbose=0)
        
        return self.model
    
    def predict(self, X: np.ndarray) -> np.ndarray:
        """Make predictions."""
        if self.model is None:
            raise ValueError("Model not trained")
        return self.model.predict(X)
    
    def evaluate(
        self,
        predictions: np.ndarray,
        actual: np.ndarray,
    ) -> dict:
        """Evaluate predictions."""
        mse = np.mean((predictions - actual) ** 2)
        mae = np.mean(np.abs(predictions - actual))
        
        # Direction accuracy
        pred_direction = (predictions > 0).astype(int)
        actual_direction = (actual > 0).astype(int)
        direction_accuracy = np.mean(pred_direction == actual_direction)
        
        return {
            "mse": float(mse),
            "mae": float(mae),
            "direction_accuracy": float(direction_accuracy),
            "rmse": float(np.sqrt(mse)),
        }
    
    def risk_adjust(self, predictions: np.ndarray, volatility: float = 0.02) -> np.ndarray:
        """Risk-adjust predictions using volatility scaling."""
        return predictions * volatility


# =============================================================================
# Classification Use Case
# =============================================================================

@dataclass
class ClassificationConfig:
    """Configuration for classification."""
    num_classes: int = 2
    num_features: int = 8
    balanced: bool = True


class QuantumClassifier(QuantumUseCase):
    """
    Binary Classification using Quantum Deep Learning.
    
    Use cases:
    - Credit risk prediction
    - Customer churn prediction
    - Fraud detection
    """
    
    def __init__(
        self,
        config: Optional[ClassificationConfig] = None,
        model_config: Optional[HybridModelConfig] = None,
    ):
        self.config = config or ClassificationConfig()
        self.model_config = model_config or HybridModelConfig(
            input_dim=self.config.num_features,
            output_dim=1,
            num_qubits=4,
            num_quantum_layers=2,
        )
        self.model: Optional[QuantumDeepLearningModel] = None
    
    def generate_synthetic_data(
        self,
        n_samples: int = 1000,
    ) -> Tuple[np.ndarray, np.ndarray]:
        """Generate synthetic classification data."""
        np.random.seed(42)
        
        # Generate features (e.g., customer attributes)
        X = np.random.randn(n_samples, self.config.num_features).astype(np.float32)
        
        # Generate labels with some correlation to features
        weights = np.random.randn(self.config.num_features) * 0.5
        linear_score = X @ weights + np.random.randn(n_samples) * 0.5
        probabilities = 1 / (1 + np.exp(-linear_score))
        
        if self.config.balanced:
            # Balance classes
            labels = (np.random.rand(n_samples) < probabilities).astype(float)
        else:
            # Imbalanced (80/20)
            labels = (np.random.rand(n_samples) < probabilities * 0.5).astype(float)
        
        y = labels.reshape(-1, 1)
        
        return X, y
    
    def prepare_data(self, n_samples: int = 1000) -> Tuple[np.ndarray, np.ndarray]:
        """Prepare classification data."""
        return self.generate_synthetic_data(n_samples=n_samples)
    
    def train(
        self,
        X_train: np.ndarray,
        y_train: np.ndarray,
        epochs: int = 50,
    ) -> QuantumDeepLearningModel:
        """Train the classifier."""
        logger.info(f"Training classifier on {len(X_train)} samples")
        
        self.model = QuantumDeepLearningModel(self.model_config)
        self.model.train(X_train, y_train, epochs=epochs, verbose=0)
        
        return self.model
    
    def predict(self, X: np.ndarray) -> np.ndarray:
        """Make predictions."""
        if self.model is None:
            raise ValueError("Model not trained")
        return self.model.predict(X)
    
    def predict_proba(self, X: np.ndarray) -> np.ndarray:
        """Predict class probabilities."""
        predictions = self.predict(X)
        return np.hstack([1 - predictions, predictions])
    
    def evaluate(
        self,
        predictions: np.ndarray,
        actual: np.ndarray,
    ) -> dict:
        """Evaluate classification."""
        pred_labels = (predictions > 0.5).astype(int)
        actual_labels = (actual > 0.5).astype(int)
        
        accuracy = np.mean(pred_labels == actual_labels)
        
        # Confusion matrix elements
        tp = np.sum((pred_labels == 1) & (actual_labels == 1))
        tn = np.sum((pred_labels == 0) & (actual_labels == 0))
        fp = np.sum((pred_labels == 1) & (actual_labels == 0))
        fn = np.sum((pred_labels == 0) & (actual_labels == 1))
        
        precision = tp / (tp + fp) if (tp + fp) > 0 else 0
        recall = tp / (tp + fn) if (tp + fn) > 0 else 0
        f1 = 2 * precision * recall / (precision + recall) if (precision + recall) > 0 else 0
        
        return {
            "accuracy": float(accuracy),
            "precision": float(precision),
            "recall": float(recall),
            "f1": float(f1),
            "confusion_matrix": {"tp": int(tp), "tn": int(tn), "fp": int(fp), "fn": int(fn)},
        }


# =============================================================================
# Anomaly Detection Use Case
# =============================================================================

@dataclass
class AnomalyConfig:
    """Configuration for anomaly detection."""
    num_features: int = 8
    contamination: float = 0.1


class QuantumAnomalyDetector(QuantumUseCase):
    """
    Anomaly Detection using Quantum Kernel Methods.
    
    Use cases:
    - Network intrusion detection
    - Credit card fraud
    - Manufacturing defect detection
    """
    
    def __init__(
        self,
        config: Optional[AnomalyConfig] = None,
        model_config: Optional[HybridModelConfig] = None,
    ):
        self.config = config or AnomalyConfig()
        self.model_config = model_config or HybridModelConfig(
            input_dim=self.config.num_features,
            output_dim=1,
            num_qubits=4,
            num_quantum_layers=2,
        )
        self.model: Optional[QuantumDeepLearningModel] = None
        self.threshold: float = 0.0
    
    def generate_synthetic_data(
        self,
        n_samples: int = 1000,
    ) -> Tuple[np.ndarray, np.ndarray]:
        """Generate synthetic anomaly data."""
        np.random.seed(42)
        
        n_normal = int(n_samples * (1 - self.config.contamination))
        n_anomaly = n_samples - n_normal
        
        # Normal data: Gaussian distribution
        X_normal = np.random.randn(n_normal, self.config.num_features).astype(np.float32)
        y_normal = np.zeros((n_normal, 1))
        
        # Anomalies: displaced distribution
        X_anomaly = np.random.randn(n_anomaly, self.config.num_features).astype(np.float32) + 3.0
        y_anomaly = np.ones((n_anomaly, 1))
        
        # Combine
        X = np.vstack([X_normal, X_anomaly])
        y = np.vstack([y_normal, y_anomaly])
        
        # Shuffle
        shuffle_idx = np.random.permutation(n_samples)
        return X[shuffle_idx], y[shuffle_idx]
    
    def prepare_data(self, n_samples: int = 1000) -> Tuple[np.ndarray, np.ndarray]:
        """Prepare anomaly data."""
        return self.generate_synthetic_data(n_samples=n_samples)
    
    def train(
        self,
        X_train: np.ndarray,
        y_train: np.ndarray,
        epochs: int = 50,
    ) -> QuantumDeepLearningModel:
        """Train the anomaly detector."""
        logger.info(f"Training anomaly detector on {len(X_train)} samples")
        
        self.model = QuantumDeepLearningModel(self.model_config)
        self.model.train(X_train, y_train, epochs=epochs, verbose=0)
        
        return self.model
    
    def fit_threshold(self, X: np.ndarray, percentile: float = 90):
        """Fit anomaly detection threshold."""
        predictions = self.predict(X)
        self.threshold = np.percentile(predictions, percentile)
        return self.threshold
    
    def detect(self, X: np.ndarray) -> np.ndarray:
        """Detect anomalies."""
        predictions = self.predict(X)
        return (predictions > self.threshold).astype(int)
    
    def evaluate(
        self,
        predictions: np.ndarray,
        actual: np.ndarray,
    ) -> dict:
        """Evaluate anomaly detection."""
        pred_labels = (predictions > 0.5).astype(int)
        actual_labels = actual.flatten().astype(int)
        
        accuracy = np.mean(pred_labels == actual_labels)
        
        tp = np.sum((pred_labels == 1) & (actual_labels == 1))
        tn = np.sum((pred_labels == 0) & (actual_labels == 0))
        fp = np.sum((pred_labels == 1) & (actual_labels == 0))
        fn = np.sum((pred_labels == 0) & (actual_labels == 1))
        
        return {
            "accuracy": float(accuracy),
            "true_positives": int(tp),
            "true_negatives": int(tn),
            "false_positives": int(fp),
            "false_negatives": int(fn),
        }
    
    def predict(self, X: np.ndarray) -> np.ndarray:
        """Make predictions."""
        if self.model is None:
            raise ValueError("Model not trained")
        return self.model.predict(X)


# =============================================================================
# Demo Function
# =============================================================================

def run_all_use_cases():
    """Run all use case demonstrations."""
    logger.info("=" * 60)
    logger.info("RUNNING QUANTUM DEEP LEARNING USE CASES")
    logger.info("=" * 60)
    
    results = {}
    
    # Financial Prediction
    logger.info("\n[1] Financial Prediction")
    logger.info("-" * 40)
    fin = FinancialPrediction()
    X, y = fin.prepare_data()
    
    # Split data
    split = int(0.8 * len(X))
    X_train, y_train = X[:split], y[:split]
    X_test, y_test = X[split:], y[split:]
    
    fin.train(X_train, y_train, epochs=20)
    predictions = fin.predict(X_test)
    results["financial"] = fin.evaluate(predictions, y_test)
    logger.info(f"Results: {results['financial']}")
    
    # Classification
    logger.info("\n[2] Classification")
    logger.info("-" * 40)
    clf = QuantumClassifier()
    X, y = clf.prepare_data()
    
    split = int(0.8 * len(X))
    X_train, y_train = X[:split], y[:split]
    X_test, y_test = X[split:], y[split:]
    
    clf.train(X_train, y_train, epochs=20)
    predictions = clf.predict(X_test)
    results["classification"] = clf.evaluate(predictions, y_test)
    logger.info(f"Results: {results['classification']}")
    
    # Anomaly Detection
    logger.info("\n[3] Anomaly Detection")
    logger.info("-" * 40)
    anomaly = QuantumAnomalyDetector()
    X, y = anomaly.prepare_data()
    
    split = int(0.8 * len(X))
    X_train, y_train = X[:split], y[:split]
    X_test, y_test = X[split:], y[split:]
    
    anomaly.train(X_train, y_train, epochs=20)
    predictions = anomaly.predict(X_test)
    results["anomaly"] = anomaly.evaluate(predictions, y_test)
    logger.info(f"Results: {results['anomaly']}")
    
    logger.info("\n" + "=" * 60)
    logger.info("ALL USE CASES COMPLETE")
    logger.info("=" * 60)
    
    return results


if __name__ == "__main__":
    run_all_use_cases()