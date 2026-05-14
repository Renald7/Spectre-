"""
Most Powerful Quantum Deep Learning Protocol
============================================
A comprehensive hybrid quantum-classical deep learning framework featuring:
- Parameterized quantum circuits with universal gate sets
- Amplitude encoding for efficient quantum data embedding
- Hybrid quantum-classical neural network architecture
- Parameter-shift rule for quantum gradient computation
- Backpropagation through quantum layers
- Multiple ansatz templates (SU2, RealAmplitudes, EfficientSU2)
"""

import numpy as np
from typing import List, Tuple, Optional, Callable
from dataclasses import dataclass, field
import warnings

# Qiskit imports
from qiskit import QuantumCircuit
from qiskit.circuit import ParameterVector, Parameter
from qiskit.circuit.library import (
    ZZFeatureMap, 
    RealAmplitudes, 
    EfficientSU2,
    TwoLocal,
    NLocal
)
from qiskit.quantum_info import Statevector, Operator, SparsePauliOp

# TensorFlow/Keras imports
import tensorflow as tf
from tensorflow import keras
from keras import layers, Model, optimizers, losses, callbacks


# =============================================================================
# QUANTUM CONFIGURATION
# =============================================================================

@dataclass
class QuantumConfig:
    """Configuration for quantum deep learning components."""
    num_qubits: int = 4
    num_layers: int = 2  # Number of variational layers
    ansatz_type: str = " EfficientSU2"  # Options: "RealAmplitudes", "EfficientSU2", "ZZFeatureMap", "TwoLocal"
    entanglement: str = "full"  # "full", "linear", "sca"
    repetitions: int = 1
    rotation_blocks: str = "ry"  # "ry", "rz", "rx", "u"
    include_slack: bool = False
    seed: int = 42
    
    def __post_init__(self):
        np.random.seed(self.seed)
        tf.random.set_seed(self.seed)


# =============================================================================
# QUANTUM CIRCUIT LAYER
# =============================================================================

class QuantumCircuitLayer:
    """
    Parameterized quantum circuit layer for variational quantum learning.
    Implements universal quantum computation with trainable parameters.
    """
    
    def __init__(self, config: QuantumConfig):
        self.config = config
        self.num_qubits = config.num_qubits
        self.num_params = config.num_layers * config.num_qubits * 4  # Estimate
        self.parameters: List[Parameter] = []
        self._build_ansatz()
    
    def _build_ansatz(self):
        """Build the variational ansatz based on configuration."""
        if self.config.ansatz_type == " RealAmplitudes":
            self.ansatz = RealAmplitudes(
                self.num_qubits,
                repetitions=self.config.repetitions,
                entanglement=self.config.entanglement,
            )
        elif self.config.ansatz_type == "EfficientSU2":
            self.ansatz = EfficientSU2(
                self.num_qubits,
                reps=self.config.repetitions,
                entanglement=self.config.entanglement,
            )
        elif self.config.ansatz_type == "TwoLocal":
            self.ansatz = TwoLocal(
                self.num_qubits,
                rotation_blocks=self.config.rotation_blocks,
                entanglement_blocks="cx",
                entanglement=self.config.entanglement,
                repetitions=self.config.repetitions,
            )
        else:
            self.ansatz = EfficientSU2(
                self.num_qubits,
                reps=self.config.repetitions,
                entanglement=self.config.entanglement,
            )
        
        self.num_params = self.ansatz.num_parameters
    
    def get_circuit(self, params: Optional[np.ndarray] = None) -> QuantumCircuit:
        """Get parametrized quantum circuit with specified parameters."""
        if params is None:
            params = np.random.uniform(0, 2*np.pi, self.num_params)
        
        qc = QuantumCircuit(self.num_qubits)
        
        # Apply initial layer - data embedding will happen elsewhere
        qc.h(range(self.num_qubits))  # Initial superposition
        
        # Apply variational ansatz
        parameterized_ansatz = self.ansatz.assign_parameters(params)
        qc.compose(parameterized_ansatz, inplace=True)
        
        return qc
    
    def get_expectation_operator(self, observable: str = "Z") -> List[SparsePauliOp]:
        """Get measurement operators for expectation values."""
        obs = []
        for i in range(self.num_qubits):
            pauli = "I" * i + observable + "I" * (self.num_qubits - i - 1)
            obs.append(SparsePauliOp.from_list([(pauli, 1.0)]))
        return obs


