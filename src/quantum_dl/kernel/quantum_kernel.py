"""
Quantum Kernel Module
=================
Quantum kernel computation for kernel-based learning.
"""

import numpy as np
from qiskit import QuantumCircuit
from qiskit.quantum_info import Statevector
from typing import Optional
from dataclasses import dataclass

from ..layers.quantum_layer import QuantumCircuitLayer, QuantumCircuitConfig
from ..embedding.quantum_embedding import QuantumEmbedding, EmbeddingConfig


@dataclass
class KernelConfig:
    """Configuration for quantum kernel."""
    num_qubits: int = 4
    embedding_method: str = "iqp"
    normalize: bool = True


class QuantumKernel:
    """
    Quantum Kernel for kernel-based quantum learning.
    Computes quantum fidelity between quantum states.
    """
    
    def __init__(self, config: KernelConfig):
        self.config = config
        
        # Initialize quantum components
        qc_config = QuantumCircuitConfig(
            num_qubits=config.num_qubits,
            num_layers=1,
        )
        self.quantum_layer = QuantumCircuitLayer(qc_config)
        
        emb_config = EmbeddingConfig(
            num_qubits=config.num_qubits,
            method=config.embedding_method,
        )
        self.embedding = QuantumEmbedding(emb_config)
    
    def _create_circuit(self, data: np.ndarray) -> QuantumCircuit:
        """Create quantum circuit for data embedding."""
        return self.embedding.iqp_encode(data)
    
    def compute_kernel_matrix(
        self,
        X: np.ndarray,
        Y: Optional[np.ndarray] = None,
    ) -> np.ndarray:
        """
        Compute quantum kernel matrix between datasets.
        K(x,y) = |⟨ψ(x)|ψ(y)⟩|²
        
        Args:
            X: First dataset (n samples, d features)
            Y: Second dataset (m samples, d features), defaults to X
            
        Returns:
            Kernel matrix (n, m)
        """
        if Y is None:
            Y = X
        
        n, m = len(X), len(Y)
        kernel_matrix = np.zeros((n, m))
        
        for i in range(n):
            circuit_i = self._create_circuit(X[i])
            sv_i = Statevector([1,0,0,0] + [0]*(2**self.config.num_qubits-1))
            sv_i = sv_i.evolve(circuit_i)
            
            for j in range(m):
                circuit_j = self._create_circuit(Y[j])
                sv_j = Statevector([1,0,0,0] + [0]*(2**self.config.num_qubits-1))
                sv_j = sv_j.evolve(circuit_j)
                
                # Compute fidelity: |⟨ψ_i|ψ_j⟩|²
                overlap = sum(np.conj(sv_i.data) * sv_j.data)
                kernel_matrix[i, j] = np.abs(overlap)**2
        
        return kernel_matrix
    
    def compute_kernel_vector(
        self,
        x: np.ndarray,
        Y: np.ndarray,
    ) -> np.ndarray:
        """
        Compute kernel vector between single sample and dataset.
        
        Args:
            x: Single sample (d_features,)
            Y: Dataset (n_samples, d_features)
            
        Returns:
            Kernel vector (n_samples,)
        """
        return self.compute_kernel_matrix(x.reshape(1, -1), Y).flatten()
    
    def compute_quantum_collapse(
        self,
        params: np.ndarray,
        embedding_circuit: Optional[QuantumCircuit] = None,
    ) -> np.ndarray:
        """
        Compute quantum kernel collapse for quantum embedding.
        
        Measures the collapse of quantum state under parameterized circuit.
        
        Args:
            params: Variational parameters
            embedding_circuit: Data embedding circuit
            
        Returns:
            Measurement outcomes
        """
        return self.quantum_layer.forward(params, embedding_circuit)
    
    def __repr__(self) -> str:
        return f"QuantumKernel(num_qubits={self.config.num_qubits}, method={self.config.embedding_method})"