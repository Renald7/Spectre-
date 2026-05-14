"""
Quantum Circuit Layer Module
=====================
Parameterized quantum circuits for variational quantum learning.
"""

import numpy as np
from qiskit import QuantumCircuit
from qiskit.circuit import Parameter
from qiskit.circuit.library import (
    EfficientSU2,
    RealAmplitudes,
    TwoLocal,
    ZZFeatureMap,
)
from qiskit.quantum_info import Statevector, SparsePauliOp
from typing import Optional
from dataclasses import dataclass


@dataclass
class QuantumCircuitConfig:
    """Configuration for quantum circuit layer."""
    num_qubits: int = 4
    num_layers: int = 2
    ansatz_type: str = "EfficientSU2"
    entanglement: str = "full"
    repetitions: int = 1
    rotation_blocks: str = "ry"
    seed: int = 42


class QuantumCircuitLayer:
    """
    Parameterized quantum circuit layer for variational quantum learning.
    Implements universal quantum computation with trainable parameters.
    """
    
    def __init__(self, config: QuantumCircuitConfig):
        self.config = config
        self.num_qubits = config.num_qubits
        self.config.seed = config.seed
        np.random.seed(config.seed)
        self._build_ansatz()
    
    def _build_ansatz(self):
        """Build the variational ansatz based on configuration."""
        ansatz_map = {
            "EfficientSU2": lambda: EfficientSU2(
                self.num_qubits,
                reps=self.config.repetitions,
                entanglement=self.config.entanglement,
            ),
            "RealAmplitudes": lambda: RealAmplitudes(
                self.num_qubits,
                repetitions=self.config.repetitions,
                entanglement=self.config.entanglement,
            ),
            "TwoLocal": lambda: TwoLocal(
                self.num_qubits,
                rotation_blocks=self.config.rotation_blocks,
                entanglement_blocks="cx",
                entanglement=self.config.entanglement,
                repetitions=self.config.repetitions,
            ),
            "ZZFeatureMap": lambda: ZZFeatureMap(
                self.num_qubits,
                reps=self.config.repetitions,
                entanglement=self.config.entanglement,
            ),
        }
        
        builder = ansatz_map.get(self.config.ansatz_type, ansatz_map["EfficientSU2"])
        self.ansatz = builder()
        self.num_params = self.ansatz.num_parameters
    
    def get_circuit(self, params: Optional[np.ndarray] = None) -> QuantumCircuit:
        """Get parametrized quantum circuit with specified parameters."""
        if params is None:
            params = np.random.uniform(0, 2*np.pi, self.num_params)
        
        qc = QuantumCircuit(self.num_qubits)
        
        # Initial superposition
        qc.h(range(self.num_qubits))
        
        # Apply variational ansatz
        parameterized_ansatz = self.ansatz.assign_parameters(params)
        qc.compose(parameterized_ansatz, inplace=True)
        
        return qc
    
    def get_expectation_operator(self, observable: str = "Z") -> list[SparsePauliOp]:
        """Get measurement operators for expectation values."""
        obs = []
        for i in range(self.num_qubits):
            pauli = "I" * i + observable + "I" * (self.num_qubits - i - 1)
            obs.append(SparsePauliOp.from_list([(pauli, 1.0)]))
        return obs
    
    def forward(self, params: np.ndarray, embedding_circuit: Optional[QuantumCircuit] = None) -> np.ndarray:
        """
        Execute quantum circuit and return measurement probabilities.
        
        Args:
            params: Variational parameters
            embedding_circuit: Data embedding circuit
            
        Returns:
            Measurement probabilities
        """
        # Create fresh circuit
        qc = QuantumCircuit(self.num_qubits)
        
        # Initial state
        from qiskit.quantum_info import Statevector
        sv = Statevector.from_int(0, 2**self.num_qubits)
        
        # Apply embedding if provided
        if embedding_circuit is not None:
            qc.compose(embedding_circuit, inplace=True)
        
        # Apply variational ansatz
        var_circuit = self.get_circuit(params)
        qc.compose(var_circuit, inplace=True)
        
        # Evolve the statevector
        sv = sv.evolve(qc)
        probs = np.abs(sv.probabilities())**2
        
        return probs
    
    def __repr__(self) -> str:
        return f"QuantumCircuitLayer(num_qubits={self.num_qubits}, num_params={self.num_params}, ansatz={self.config.ansatz_type})"