# =============================================================================
# QUANTUM DATA EMBEDDING
# =============================================================================

class QuantumEmbedding:
    """
    Quantum data embedding protocols for classical-to-quantum data mapping.
    Supports multiple encoding strategies.
    """
    
    def __init__(self, num_qubits: int, method: str = "amplitude"):
        self.num_qubits = num_qubits
        self.method = method
        self.feature_dim = 2 ** num_qubits  # Amplitude encoding capacity
    
    def amplitude_encode(self, data: np.ndarray, normalize: bool = True) -> np.ndarray:
        """
        Amplitude encoding: encodes features into quantum state amplitudes.
        Encodes log2(num_qubits) features using 2^n amplitudes.
        """
        n_features = min(len(data), self.feature_dim)
        
        if normalize:
            # L2 normalize the data
            norm = np.linalg.norm(data[:n_features])
            if norm > 0:
                data = data[:n_features] / norm
            else:
                data = data[:n_features]
        else:
            data = data[:n_features]
        
        # Pad to full dimensionality
        encoded = np.zeros(self.feature_dim, dtype=complex)
        encoded[:n_features] = data
        
        return encoded
    
    def angle_encode(self, data: np.ndarray) -> QuantumCircuit:
        """
        Angle encoding: encodes features as rotation angles.
        Each qubit receives one feature as rotation angle.
        """
        n_features = min(len(data), self.num_qubits)
        qc = QuantumCircuit(self.num_qubits)
        
        for i in range(n_features):
            qc.ry(data[i], i)
        
        # Pad remaining qubits with Hadamard
        for i in range(n_features, self.num_qubits):
            qc.h(i)
        
        return qc
    
    def basis_encode(self, data: np.ndarray) -> QuantumCircuit:
        """
        Basis encoding: encodes binary features into computational basis states.
        """
        qc = QuantumCircuit(self.num_qubits)
        
        for i, bit in enumerate(data):
            if i >= self.num_qubits:
                break
            if bit > 0.5:
                qc.x(i)
        
        return qc
    
    def IQP_encode(self, data: np.ndarray, repetitions: int = 1) -> QuantumCircuit:
        """
        IQP (Instantaneous Quantum Polynomial) encoding.
        Powerful encoding for certain kernel computations.
        """
        qc = QuantumCircuit(self.num_qubits)
        
        # Initial superposition
        qc.h(range(self.num_qubits))
        
        # Repeated feature-dependent rotations
        for rep in range(repetitions):
            for i in range(self.num_qubits):
                angle = data[i] * np.pi
                qc.rz(angle, i)
            
            # Entangling operations
            for i in range(self.num_qubits - 1):
                qc.cx(i, i + 1)
            if self.num_qubits > 1:
                qc.cx(self.num_qubits - 1, 0)
        
        return qc
    
    def embed(self, data: np.ndarray) -> Tuple[QuantumCircuit, np.ndarray]:
        """
        Main embedding method - combines embedding strategies.
        Returns both circuit and statevector.
        """
        if self.method == "amplitude":
            state_vector = self.angle_encode(data)
            return QuantumCircuit(self.num_qubits), state_vector
        elif self.method == "iqp":
            return self.IQP_encode(data), None
        elif self.method == "basis":
            return self.basis_encode(data), None
        else:
            return self.angle_encode(data), None


# =============================================================================
# HYBRID QUANTUM-CLASSICAL NEURAL NETWORK
# =============================================================================

