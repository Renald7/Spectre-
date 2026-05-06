"""
Tests for Quantum Deep Learning Package
======================================
"""

import pytest
import numpy as np


def test_quantum_config():
    """Test quantum configuration."""
    from quantum_dl.config import QuantumConfig
    
    config = QuantumConfig(num_qubits=4, num_layers=2)
    assert config.num_qubits == 4
    assert config.num_layers == 2


def test_model_config():
    """Test model configuration."""
    from quantum_dl.config import ModelConfig
    
    config = ModelConfig(input_dim=8, output_dim=1)
    assert config.input_dim == 8
    assert config.output_dim == 1


def test_quantum_circuit_layer():
    """Test quantum circuit layer."""
    from quantum_dl.layers.quantum_layer import QuantumCircuitLayer, QuantumCircuitConfig
    
    config = QuantumCircuitConfig(num_qubits=4, num_layers=2)
    layer = QuantumCircuitLayer(config)
    
    assert layer.num_qubits == 4
    assert layer.num_params > 0
    
    # Test forward pass
    params = np.random.uniform(0, 2*np.pi, layer.num_params)
    result = layer.forward(params)
    
    assert result.shape[0] == 2 ** config.num_qubits
    assert np.allclose(result.sum(), 1.0, atol=1e-5)


def test_quantum_embedding():
    """Test quantum embedding."""
    from quantum_dl.embedding.quantum_embedding import QuantumEmbedding, EmbeddingConfig
    
    config = EmbeddingConfig(num_qubits=4, method="angle")
    embedding = QuantumEmbedding(config)
    
    data = np.random.randn(4)
    circuit = embedding.angle_encode(data)
    
    assert circuit.num_qubits == 4


def test_quantum_gradient():
    """Test quantum gradient."""
    from quantum_dl.gradient.quantum_gradient import QuantumGradient, GradientConfig
    
    config = GradientConfig()
    gradient = QuantumGradient(config)
    
    assert gradient.shift == np.pi / 2
    
    # Test numeric gradient
    params = np.random.randn(10)
    def loss_fn(p):
        return np.sum(p ** 2)
    
    grads = gradient.compute_gradients_numeric(params, loss_fn)
    
    assert grads.shape == params.shape
    # For f(x) = x^2, gradient should be 2x
    expected = 2 * params
    assert np.allclose(grads, expected, atol=1e-4)


def test_quantum_kernel():
    """Test quantum kernel."""
    from quantum_dl.kernel.quantum_kernel import QuantumKernel, KernelConfig
    
    config = KernelConfig(num_qubits=4)
    kernel = QuantumKernel(config)
    
    X = np.random.randn(10, 4)
    K = kernel.compute_kernel_matrix(X)
    
    assert K.shape == (10, 10)
    # Kernel should be symmetric
    assert np.allclose(K, K.T)


def test_hybrid_model():
    """Test hybrid quantum-classical model."""
    from quantum_dl.models.quantum_model import QuantumDeepLearningModel, HybridModelConfig
    
    config = HybridModelConfig(
        input_dim=4,
        output_dim=1,
        num_qubits=4,
        num_quantum_layers=1,
    )
    
    model = QuantumDeepLearningModel(config)
    
    # Generate data
    X = np.random.randn(100, 4)
    y = np.random.randn(100, 1)
    
    # Train briefly
    history = model.train(X, y, epochs=5, verbose=0)
    assert history is not None
    
    # Make predictions
    predictions = model.predict(X[:10])
    assert predictions.shape == (10, 1)


def test_use_cases():
    """Test use cases."""
    from quantum_dl.use_cases import (
        FinancialPrediction,
        QuantumClassifier,
        QuantumAnomalyDetector,
    )
    
    # Test financial prediction
    fin = FinancialPrediction()
    X, y = fin.prepare_data(n_samples=100)
    assert X.shape[0] == y.shape[0]
    
    # Test classifier
    clf = QuantumClassifier()
    X, y = clf.prepare_data(n_samples=100)
    assert X.shape[0] == y.shape[0]
    
    # Test anomaly detector
    anomaly = QuantumAnomalyDetector()
    X, y = anomaly.prepare_data(n_samples=100)
    assert X.shape[0] == y.shape[0]


if __name__ == "__main__":
    pytest.main([__file__, "-v"])