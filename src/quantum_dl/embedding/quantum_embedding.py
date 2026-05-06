"""
Quantum Data Embedding Module
===========================
Classical-to-quantum data mapping with multiple encoding strategies.
"""

import numpy as np
from qiskit import QuantumCircuit
from qiskit.quantum_info import Statevector
from typing import Optional, Tuple
from dataclasses import dataclass


@dataclass
class EmbeddingConfig:
    """Configuration for quantum embedding."""
    num_qubits: int = 4
    method: str = "angle"  # angle, amplitude, iqp, basis
    normalize: bool = True


class QuantumEmbedding:
    """
    Quantum data embedding protocols.
    Supports multiple encoding strategies for classical-to-quantum mapping.
    """
    
    def __init__(self, config: EmbeddingConfig):
        self.config = config
        self.num_qubits = config.num_qubits
        self.method = config.method
        self.feature_dim = 2 ** config.num_qubits
    
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
    
    def amplitude_encode(self, data: np.ndarray) -> np.ndarray:
        """
        Amplitude encoding: encodes features into quantum state amplitudes.
        Uses log2(num_qubits) features via 2^n amplitudes.
        """
        n_features = min(len(data), self.feature_dim)
        
        if self.config.normalize:
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
    
    def iqp_encode(self, data: np.ndarray, repetitions: int = 1) -> QuantumCircuit:
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
    
    def encode(self, data: np.ndarray) -> Tuple[QuantumCircuit, Optional[np.ndarray]]:
        """
        Main embedding method - returns circuit and optional statevector.
        
        Args:
            data: Input data vector
            
        Returns:
            Tuple of (embedding_circuit, statevector_for_amplitude)
        """
        method_map = {
            "angle": lambda: (self.angle_encode(data), None),
            "amplitude": lambda: (None, self.amplitude_encode(data)),
            "iqp": lambda: (self.iqp_encode(data), None),
            "basis": lambda: (self.basis_encode(data), None),
        }
        
        encoder = method_map.get(self.method, method_map["angle"])
        return encoder()
    
    def __repr__(self) -> str:
        return f"QuantumEmbedding(num_qubits={self.num_qubits}, method={self.method})"