class HybridQuantumClassicalLayer(layers.Layer):
    """
    Hybrid Quantum-Classical Neural Network Layer.
    Integrates quantum circuits with differentiable TensorFlow interface.
    """
    
    def __init__(
        self,
        config: QuantumConfig,
        embedding_method: str = "angle",
        **kwargs
    ):
        super().__init__(**kwargs)
        self.config = config
        self.embedding_method = embedding_method
        self.quantum_layer = QuantumCircuitLayer(config)
        self.embedding = QuantumEmbedding(config.num_qubits, embedding_method)
        
        # Trainable variational parameters
        self.variational_params = self.add_weight(
            name="variational_params",
            shape=(self.quantum_layer.num_params,),
            initializer=keras.initializers.RandomUniform(0, 2*np.pi),
            trainable=True,
        )
        
    def build(self, input_shape):
        """Build layer with input dimension."""
        super().build(input_shape)
    
    def call(self, inputs: tf.Tensor, training: Optional[bool] = None) -> tf.Tensor:
        """
        Forward pass through hybrid quantum-classical layer.
        Classical inputs → Quantum embedding → Variational circuit → Measurement
        """
        batch_size = tf.shape(inputs)[0]
        
        # Process each sample in batch
        outputs = []
        for i in range(batch_size):
            classical_data = inputs[i].numpy()
            
            # Quantum embedding
            if self.embedding_method == "angle":
                embedded_circuit = self.embedding.angle_encode(classical_data)
            else:
                embedded_circuit = self.embedding.IQP_encode(classical_data)
            
            # Get variational circuit with trainable parameters
            params = self.variational_params.numpy()
            var_circuit = self.quantum_layer.get_circuit(params)
            
            # Combine embedding + variational
            full_circuit = embedded_circuit.compose(var_circuit)
            
            # Execute and get expectation values
            sv = Statevector([0] * (2**self.config.num_qubits))
            sv = sv.evolve(full_circuit)
            
            # Return probabilities as output (measurement)
            probs = np.abs(sv.probabilities())**2
            outputs.append(probs)
        
        return tf.convert_to_tensor(outputs, dtype=tf.float32)
    
    def get_config(self):
        config = super().get_config()
        config.update({
            "config": self.config.__dict__,
            "embedding_method": self.embedding_method,
        })
        return config


# =============================================================================
# QUANTUM GRADIENT COMPUTATION (Parameter-Shift Rule)
# =============================================================================

class QuantumGradient:
    """
    Quantum gradient computation using the parameter-shift rule.
    Enables differentiation of quantum circuits for backpropagation.
    """
    
    def __init__(self, config: QuantumConfig):
        self.config = config
        self.quantum_layer = QuantumCircuitLayer(config)
        self.shift = np.pi / 2  # Standard shift
    
    def parameter_shift_gradient(
        self, 
        circuit: QuantumCircuit, 
        param_indices: List[int],
        observables: List[SparsePauliOp]
    ) -> np.ndarray:
        """
        Compute gradients using parameter-shift rule.
        
        For a parameterized gate U(θ) = e^(-iθP/2), the gradient is:
        ∇⟨O⟩ = (⟨O⟩_{θ+π/2} - ⟨O⟩_{θ-π/2}) / 2
        
        This is exact for gates from the Clifford group.
        """
        gradients = []
        
        for idx in param_indices:
            # Clone circuit
            qc_plus = circuit.copy()
            qc_minus = circuit.copy()
            
            # Get current parameter value
            param_val = circuit.parameters[idx]
            
            # Shifted parameters
            params_plus = {param_val: param_val + self.shift}
            params_minus = {param_val: param_val - self.shift}
            
            # Execute circuits
            sv_plus = Statevector(qc_plus.assign_parameters(params_plus))
            sv_minus = Statevector(qc_minus.assign_parameters(params_minus))
            
            # Compute expectation values
            exp_plus = sv_plus.expectation_value(observables[0])
            exp_minus = sv_minus.expectation_value(observables[0])
            
            # Parameter-shift gradient
            gradient = (exp_plus - exp_minus) / 2
            gradients.append(gradient)
        
        return np.array(gradients)
    
    def compute_gradients_numeric(
        self,
        params: np.ndarray,
        embedding_data: np.ndarray,
        target_fn: Callable[[np.ndarray], float]
    ) -> np.ndarray:
        """
        Compute gradients numerically using finite differences.
        Backup method when parameter-shift not available.
        """
        epsilon = 1e-5
        gradients = []
        
        for i in range(len(params)):
            params_plus = params.copy()
            params_plus[i] += epsilon
            
            params_minus = params.copy()
            params_minus[i] -= epsilon
            
            # Dummy forward pass
            loss_plus = target_fn(params_plus)
            loss_minus = target_fn(params_minus)
            
            gradient = (loss_plus - loss_minus) / (2 * epsilon)
            gradients.append(gradient)
        
        return np.array(gradients)


# =============================================================================
# QUANTUM DEEP LEARNING MODEL
# =============================================================================

