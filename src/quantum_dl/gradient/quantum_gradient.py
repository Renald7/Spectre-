"""
Quantum Gradient Computation Module
================================
Parameter-shift rule for quantum gradient computation.
"""

import numpy as np
from qiskit import QuantumCircuit
from qiskit.quantum_info import Statevector, SparsePauliOp
from typing import Callable, Optional
from dataclasses import dataclass


@dataclass
class GradientConfig:
    """Configuration for gradient computation."""
    shift: float = np.pi / 2  # Standard parameter shift
    epsilon: float = 1e-5  # Finite difference epsilon


class QuantumGradient:
    """
    Quantum gradient computation using parameter-shift rule.
    Enables differentiation of quantum circuits for backpropagation.
    """
    
    def __init__(self, config: GradientConfig):
        self.config = config
        self.shift = config.shift
        self.epsilon = config.epsilon
    
    def parameter_shift_gradient(
        self,
        circuit: QuantumCircuit,
        param_values: dict,
        observable: Optional[SparsePauliOp] = None,
    ) -> np.ndarray:
        """
        Compute gradients using parameter-shift rule.
        
        For parameterized gate U(θ) = e^(-iθP/2):
        ∇⟨O⟩ = (⟨O⟩_{θ+π/2} - ⟨O⟩_{θ-π/2}) / 2
        
        Args:
            circuit: Parameterized quantum circuit
            param_values: Dictionary of parameter values
            observable: Measurement operator
            
        Returns:
            Array of gradients for each parameter
        """
        if observable is None:
            observable = SparsePauliOp.from_list([("Z" + "I" * 15, 1.0)])
        
        params = list(param_values.keys())
        gradients = []
        
        for param in params:
            param_val = param_values[param]
            
            # Create shifted circuits
            params_plus = {param: param_val + self.shift}
            params_minus = {param: param_val - self.shift}
            
            # Execute circuits
            sv_plus = Statevector([1,0,0,0] + [0]*15).evolve(
                circuit.assign_parameters(params_plus)
            )
            sv_minus = Statevector([1,0,0,0] + [0]*15).evolve(
                circuit.assign_parameters(params_minus)
            )
            
            # Compute expectation values
            exp_plus = sv_plus.expectation_value(observable)
            exp_minus = sv_minus.expectation_value(observable)
            
            # Parameter-shift gradient
            gradient = (exp_plus - exp_minus) / 2
            gradients.append(gradient)
        
        return np.array(gradients)
    
    def compute_gradients_numeric(
        self,
        params: np.ndarray,
        loss_fn: Callable[[np.ndarray], float],
    ) -> np.ndarray:
        """
        Compute gradients numerically using finite differences.
        Backup method when parameter-shift not available.
        
        Args:
            params: Parameter array
            loss_fn: Loss function to differentiate
            
        Returns:
            Array of gradients
        """
        gradients = []
        
        for i in range(len(params)):
            params_plus = params.copy()
            params_plus[i] += self.epsilon
            
            params_minus = params.copy()
            params_minus[i] -= self.epsilon
            
            loss_plus = loss_fn(params_plus)
            loss_minus = loss_fn(params_minus)
            
            gradient = (loss_plus - loss_minus) / (2 * self.epsilon)
            gradients.append(gradient)
        
        return np.array(gradients)
    
    def compute_gradients_autograd(
        self,
        params: np.ndarray,
        forward_fn: Callable[[np.ndarray], np.ndarray],
    ) -> np.ndarray:
        """
        Compute gradients using autograd (automatic differentiation).
        
        Uses numpy's autograd for gradient computation.
        
        Args:
            params: Parameter array
            forward_fn: Forward pass function
            
        Returns:
            Array of gradients
        """
        try:
            from autograd import grad
            grad_fn = grad(forward_fn)
            return grad_fn(params)
        except ImportError:
            # Fallback to numeric gradients
            return self.compute_gradients_numeric(params, forward_fn)
    
    def __repr__(self) -> str:
        return f"QuantumGradient(shift={self.shift:.4f})"