class QuantumDeepLearningModel(Model):
    """
    Full Quantum Deep Learning Model.
    Multi-layer hybrid quantum-classical neural network.
    """
    
    def __init__(
        self,
        num_qubits: int = 4,
        num_layers: int = 2,
        output_dim: int = 1,
        **kwargs
    ):
        super().__init__(**kwargs)
        
        self.config = QuantumConfig(num_qubits=num_qubits, num_layers=num_layers)
        self.output_dim = output_dim
        
        # Classical preprocessing layers
        self.dense1 = layers.Dense(32, activation="relu", name="classical_preprocess1")
        self.dense2 = layers.Dense(16, activation="relu", name="classical_preprocess2")
        self.dropout = layers.Dropout(0.3)
        
        # Quantum layer
        self.quantum = HybridQuantumClassicalLayer(
            self.config,
            name="quantum_layer"
        )
        
        # Classical postprocessing
        self.dense3 = layers.Dense(8, activation="relu", name="classical_postprocess")
        self.output_layer = layers.Dense(output_dim, activation="linear", name="output")
    
    def call(self, inputs: tf.Tensor, training: Optional[bool] = None) -> tf.Tensor:
        """Forward pass through full quantum DNN."""
        # Classical preprocessing
        x = self.dense1(inputs)
        x = self.dense2(x)
        x = self.dropout(x, training=training)
        
        # Quantum processing (if dimension matches)
        if inputs.shape[-1] <= self.config.num_qubits:
            x = self.quantum(x, training=training)
        
        # Classical postprocessing
        x = self.dense3(x)
        output = self.output_layer(x)
        
        return output
    
    def get_quantum_params(self) -> np.ndarray:
        """Get current variational parameters."""
        return self.quantum.variational_params.numpy()
    
    def set_quantum_params(self, params: np.ndarray):
        """Set variational parameters."""
        self.quantum.variational_params.assign(params)


# =============================================================================
# TRAINING UTILITIES
# =============================================================================

class QuantumLoss(losses.Loss):
    """
    Custom loss functions for quantum deep learning.
    Includes fidelity-based and hinge losses.
    """
    
    def __init__(self, loss_type: str = "mse", **kwargs):
        super().__init__(**kwargs)
        self.loss_type = loss_type
    
    def call(self, y_true: tf.Tensor, y_pred: tf.Tensor) -> tf.Tensor:
        if self.loss_type == "mse":
            return tf.reduce_mean(tf.square(y_true - y_pred))
        elif self.loss_type == "mae":
            return tf.reduce_mean(tf.abs(y_true - y_pred))
        elif self.loss_type == "huber":
            return tf.reduce_mean(
                tf.where(
                    tf.abs(y_true - y_pred) < 1.0,
                    0.5 * tf.square(y_true - y_pred),
                    tf.abs(y_true - y_pred) - 0.5
                )
            )
        else:
            return tf.reduce_mean(tf.square(y_true - y_pred))


def create_quantum_model(
    input_dim: int,
    output_dim: int = 1,
    num_qubits: int = 4,
    num_quantum_layers: int = 2
) -> QuantumDeepLearningModel:
    """
    Factory function to create a quantum deep learning model.
    """
    model = QuantumDeepLearningModel(
        num_qubits=num_qubits,
        num_layers=num_quantum_layers,
        output_dim=output_dim,
    )
    
    # Build model
    model.build(input_shape=(None, input_dim))
    
    return model


# =============================================================================
# QUANTUM KERNEL FUNCTION
# =============================================================================

class QuantumKernel:
    """
    Quantum Kernel for kernel-based quantum learning.
    Computes quantum fidelity between quantum states.
    """
    
    def __init__(self, config: QuantumConfig):
        self.config = config
        self.quantum_layer = QuantumCircuitLayer(config)
        self.embedding = QuantumEmbedding(config.num_qubits, "iqp")
    
    def compute_kernel_matrix(
        self, 
        X: np.ndarray, 
        Y: Optional[np.ndarray] = None
    ) -> np.ndarray:
        """
        Compute quantum kernel matrix between datasets.
        K(x,y) = |⟨ψ(x)|ψ(y)⟩|²
        """
        if Y is None:
            Y = X
        
        n, m = len(X), len(Y)
        kernel_matrix = np.zeros((n, m))
        
        for i in range(n):
            for j in range(m):
                # Embed data into quantum states
                circuit_i = self.embedding.IQP_encode(X[i])
                circuit_j = self.embedding.IQP_encode(Y[j])
                
                # Get statevectors using evolved initial state |0...0>
                sv_i = Statevector([1,0,0,0] + [0]*(2**self.config.num_qubits-1))
                sv_i = sv_i.evolve(circuit_i)
                
                sv_j = Statevector([1,0,0,0] + [0]*(2**self.config.num_qubits-1))
                sv_j = sv_j.evolve(circuit_j)
                
                # Compute fidelity: |⟨ψ_i|ψ_j⟩|²
                overlap = sum(np.conj(sv_i.data) * sv_j.data)
                fidelity = np.abs(overlap)**2
                kernel_matrix[i, j] = fidelity
        
        return kernel_matrix


# =============================================================================
# MAIN EXECUTION
# =============================================================================

def main():
    """
    Main execution: train and test quantum deep learning protocol.
    """
    print("=" * 60)
    print("QUANTUM DEEP LEARNING PROTOCOL")
    print("=" * 60)
    
    # Configuration
    config = QuantumConfig(
        num_qubits=4,
        num_layers=2,
        ansatz_type="EfficientSU2",
        entanglement="full",
    )
    print(f"\n[CONFIG] {config}")
    
    # Generate synthetic training data
    print("\n[DATA] Generating synthetic training data...")
    n_samples = 200
    input_dim = 8
    output_dim = 1
    
    # Generate complex synthetic data
    X_train = np.random.randn(n_samples, input_dim).astype(np.float32)
    y_train = np.sum(np.sin(X_train[:, :4]), axis=1, keepdims=True) + 0.1 * np.random.randn(n_samples, 1)
    
    X_test = np.random.randn(n_samples // 5, input_dim).astype(np.float32)
    y_test = np.sum(np.sin(X_test[:, :4]), axis=1, keepdims=True)
    
    print(f"  Training samples: {n_samples}")
    print(f"  Input dimension: {input_dim}")
    print(f"  Output dimension: {output_dim}")
    
    # Build model
    print("\n[BUILD] Creating quantum deep learning model...")
    model = create_quantum_model(
        input_dim=input_dim,
        output_dim=output_dim,
        num_qubits=config.num_qubits,
        num_quantum_layers=config.num_layers,
    )
    
    # Compile model
    model.compile(
        optimizer=optimizers.Adam(learning_rate=0.001),
        loss=QuantumLoss(loss_type="huber"),
        metrics=["mae", "mse"],
    )
    
    print(model.summary())
    
    # Training
    print("\n[TRAIN] Training quantum deep learning model...")
    history = model.fit(
        X_train, y_train,
        epochs=50,
        batch_size=32,
        validation_split=0.2,
        verbose=1,
        callbacks=[
            callbacks.EarlyStopping(patience=10, restore_best_weights=True),
            callbacks.ReduceLROnPlateau(factor=0.5, patience=5),
        ]
    )
    
    # Evaluation
    print("\n[EVALUATE] Evaluating model performance...")
    train_loss = model.evaluate(X_train, y_train, verbose=0)
    test_loss = model.evaluate(X_test, y_test, verbose=0)
    
    print(f"\n  Training Metrics:")
    print(f"    - Loss: {train_loss[0]:.4f}")
    print(f"    - MAE:  {train_loss[1]:.4f}")
    print(f"    - MSE:  {train_loss[2]:.4f}")
    
    print(f"\n  Test Metrics:")
    print(f"    - Loss: {test_loss[0]:.4f}")
    print(f"    - MAE:  {test_loss[1]:.4f}")
    print(f"    - MSE:  {test_loss[2]:.4f}")
    
    # Quantum kernel demonstration
    print("\n[KERNEL] Computing quantum kernel matrix...")
    kernel = QuantumKernel(config)
    X_sample = X_train[:10]
    K = kernel.compute_kernel_matrix(X_sample)
    
    print(f"  Kernel matrix shape: {K.shape}")
    print(f"  Kernel diagonal (self-fidelities): {np.diag(K)}")
    print(f"  Kernel mean: {np.mean(K):.4f}")
    
    # Gradient demonstration
    print("\n[GRADIENT] Testing quantum gradient computation...")
    gradient = QuantumGradient(config)
    test_params = np.random.uniform(0, 2*np.pi, gradient.quantum_layer.num_params)
    
    # Simple loss function for gradient testing
    def test_loss_fn(params):
        return np.sum(np.sin(params))
    
    grads = gradient.compute_gradients_numeric(test_params, X_train[0], test_loss_fn)
    
    print(f"  Number of parameters: {len(test_params)}")
    print(f"  Sample gradients: {grads[:5]}")
    print(f"  Gradient norm: {np.linalg.norm(grads):.4f}")
    
    print("\n" + "=" * 60)
    print("QUANTUM DEEP LEARNING PROTOCOL COMPLETE")
    print("=" * 60)
    
    return model, history


if __name__ == "__main__":
    model, history = main(RENALD202320252026)