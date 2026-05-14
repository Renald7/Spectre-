#!/usr/bin/env python3
"""
╔══════════════════════════════════════════════════════════════════════════════╗
║                                                                      ║
║       🚀 AI ENGINEER MASTERCLASS - COMPLETE COURSEWARE                  ║
║       From Zero to Top 10 University Level - 2026                    ║
║                                                                      ║
╚══════════════════════════════════════════════════════════════════════╝

WELCOME TO YOUR AI ENGINEER JOURNEY!

This course will take you from zero to hero in AI/ML/Quantum Computing.
Follow each step carefully. Run each cell. Build your skills systematically.

╔══════════════════════════════════════════════════════════════════════════════╗
║                           COURSE ROADMAP                               ║
╚══════════════════════════════════════════════════════════════════════════════╝

Week     Topic                           Level
─────────────────────────────────────────────────────────────────────────────
  1      Python Fundamentals           ⭐☆☆☆☆☆☆☆☆☆
  2      Mathematics for AI            ⭐⭐☆☆☆☆☆☆☆☆
  3      Machine Learning Basics       ⭐⭐⭐☆☆☆☆☆☆☆
  4      Deep Learning & TensorFlow   ⭐⭐⭐⭐☆☆☆☆☆☆
  5      Quantum Computing Basics      ⭐⭐⭐⭐⭐☆☆☆☆
  6      Quantum Machine Learning     ⭐⭐⭐⭐⭐⭐☆☆☆
  7      Hybrid Quantum-Classical   ⭐⭐⭐⭐⭐⭐⭐☆☆
  8      Capstone Projects          ⭐⭐⭐⭐⭐⭐⭐⭐☆

══════════════════════════════════════════════════════════════════════════════
══════════════════════════════════════════════════════════════════════════════

"""


# ═══════════════════════════════════════════════════════════════════════════════
# WEEK 1: PYTHON FUNDAMENTALS
# ═══════════════════════════════════════════════════════════════════════════════

print("""
╔══════════════════════════════════════════════════════════════════════════════╗
║                     WEEK 1: PYTHON FUNDAMENTALS                        ║
╚══════════════════════════════════════════════════════════════════════════════╝

In this week, you'll master:
• Variables and Data Types
• Operations and Expressions  
• Control Flow (if/else, loops)
• Functions and Modules
• Object-Oriented Programming (Classes)
• File I/O and Error Handling

Let's begin! 🚀
""")

# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
# SECTION 1.1: VARIABLES AND DATA TYPES
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

print("""
┌──────────────────────────────────────────────────────────────────────────────┐
│ SECTION 1.1: VARIABLES AND DATA TYPES                   │
└──────────────────────────────────────────────────────────────────────────────┘

Python has several built-in data types:

1. int    - Integer numbers (1, 42, 1000)
2. float  - Decimal numbers (3.14, 2.71, 0.001)
3. str    - Text strings ("Hello", "AI Engineer")
4. bool   - Boolean (True, False)
5. list   - Ordered collections ([1, 2, 3])
6. dict   - Key-value pairs ({"key": "value"})
7. tuple  - Immutable sequences ((1, 2, 3))
8. set    - Unique collections {1, 2, 3}

Let's practice!
""")

# PRACTICE CELL: Run this to learn about variables
age = 25  # Integer
price = 19.99  # Float
name = "AI Engineer"  # String
is_student = True  # Boolean
skills = ["Python", "TensorFlow", "Qiskit"]  # List
profile = {"name": name, "age": age, "skills": skills}  # Dictionary

print(f"Integer (age): {age} → type: {type(age).__name__}")
print(f"Float (price): {price} → type: {type(price).__name__}")
print(f"String (name): {name} → type: {type(name).__name__}")
print(f"Boolean (is_student): {is_student} → type: {type(is_student).__name__}")
print(f"List (skills): {skills}")
print(f"Dictionary (profile): {profile}")

print("\n✅ Variables and data types - COMPLETED")

# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
# SECTION 1.2: OPERATIONS
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

print("""
┌──────────────────────────────────────────────────────────────────────────────┐
│ SECTION 1.2: OPERATIONS AND EXPRESSIONS                       │
└──────────────────────────────────────────────────────────────────────────────┘

Python supports various operations:
""")

# Arithmetic
a, b = 10, 3
print(f"Arithmetic (a={a}, b={b}):")
print(f"  a + b = {a + b}   (addition)")
print(f"  a - b = {a - b}   (subtraction)")
print(f"  a * b = {a * b}   (multiplication)")
print(f"  a / b = {a / b:.2f}   (division)")
print(f"  a ** b = {a ** b}  (power)")
print(f"  a % b = {a % b}   (modulus)")

# Comparison
x, y = 5, 10
print(f"\nComparison (x={x}, y={y}):")
print(f"  x == y: {x == y}  (equal)")
print(f"  x != y: {x != y}  (not equal)")
print(f"  x < y:  {x < y}   (less than)")
print(f"  x > y:  {x > y}   (greater than)")
print(f"  x <= y: {x <= y}  (less or equal)")
print(f"  x >= y: {x >= y}  (greater or equal)")

# Logical
print(f"\nLogical (x={x}, y={y}):")
print(f"  x > 0 and y > 0: {x > 0 and y > 0}")
print(f"  x > 0 or y > 0: {x > 0 or y > 0}")
print(f"  not (x > y): {not (x > y)}")

print("\n✅ Operations - COMPLETED")

# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
# SECTION 1.3: FUNCTIONS
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

print("""
┌──────────────────────────────────────────────────────────────────────────────┐
│ SECTION 1.3: FUNCTIONS                                    │
└──────────────────────────────────────────────────────────────────────────────┘

Functions are reusable blocks of code. Let's create some!
""")

# Basic function
def greet(name):
    """A simple greeting function"""
    return f"Hello, {name}! Welcome to AI Engineer Masterclass!"

print(greet("Future AI Engineer"))

# Function with multiple parameters
def calculate_ml_accuracy(predictions, actual):
    """
    Calculate classification accuracy.
    
    Args:
        predictions: Model predictions (list or array)
        actual: Actual labels (list or array)
    
    Returns:
        accuracy: Classification accuracy (float)
    """
    correct = sum(p == a for p, a in zip(predictions, actual))
    accuracy = correct / len(predictions)
    return accuracy

# Test the function
y_pred = [1, 0, 1, 1, 0, 1, 0, 0, 1, 1]
y_true = [1, 0, 0, 1, 0, 1, 1, 0, 1, 1]
accuracy = calculate_ml_accuracy(y_pred, y_true)
print(f"\nAccuracy calculation:")
print(f"  Predictions: {y_pred}")
print(f"  Actual:      {y_true}")
print(f"  Accuracy:   {accuracy:.0%}")

# Function with default parameters
def train_model(data, epochs=10, learning_rate=0.001):
    """Simulate model training"""
    print(f"Training on {len(data)} samples...")
    print(f"  Epochs: {epochs}")
    print(f"  Learning rate: {learning_rate}")
    return "Model trained successfully!"

result = train_model([1, 2, 3, 4, 5], epochs=5, learning_rate=0.01)
print(f"\n{result}")

print("\n✅ Functions - COMPLETED")

# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
# SECTION 1.4: CLASSES (OBJECT-ORIENTED PROGRAMMING)
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

print("""
┌──────────────────────────────────────────────────────────────────────────────┐
│ SECTION 1.4: CLASSES (OOP)                                │
└──────────────────────────────────────────────────────────────────────────────┘

Classes bundle data and functions together. Here's a Neural Network class!
""")

class NeuralNetwork:
    """
    A simple neural network classifier.
    
    Attributes:
        input_dim: Number of input features
        output_dim: Number of output classes
        weights: Model parameters
    """
    
    def __init__(self, input_dim, output_dim):
        """
        Initialize the neural network.
        
        Args:
            input_dim: Number of input features
            output_dim: Number of output classes
        """
        self.input_dim = input_dim
        self.output_dim = output_dim
        self.weights = None
        self.bias = None
        print(f"🧠 Neural Network created!")
        print(f"   - Input dimension: {input_dim}")
        print(f"   - Output dimension: {output_dim}")
    
    def forward(self, X):
        """
        Forward pass through the network.
        
        Args:
            X: Input data (numpy array)
        
        Returns:
            predictions: Model predictions
        """
        return f"Processing {X.shape[0]} samples..."
    
    def train(self, X, y, epochs=10):
        """
        Train the neural network.
        
        Args:
            X: Training data
            y: Training labels
            epochs: Number of training epochs
        """
        print(f"🏋️ Training for {epochs} epochs...")
        self.weights = "trained_weights"
        return "Training complete!"
    
    def predict(self, X):
        """
        Make predictions.
        
        Args:
            X: Input data
        
        Returns:
            predictions: Model predictions
        """
        return [0, 1, 0, 1]  # Example predictions

# Create an instance of the class
model = NeuralNetwork(input_dim=784, output_dim=10)

# Call methods
import numpy as np
X_train = np.random.randn(100, 784)
y_train = np.random.randint(0, 10, 100)

model.train(X_train, y_train, epochs=5)
predictions = model.forward(X_train[:10])
print(f"\n📊 {predictions}")
print(f"   Sample predictions: {model.predict(X_train[:5])}")

print("\n✅ Classes (OOP) - COMPLETED")

# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
# WEEK 1 COMPLETE!
print("""
╔══════════════════════════════════════════════════════════════════════════════╗
║                   ✅ WEEK 1 COMPLETE!                                     ║
╚══════════════════════════════════════════════════════════════════════════════╝

What you learned:
• Variables and all data types (int, float, str, bool, list, dict, tuple, set)
• Arithmetic, comparison, and logical operations
• Writing and calling functions
• Object-oriented programming with classes

Next: WEEK 2 - Mathematics for AI

══════════════════════════════════════════════════════════════════════════════
══════════════════════════════════════════════════════════════════════════════════════
""")

input("Press ENTER to continue to Week 2...")


# ═══════════════════════════════════════════════════════════════════════════════
# WEEK 2: MATHEMATICS FOR AI
# ═══════════════════════════════════════════════════════════════════════════════

print("""
╔══════════════════════════════════════════════════════════════════════════════╗
║                     WEEK 2: MATHEMATICS FOR AI                             ║
╚══════════════════════════════════════════════════════════════════════════════╝

Mathematics is the foundation of all machine learning.
You'll master:
• Linear Algebra (vectors, matrices, operations)
• Calculus (derivatives, gradients)
• Probability & Statistics
• Optimization

Let's begin! 🚀
""")

# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
# SECTION 2.1: LINEAR ALGEBRA
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

print("""
┌──────────────────────────────────────────────────────────────────────────────┐
│ SECTION 2.1: LINEAR ALGEBRA                              │
└──────────────────────────────────────────────────────────────────────────────┘

Linear algebra is the math of vectors and matrices - essential for ML!
""")

import numpy as np

# VECTORS
vector = np.array([1, 2, 3, 4, 5])
print(f"📐 Vector: {vector}")
print(f"   Shape: {vector.shape}")
print(f"   L2 Norm: {np.linalg.norm(vector):.4f}")
print(f"   Sum: {np.sum(vector)}")
print(f"   Mean: {np.mean(vector):.4f}")

# MATRICES
matrix = np.array([[1, 2, 3], 
                  [4, 5, 6], 
                  [7, 8, 9]])
print(f"\n📐 Matrix:\n{matrix}")
print(f"   Shape: {matrix.shape}")
print(f"   Transpose:\n{matrix.T}")
print(f"   Determinant: {np.linalg.det(matrix[:2,:2]):.4f}")

# MATRIX OPERATIONS
A = np.array([[1, 2], [3, 4]])
B = np.array([[5, 6], [7, 8]])

print(f"\nMatrix A:\n{A}")
print(f"Matrix B:\n{B}")
print(f"A + B:\n{A + B}")
print(f"A - B:\n{A - B}")
print(f"A @ B (dot product):\n{A @ B}")
print(f"A * B (element-wise):\n{A * B}")

# Special matrices
identity = np.eye(3)
zeros = np.zeros((3, 3))
ones = np.ones((3, 3))

print(f"\nSpecial matrices:")
print(f"Identity (3x3):\n{identity}")
print(f"Zeros (3x3):\n{zeros}")
print(f"Ones (3x3):\n{ones}")

print("\n✅ Linear Algebra - COMPLETED")

# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
# SECTION 2.2: CALCULUS
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

print("""
┌──────────────────────────────────────────────────────────────────────────────┐
│ SECTION 2.2: CALCULUS                                │
└──────────────────────────────────────────────────────────────────────────────┘

Calculus helps us optimize ML models. Let's explore derivatives and gradients!
""")

# DERIVATIVES
def sigmoid(x):
    """Sigmoid activation function"""
    return 1 / (1 + np.exp(-x))

def sigmoid_derivative(x):
    """Derivative of sigmoid: σ'(x) = σ(x)(1 - σ(x))"""
    s = sigmoid(x)
    return s * (1 - s)

# Test the derivative
x = np.linspace(-5, 5, 11)
print("📐 Sigmoid and its derivative:")
print(f"x:          {x.round(2)}")
print(f"σ(x):       {sigmoid(x).round(4)}")
print(f"σ'(x):      {sigmoid_derivative(x).round(4)}")

# GRADIENT DESCENT - The optimization algorithm behind all ML!
def gradient_descent(f, initial_x, learning_rate=0.1, iterations=20):
    """
    Find the minimum of a function using gradient descent.
    
    Args:
        f: Function to minimize
        initial_x: Starting point
        learning_rate: Step size
        iterations: Number of iterations
    
    Returns:
        minimum: The x value that minimizes f
        history: All x values visited
    """
    x = initial_x
    history = [x]
    
    for i in range(iterations):
        # Numerical gradient (finite differences)
        epsilon = 1e-5
        grad = (f(x + epsilon) - f(x - epsilon)) / (2 * epsilon)
        x = x - learning_rate * grad
        history.append(x)
    
    return x, history

# Example: minimize f(x) = x^2
f = lambda x: x**2
minimum, path = gradient_descent(f, initial_x=5.0, learning_rate=0.1)

print(f"\n📐 Finding minimum of f(x) = x²:")
print(f"   Starting at x = 5.0")
print(f"   Learning rate = 0.1")
print(f"   Found minimum at x = {minimum:.6f}")
print(f"   Minimum value f(x) = {f(minimum):.6f}")
print(f"   Path: {[round(x, 2) for x in path]}")

# GRADIENT DESCENT FOR LINEAR REGRESSION
def gradient_descent_lr(X, y, learning_rate=0.01, epochs=100):
    """
    Linear regression using gradient descent.
    
    Args:
        X: Features (n_samples, n_features)
        y: Targets (n_samples,)
        learning_rate: Step size
        epochs: Number of iterations
    
    Returns:
        weights: Learned weights
        bias: Learned bias
    """
    n_samples, n_features = X.shape
    
    # Initialize
    weights = np.zeros(n_features)
    bias = 0
    
    for epoch in range(epochs):
        # Predictions
        y_pred = np.dot(X, weights) + bias
        
        # Gradients
        dw = (1/n_samples) * np.dot(X.T, (y_pred - y))
        db = (1/n_samples) * np.sum(y_pred - y)
        
        # Update
        weights -= learning_rate * dw
        bias -= learning_rate * db
    
    return weights, bias

# Generate sample data
np.random.seed(42)
X = np.random.randn(200, 3)
y = 3*X[:, 0] + 2*X[:, 1] - X[:, 2] + 5 + np.random.randn(200)*0.1

# Train
weights, bias = gradient_descent_lr(X, y, learning_rate=0.1, epochs=100)

# Evaluate
y_pred = np.dot(X, weights) + bias
mse = np.mean((y - y_pred)**2)

print(f"\n📐 Linear Regression with Gradient Descent:")
print(f"   True weights: [3, 2, -1]")
print(f"   Learned weights: {weights.round(4)}")
print(f"   True bias: 5")
print(f"   Learned bias: {bias:.4f}")
print(f"   MSE: {mse:.4f}")

print("\n✅ Calculus - COMPLETED")

# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
# SECTION 2.3: PROBABILITY AND STATISTICS
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

print("""
┌──────────────────────────────────────────────────────────────────────────────┐
│ SECTION 2.3: PROBABILITY AND STATISTICS                 │
└──────────────────────────────────────────────────────────────────────────────┘

Probability and statistics are crucial for understanding data and model uncertainty!
""")

# Generate sample data
np.random.seed(42)
data = np.random.randn(1000)  # Standard normal distribution

# Basic statistics
print("📊 Basic Statistics:")
print(f"   Mean: {np.mean(data):.4f}")
print(f"   Median: {np.median(data):.4f}")
print(f"   Std Dev: {np.std(data):.4f}")
print(f"   Variance: {np.var(data):.4f}")
print(f"   Min: {np.min(data):.4f}")
print(f"   Max: {np.max(data):.4f}")
print(f"   25th percentile: {np.percentile(data, 25):.4f}")
print(f"   50th percentile: {np.percentile(data, 50):.4f}")
print(f"   75th percentile: {np.percentile(data, 75):.4f}")

# PROBABILITY DISTRIBUTIONS
print("\n📊 Common Probability Distributions:")

# Uniform distribution
uniform = np.random.uniform(0, 1, 10000)
print(f"   Uniform(0,1): mean={np.mean(uniform):.4f}, std={np.std(uniform):.4f}")

# Normal/Gaussian distribution
normal = np.random.normal(0, 1, 10000)
print(f"   Normal(0,1): mean={np.mean(normal):.4f}, std={np.std(normal):.4f}")

# Binomial distribution (for classification)
binom = np.random.binomial(1, 0.7, 10000)  # 70% probability of class 1
print(f"   Binomial(1, 0.7): class 1 = {np.sum(binom)}, class 0 = {len(binom) - np.sum(binom)}")

# EXPECTED VALUE AND VARIANCE
# E[X] = mean, Var[X] = E[(X - E[X])²]
print("\n📊 Expected Value and Variance:")
print(f"   E[X] = mean = {np.mean(data):.4f}")
print(f"   Var[X] = E[(X - E[X])²] = {np.var(data):.4f}")

print("\n✅ Probability & Statistics - COMPLETED")

# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
# WEEK 2 COMPLETE!
print("""
╔══════════════════════════════════════════════════════════════════════════════╗
║                   ✅ WEEK 2 COMPLETE!                                     ║
╚══════════════════════════════════════════════════════════════════════════════════════╝

What you learned:
• Linear Algebra: Vectors, matrices, operations (dot product, transpose, etc.)
• Calculus: Derivatives, gradient descent, optimization
• Probability & Statistics: Distributions, mean, variance, percentiles

Next: WEEK 3 - Machine Learning Basics

══════════════════════════════════════════════════════════════════════════════
══════════════════════════════════════════════════════════════════════════════
""")

input("Press ENTER to continue to Week 3...")


# ═══════════════════════════════════════════════════════════════════════════════
# WEEK 3: MACHINE LEARNING BASICS
# ═══════════════════════════════════════════════════════════════════════════════

print("""
╔══════════════════════════════════════════════════════════════════════════════╗
║                  WEEK 3: MACHINE LEARNING BASICS                           ║
╚══════════════════════════════════════════════════════════════════════════════╝

Now we'll build actual ML models from scratch!
You'll learn:
• Linear Regression (predicting continuous values)
• Logistic Regression (binary classification)
• K-Nearest Neighbors (instance-based learning)
• Decision Trees and Random Forests
• Model Evaluation Metrics

Let's begin! 🚀
""")

# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
# SECTION 3.1: LINEAR REGRESSION FROM SCRATCH
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

print("""
┌──────────────────────────────────────────────────────────────────────────────┐
│ SECTION 3.1: LINEAR REGRESSION FROM SCRATCH            │
└──────────────────────────────────────────────────────────────────────────────┘

Linear regression finds the best linear relationship between features and target.
""")

class LinearRegression:
    """Linear Regression implemented from scratch"""
    
    def __init__(self):
        self.weights = None
        self.bias = None
    
    def fit(self, X, y, learning_rate=0.01, epochs=100):
        """
        Train using gradient descent.
        
        Args:
            X: Features (n_samples, n_features)
            y: Target values (n_samples,)
            learning_rate: Step size
            epochs: Number of iterations
        """
        n_samples, n_features = X.shape
        
        # Initialize
        self.weights = np.zeros(n_features)
        self.bias = 0
        
        for epoch in range(epochs):
            # Predictions
            y_pred = np.dot(X, self.weights) + self.bias
            
            # Gradients
            dw = (1/n_samples) * np.dot(X.T, (y_pred - y))
            db = (1/n_samples) * np.sum(y_pred - y)
            
            # Update
            self.weights -= learning_rate * dw
            self.bias -= learning_rate * db
    
    def predict(self, X):
        """Make predictions"""
        return np.dot(X, self.weights) + self.bias

# Generate sample data
np.random.seed(42)
X = np.random.randn(200, 3)
y = 3*X[:, 0] + 2*X[:, 1] - X[:, 2] + 5 + np.random.randn(200)*0.1

# Train
model = LinearRegression()
model.fit(X, y, learning_rate=0.1, epochs=100)

# Evaluate
y_pred = model.predict(X)
mse = np.mean((y - y_pred)**2)
r2 = 1 - mse/np.var(y)

print(f"📐 Linear Regression Results:")
print(f"   True weights: [3, 2, -1], bias: 5")
print(f"   Learned weights: {model.weights.round(4)}")
print(f"   Learned bias: {model.bias:.4f}")
print(f"   MSE: {mse:.4f}")
print(f"   R² Score: {r2:.4f}")

print("\n✅ Linear Regression - COMPLETED")

# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
# SECTION 3.2: LOGISTIC REGRESSION FROM SCRATCH
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

print("""
┌──────────────────────────────────────────────────────────────────────────────┐
│ SECTION 3.2: LOGISTIC REGRESSION FROM SCRATCH         │
└──────────────────────────────────────────────────────────────────────────────┘

Logistic regression is used for binary classification (spam/not spam, fraud/not fraud).
""")

class LogisticRegression:
    """Binary Classification from scratch"""
    
    def __init__(self):
        self.weights = None
        self.bias = None
    
    def sigmoid(self, x):
        """Sigmoid activation"""
        return 1 / (1 + np.exp(-x))
    
    def fit(self, X, y, learning_rate=0.01, epochs=100):
        """Train the classifier"""
        n_samples, n_features = X.shape
        
        self.weights = np.zeros(n_features)
        self.bias = 0
        
        for epoch in range(epochs):
            linear = np.dot(X, self.weights) + self.bias
            y_pred = self.sigmoid(linear)
            
            # Gradients
            dw = (1/n_samples) * np.dot(X.T, (y_pred - y))
            db = (1/n_samples) * np.sum(y_pred - y)
            
            # Update
            self.weights -= learning_rate * dw
            self.bias -= learning_rate * db
    
    def predict_proba(self, X):
        """Predict probabilities"""
        linear = np.dot(X, self.weights) + self.bias
        return self.sigmoid(linear)
    
    def predict(self, X, threshold=0.5):
        """Predict classes"""
        return (self.predict_proba(X) >= threshold).astype(int)

# Generate binary classification data
np.random.seed(42)
X = np.random.randn(200, 2)
y = (X[:, 0] + X[:, 1] > 0).astype(int)

# Train
clf = LogisticRegression()
clf.fit(X, y, learning_rate=0.1, epochs=100)

# Evaluate
y_pred = clf.predict(X)
accuracy = np.mean(y_pred == y)

# Confusion matrix
tp = np.sum((y_pred == 1) & (y == 1))
tn = np.sum((y_pred == 0) & (y == 0))
fp = np.sum((y_pred == 1) & (y == 0))
fn = np.sum((y_pred == 0) & (y == 1))

precision = tp / (tp + fp) if (tp + fp) > 0 else 0
recall = tp / (tp + fn) if (tp + fn) > 0 else 0
f1 = 2 * precision * recall / (precision + recall) if (precision + recall) > 0 else 0

print(f"📐 Logistic Regression Results:")
print(f"   Accuracy: {accuracy:.2%}")
print(f"   Precision: {precision:.2%}")
print(f"   Recall: {recall:.2%}")
print(f"   F1 Score: {f1:.2%}")
print(f"\n   Confusion Matrix:")
print(f"   TP: {tp}, TN: {tn}")
print(f"   FP: {fp}, FN: {fn}")

print("\n✅ Logistic Regression - COMPLETED")

# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
# SECTION 3.3: K-NEAREST NEIGHBORS (KNN)
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

print("""
┌──────────────────────────────────────────────────────────────────────────────┐
│ SECTION 3.3: K-NEAREST NEIGHBORS (KNN)               │
└──────────────────────────────────────────────────────────────────────────────┘

KNN is a simple but effective algorithm - it classifies based on similar neighbors.
""")

from collections import Counter

class KNN:
    """K-Nearest Neighbors Classifier"""
    
    def __init__(self, k=3):
        self.k = k
        self.X_train = None
        self.y_train = None
    
    def fit(self, X, y):
        """Store training data"""
        self.X_train = X
        self.y_train = y
    
    def predict(self, X):
        """Predict classes"""
        predictions = []
        for x in X:
            # Calculate distances to all training points
            distances = np.sqrt(np.sum((self.X_train - x)**2, axis=1))
            
            # Get k nearest neighbors
            k_indices = np.argsort(distances)[:self.k]
            k_labels = self.y_train[k_indices]
            
            # Majority vote
            vote = Counter(k_labels).most_common(1)[0][0]
            predictions.append(vote)
        
        return np.array(predictions)

# Test KNN
np.random.seed(42)
X = np.random.randn(100, 2)
y = np.array([0]*50 + [1]*50)

# Create separation
X[y == 1] += 2

# Train and test
knn = KNN(k=5)
knn.fit(X, y)
predictions = knn.predict(X)
accuracy = np.mean(predictions == y)

print(f"📐 KNN Results (k=5):")
print(f"   Accuracy: {accuracy:.2%}")

print("\n✅ KNN - COMPLETED")

# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
# WEEK 3 COMPLETE!
print("""
╔══════════════════════════════════════════════════════════════════════════════╗
║                   ✅ WEEK 3 COMPLETE!                                     ║
╚══════════════════════════════════════════════════════════════════════════════╝

What you learned:
• Linear Regression: Predict continuous values from features
• Logistic Regression: Binary classification with probabilities
• KNN: Instance-based learning with majority voting
• Model evaluation: Accuracy, precision, recall, F1, confusion matrix

Next: WEEK 4 - Deep Learning with TensorFlow

══════════════════════════════════════════════════════════════════════════════
══════════════════════════════════════════════════════════════════════════════
""")

input("Press ENTER to continue to Week 4...")


# ═══════════════════════════════════════════════════════════════════════════════
# WEEK 4: DEEP LEARNING WITH TENSORFLOW
# ═══════════════════════════════════════════════════════════════════════════════

print("""
╔══════════════════════════════════════════════════════════════════════════════╗
║               WEEK 4: DEEP LEARNING WITH TENSORFLOW                       ║
╚══════════════════════════════════════════════════════════════════════════╝

Now we're going DEEP with neural networks!
You'll learn:
• TensorFlow/Keras basics
• Building feedforward neural networks
• Convolutional Neural Networks (CNNs) for images
• Recurrent Neural Networks (RNNs/LSTMs) for sequences
• Training and evaluation

Let's begin! 🚀
""")

import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3'

import tensorflow as tf
from tensorflow import keras
from keras import layers, Model
import numpy as np

print(f"TensorFlow version: {tf.__version__}")

# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
# SECTION 4.1: YOUR FIRST NEURAL NETWORK
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

print("""
┌──────────────────────────────────────────────────────────────────────────────┐
│ SECTION 4.1: FEEDFORWARD NEURAL NETWORK               │
└──────────────────────────────────────────────────────────────────────────────┘

Let's build a simple neural network for binary classification!
""")

def create_neural_network():
    """Create a feedforward neural network"""
    model = keras.Sequential([
        layers.Dense(64, activation='relu', input_shape=(8,)),  # Hidden 1
        layers.Dense(32, activation='relu'),  # Hidden 2
        layers.Dense(16, activation='relu'),   # Hidden 3
        layers.Dense(1, activation='sigmoid')  # Output
    ])
    
    model.compile(
        optimizer='adam',
        loss='binary_crossentropy',
        metrics=['accuracy']
    )
    return model

# Generate data
np.random.seed(42)
X = np.random.randn(1000, 8)
y = (X[:, 0] + X[:, 1] + X[:, 2] > 0).astype(int)

# Split
X_train, X_test = X[:800], X[800:]
y_train, y_test = y[:800], y[800:]

# Create and train
model = create_neural_network()
print("📐 Model Architecture:")
model.summary()

print("\n🏋️ Training...")
history = model.fit(
    X_train, y_train,
    epochs=10,
    batch_size=32,
    validation_data=(X_test, y_test),
    verbose=0
)

# Evaluate
loss, accuracy = model.evaluate(X_test, y_test, verbose=0)
print(f"\n📊 Results:")
print(f"   Loss: {loss:.4f}")
print(f"   Accuracy: {accuracy:.2%}")

print("\n✅ Feedforward Neural Network - COMPLETED")

# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
# SECTION 4.2: CONVOLUTIONAL NEURAL NETWORKS (CNN)
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

print("""
┌──────────────────────────────────────────────────────────────────────────────┐
│ SECTION 4.2: CNN FOR IMAGE CLASSIFICATION         │
└──────────────────────────────────────────────────────────────────────────────┘

CNNs are perfect for image classification!
""")

def create_cnn():
    """Create a CNN for image classification"""
    model = keras.Sequential([
        # Convolutional layers
        layers.Conv2D(32, (3, 3), activation='relu', input_shape=(28, 28, 1)),
        layers.MaxPooling2D((2, 2)),
        layers.Conv2D(64, (3, 3), activation='relu'),
        layers.MaxPooling2D((2, 2)),
        layers.Conv2D(64, (3, 3), activation='relu'),
        
        # Dense layers
        layers.Flatten(),
        layers.Dense(64, activation='relu'),
        layers.Dense(10, activation='softmax')  # 10 digit classes
    ])
    
    model.compile(
        optimizer='adam',
        loss='sparse_categorical_crossentropy',
        metrics=['accuracy']
    )
    return model

# Load MNIST data
(X_train, y_train), (X_test, y_test) = keras.datasets.mnist.load_data()

# Normalize
X_train = X_train.reshape(-1, 28, 28, 1).astype('float32') / 255.0
X_test = X_test.reshape(-1, 28, 28, 1).astype('float32') / 255.0

# Subset for quick training
X_train_small = X_train[:5000]
y_train_small = y_train[:5000]

# Create and train
cnn = create_cnn()
print("📐 CNN Architecture:")
cnn.summary()

print("\n🏋️ Training CNN...")
cnn.fit(X_train_small, y_train_small, epochs=3, batch_size=64, verbose=0)
print("✅ CNN training complete!")

print("\n✅ CNN - COMPLETED")

# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
# SECTION 4.3: LSTM FOR SEQUENCES
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

print("""
┌──────────────────────────────────────────────────────────────────────────────┐
│ SECTION 4.3: LSTM FOR SEQUENCE MODELING           │
└──────────────────────────────────────────────────────────────────────────────┘

LSTMs are great for sequential data (text, time series, etc.)!
""")

def create_lstm():
    """Create an LSTM model for sequences"""
    model = keras.Sequential([
        layers.Embedding(input_dim=1000, output_dim=64, input_length=50),
        layers.LSTM(64, return_sequences=True),
        layers.LSTM(32),
        layers.Dense(1, activation='sigmoid')
    ])
    
    model.compile(
        optimizer='adam',
        loss='binary_crossentropy',
        metrics=['accuracy']
    )
    return model

# Generate sequence data
np.random.seed(42)
X_seq = np.random.randint(0, 1000, size=(1000, 50))
y_seq = np.random.randint(0, 2, size=(1000, 1))

# Test
lstm = create_lstm()
print("📐 LSTM Architecture:")
lstm.summary()

print("\n🏋️ Training LSTM...")
lstm.fit(X_seq[:800], y_seq[:800], epochs=2, batch_size=32, verbose=0)
print("✅ LSTM training complete!")

print("\n✅ LSTM - COMPLETED")

# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
# WEEK 4 COMPLETE!
print("""
╔══════════════════════════════════════════════════════════════════════════════╗
║                   ✅ WEEK 4 COMPLETE!                                     ║
╚══════════════════════════════════════════════════════════════════════════════╝

What you learned:
• TensorFlow/Keras fundamentals
• Feedforward neural networks for classification
• CNNs for image classification (digit recognition)
• LSTMs for sequence modeling

Next: WEEK 5 - Quantum Computing Basics

══════════════════════════════════════════════════════════════════════════════
══════════════════════════════════════════════════════════════════════════════
""")

input("Press ENTER to continue to Week 5 (Quantum Computing)...")


# ═══════════════════════════════════════════════════════════════════════════════
# WEEK 5: QUANTUM COMPUTING BASICS
# ═══════════════════════════════════════════════════════════════════════════════

print("""
╔══════════════════════════════════════════════════════════════════════════════╗
║                  WEEK 5: QUANTUM COMPUTING BASICS                          ║
╚══════════════════════════════════════════════════════════════════════════════╝

Welcome to the QUANTUM world!
You'll learn:
• Quantum bits (qubits) and quantum circuits
• Quantum gates (Hadamard, CNOT, rotations)
• Superposition and entanglement
• Quantum measurement
• Running quantum simulations

Let's begin! ⚛️
""")

from qiskit import QuantumCircuit
from qiskit.quantum_info import Statevector, Operator
import numpy as np

# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
# SECTION 5.1: YOUR FIRST QUANTUM CIRCUIT
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

print("""
┌──────────────────────────────────────────────────────────────────────────────┐
│ SECTION 5.1: QUANTUM CIRCUITS                         │
└──────────────────────────────────────────────────────────────────────────────┘

Let's build our first quantum circuit!
""")

# Create a quantum circuit with 2 qubits
qc = QuantumCircuit(2)

# Add quantum gates
qc.h(0)       # Hadamard - creates superposition
qc.cx(0, 1)   # CNOT - creates entanglement
qc.ry(0.5, 0) # Rotation around Y axis
qc.rz(0.3, 1) # Rotation around Z axis

print("📐 Quantum Circuit:")
print(qc.draw())

# Execute and get quantum state
sv = Statevector.from_int(0, 2**2)
sv = sv.evolve(qc)

print(f"\n📊 Quantum State:")
print(f"   Amplitudes: {sv.data.round(4)}")
print(f"   Probabilities: {sv.probabilities().round(4)}")

print("\n✅ Quantum Circuits - COMPLETED")

# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
# SECTION 5.2: QUANTUM GATES
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

print("""
┌──────────────────────────────────────────────────────────────────────────────┐
│ SECTION 5.2: QUANTUM GATES                             │
└──────────────────────────────────────────────────────────────────────────────┘

Quantum gates are the building blocks of quantum computation!
""")

gates = {
    'I': lambda qc: qc.i(0),   # Identity
    'X': lambda qc: qc.x(0),  # NOT / Pauli-X
    'Y': lambda qc: qc.y(0),  # Pauli-Y
    'Z': lambda qc: qc.z(0),  # Pauli-Z
    'H': lambda qc: qc.h(0),  # Hadamard
    'S': lambda qc: qc.s(0),  # Phase
    'T': lambda qc: qc.t(0),  # T gate
}

for gate_name, gate_func in gates.items():
    qc = QuantumCircuit(1)
    gate_func(qc)
    
    op = Operator(qc)
    print(f"\n{gate_name} Gate Matrix:")
    print(f"   {op.data.round(2)}")

print("\n✅ Quantum Gates - COMPLETED")

# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
# SECTION 5.3: QUANTUM MEASUREMENT
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

print("""
┌──────────────────────────────────────────────────────────────────────────────┐
│ SECTION 5.3: QUANTUM MEASUREMENT                    │
└──────────────────────────────────────────────────────────────────────────────┘

Measurement collapses quantum states to classical bits!
""")

# Create circuit with measurement
qc = QuantumCircuit(2, 2)  # 2 qubits, 2 classical bits
qc.h(0)         # Superposition
qc.cx(0, 1)    # Entanglement
qc.measure(0, 0)
qc.measure(1, 1)

print("📐 Circuit with Measurement:")
print(qc.draw())

# Simulate using Qiskit Aer
try:
    from qiskit_aer import AerSimulator
    simulator = AerSimulator()
    result = simulator.run(qc, shots=1000).result()
    counts = result.get_counts()
    
    print("\n📊 Measurement Results (1000 shots):")
    for state, count in counts.items():
        print(f"   |{state}⟩: {count} times ({count/10:.1f}%)")
except ImportError:
    print("\n📊 Note: Install qiskit-aer for simulation")
    print("   pip install qiskit-aer")

print("\n✅ Quantum Measurement - COMPLETED")

# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
# WEEK 5 COMPLETE!
print("""
╔══════════════════════════════════════════════════════════════════════════════╗
║                   ✅ WEEK 5 COMPLETE!                                     ║
╚══════════════════════════════════════════════════════════════════════════╝

What you learned:
• Quantum circuits with qubits and gates
• Quantum gates (I, X, Y, Z, H, S, T) and their matrices
• Superposition and entanglement
• Quantum measurement and probability

Next: WEEK 6 - Quantum Machine Learning

══════════════════════════════════════════════════════════════════════════════
══════════════════════════════════════════════════════════════════════════════
""")

input("Press ENTER to continue to Week 6 (Quantum ML)...")


# ═══════════════════════════════════════════════════════════════════════════════
# WEEK 6: QUANTUM MACHINE LEARNING
# ═══════════════════════════════════════════════════════════════════════════════

print("""
╔══════════════════════════════════════════════════════════════════════════════╗
║               WEEK 6: QUANTUM MACHINE LEARNING                         ║
╚══════════════════════════════════════════════════════════════════════════════╝

Now we combine quantum computing with machine learning!
You'll learn:
• Quantum data embedding (Angle, Amplitude, IQP encoding)
• Variational quantum circuits (VQC)
• Quantum kernels
• Hybrid quantum-classical models

Let's begin! ⚛️🧠
""")

from qiskit import QuantumCircuit
from qiskit.circuit.library import EfficientSU2, ZZFeatureMap
from qiskit.quantum_info import Statevector
import numpy as np

# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
# SECTION 6.1: QUANTUM EMBEDDING
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

print("""
┌──────────────────────────────────────────────────────────────────────────────┐
│ SECTION 6.1: QUANTUM DATA EMBEDDING                   │
└──────────────────────────────────────────────────────────────────────────────┘

Embedding classical data into quantum states is crucial for quantum ML!
""")

def angle_encode(data, n_qubits=4):
    """Angle encoding - encode as rotation angles"""
    qc = QuantumCircuit(n_qubits)
    for i, val in enumerate(data[:n_qubits]):
        qc.ry(val * np.pi, i)
    return qc

# Encode sample data
data = np.array([0.5, 0.2, 0.8, 0.1])
qc = angle_encode(data)

print("📐 Angle Encoding Circuit:")
print(qc.draw())

# Get quantum state
sv = Statevector.from_int(0, 16)
sv = sv.evolve(qc)

print(f"\n📊 Quantum State Amplitudes:")
print(f"   {sv.data[:8].round(4)}")

print("\n✅ Quantum Embedding - COMPLETED")

# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
# SECTION 6.2: VARIATIONAL QUANTUM CIRCUITS
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

print("""
┌──────────────────────────────────────────────────────────────────────────────┐
│ SECTION 6.2: VARIATIONAL QUANTUM CIRCUITS            │
└──────────────────────────────────────────────────────────────────────────────┘

VQC = parameterized quantum circuits for machine learning!
""")

# Create parameterized ansatz
ansatz = EfficientSU2(num_qubits=4, reps=2, entanglement='full')
print(f"📐 Variational Ansatz: {ansatz.name}")
print(f"   Number of parameters: {ansatz.num_parameters}")

# Random parameters
params = np.random.uniform(0, 2*np.pi, ansatz.num_parameters)
param_qc = ansatz.assign_parameters(params)

# Full circuit
qc = QuantumCircuit(4)
qc.h(range(4))
qc.compose(param_qc, inplace=True)

# Get output
sv = Statevector.from_int(0, 16)
sv = sv.evolve(qc)

print(f"\n📊 Output Probabilities:")
probs = sv.probabilities()
print(f"   Top 4 states: {np.sort(probs)[-4:][::-1].round(4)}")

print("\n✅ Variational Quantum Circuits - COMPLETED")

# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
# SECTION 6.3: QUANTUM KERNELS
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

print("""
┌──────────────────────────────────────────────────────────────────────────────┐
│ SECTION 6.3: QUANTUM KERNELS                          │
└──────────────────────────────────────────────────────────────────────────────┘

Quantum kernels measure quantum state similarity!
""")

def compute_quantum_kernel(X):
    """Compute quantum kernel matrix"""
    n = len(X)
    kernel = np.zeros((n, n))
    
    fm = ZZFeatureMap(feature_dimension=len(X[0]), reps=2)
    
    for i in range(n):
        for j in range(n):
            qc_i = fm.assign_parameters(X[i])
            qc_j = fm.assign_parameters(X[j])
            
            sv_i = Statevector.from_int(0, 2**len(X[0]))
            sv_i = sv_i.evolve(qc_i)
            
            sv_j = Statevector.from_int(0, 2**len(X[0]))
            sv_j = sv_j.evolve(qc_j)
            
            overlap = np.abs(np.dot(np.conj(sv_i.data), sv_j.data))
            kernel[i, j] = overlap ** 2
    
    return kernel

# Test with small data
X_small = np.random.randn(4, 2)
kernel = compute_quantum_kernel(X_small)

print("📐 Quantum Kernel Matrix:")
print(kernel.round(4))

print("\n✅ Quantum Kernels - COMPLETED")

# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
# WEEK 6 COMPLETE!
print("""
╔══════════════════════════════════════════════════════════════════════════════╗
║                   ✅ WEEK 6 COMPLETE!                                     ║
╚══════════════════════════════════════════════════════════════════════════════╝

What you learned:
• Quantum data embedding (Angle encoding)
• Variational quantum circuits (Parameterized ansatz)
• Quantum kernel computation

Next: WEEK 7 - Hybrid Quantum-Classical ML

══════════════════════════════════════════════════════════════════════════════
══════════════════════════════════════════════════════════════════════════════
""")

input("Press ENTER to continue to Week 7 (Hybrid ML)...")


# ═══════════════════════════════════════════════════════════════════════════════
# WEEK 7: HYBRID QUANTUM-CLASSICAL ML
# ═══════════════════════════════════════════════════════════════════════════════

print("""
╔══════════════════════════════════════════════════════════════════════════════╗
║          WEEK 7: HYBRID QUANTUM-CLASSICAL ML                         ║
╚══════════════════════════════════════════════════════════════════════╝

This is the FUTURE of AI - combining quantum and classical computing!
You'll learn:
• Hybrid model architectures
• Quantum preprocessing layers
• Classical post-processing
• End-to-end training

Let's begin! ⚛️🧠
""")

import tensorflow as tf
from tensorflow import keras
from keras import layers
import numpy as np

# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
# SECTION 7.1: HYBRID MODEL ARCHITECTURE
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

print("""
┌──────────────────────────────────────────────────────────────────────────────┐
│ SECTION 7.1: HYBRID MODEL                        │
└──────────────────────────────────────────────────────────────────────────────┘

Hybrid models combine classical and quantum computing!
""")

def create_hybrid_model(input_dim=8, num_qubits=4):
    """Create a hybrid quantum-classical model"""
    inputs = keras.Input(shape=(input_dim,))
    
    # Classical preprocessing
    x = layers.Dense(32, activation='relu')(inputs)
    x = layers.Dense(16, activation='relu')(x)
    
    # Simulated quantum layer
    quantum_features = layers.Dense(2**num_qubits, activation='softmax')(x)
    
    # Classical post-processing
    x = layers.Dense(8, activation='relu')(quantum_features)
    outputs = layers.Dense(1, activation='sigmoid')(x)
    
    model = keras.Model(inputs=inputs, outputs=outputs)
    model.compile(
        optimizer='adam',
        loss='binary_crossentropy',
        metrics=['accuracy']
    )
    return model

# Create model
model = create_hybrid_model()
print("📐 Hybrid Model Architecture:")
model.summary()

# Train
np.random.seed(42)
X = np.random.randn(1000, 8)
y = (X[:, 0] + X[:, 1] > 0).astype(int)

print("\n🏋️ Training Hybrid Model...")
model.fit(X[:800], y[:800], epochs=5, verbose=0)

# Evaluate
loss, acc = model.evaluate(X[800:], y[800:], verbose=0)
print(f"\n📊 Results:")
print(f"   Loss: {loss:.4f}")
print(f"   Accuracy: {acc:.2%}")

print("\n✅ Hybrid Models - COMPLETED")

# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
# WEEK 7 COMPLETE!
print("""
╔══════════════════════════════════════════════════════════════════════════════╗
║                   ✅ WEEK 7 COMPLETE!                                     ║
╚══════════════════════════════════════════════════════════════════════════════╝

What you learned:
• Hybrid quantum-classical architectures
• End-to-end model training

Next: WEEK 8 - Capstone Projects

══════════════════════════════════════════════════════════════════════════════════════
══════════════════════════════════════════════════════════════════════════════
""")

input("Press ENTER to continue to Week 8 (Capstone Projects)...")


# ═══════════════════════════════════════════════════════════════════════════════
# WEEK 8: CAPSTONE PROJECTS
# ═══════════════════════════════════════════════════════════════════════════════

print("""
╔══════════════════════════════════════════════════════════════════════════════╗
║                   WEEK 8: CAPSTONE PROJECTS                             ║
╚══════════════════════════════════════════════════════════════════════════════╝

Time to build real-world applications!
We'll build:
1. Financial Prediction Model
2. Classification Model  
3. Anomaly Detection Model

Let's go! 🚀
""")

# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
# CAPSTONE 1: QUANTUM FINANCIAL PREDICTION
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

print("""
┌──────────────────────────────────────────────────────────────────────────────┐
│ CAPSTONE 1: QUANTUM FINANCIAL PREDICTION            │
└──────────────────────────────────────────────────────────────────────────────┘
""")

from quantum_dl.use_cases import FinancialPrediction
import numpy as np

print("💰 Building Financial Prediction Model...")

fin_model = FinancialPrediction()
X, y = fin_model.prepare_data(n_samples=1000)
print(f"📊 Data: {X.shape[0]} samples, {X.shape[1]} features")

split = int(0.8 * len(X))
X_train, y_train = X[:split], y[:split]
X_test, y_test = X[split:], y[split:]

fin_model.train(X_train, y_train, epochs=5)
predictions = fin_model.predict(X_test[:10])
results = fin_model.evaluate(predictions, y_test[:10])

print(f"\n📈 Results:")
for metric, value in results.items():
    print(f"   {metric}: {value:.4f}")

print("\n✅ Financial Prediction - COMPLETED")

# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
# CAPSTONE 2: QUANTUM CLASSIFIER
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

print("""
┌──────────────────────────────────────────────────────────────────────────────┐
│ CAPSTONE 2: QUANTUM CLASSIFIER                         │
└──────────────────────────────────────────────────────────────────────────────┘
""")

from quantum_dl.use_cases import QuantumClassifier

print("🎯 Building Quantum Classifier...")

clf = QuantumClassifier()
X, y = clf.prepare_data(n_samples=1000)
print(f"📊 Data: {X.shape[0]} samples, {X.shape[1]} features")

split = int(0.8 * len(X))
X_train, y_train = X[:split], y[:split]
X_test, y_test = X[split:], y[split:]

clf.train(X_train, y_train, epochs=5)
predictions = clf.predict(X_test[:10])
results = clf.evaluate(predictions, y_test[:10])

print(f"\n📈 Results:")
for metric, value in results.items():
    print(f"   {metric}: {value:.4f}")

print("\n✅ Quantum Classifier - COMPLETED")

# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
# CAPSTONE 3: QUANTUM ANOMALY DETECTOR
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

print("""
┌──────────────────────────────────────────────────────────────────────────────┐
│ CAPSTONE 3: QUANTUM ANOMALY DETECTOR                 │
└──────────────────────────────────────────────────────────────────────────────┘
""")

from quantum_dl.use_cases import QuantumAnomalyDetector

print("🔍 Building Anomaly Detector...")

detector = QuantumAnomalyDetector()
X, y = detector.prepare_data(n_samples=1000)
print(f"📊 Data: {X.shape[0]} samples, {X.shape[1]} features")

split = int(0.8 * len(X))
X_train, y_train = X[:split], y[:split]
X_test, y_test = X[split:], y[split:]

detector.train(X_train, y_train, epochs=5)
detector.fit_threshold(X_test)
predictions = detector.detect(X_test[:10])
results = detector.evaluate(detector.predict(X_test), y_test)

print(f"\n📈 Results:")
for metric, value in results.items():
    print(f"   {metric}: {value}")

print("\n✅ Anomaly Detector - COMPLETED")

# ═══════════════════════════════════════════════════════════════════════════════
# COURSE COMPLETE!
# ═══════════════════════════════════════════════════════════════════════════════

print("""
╔══════════════════════════════════════════════════════════════════════════════╗
║                                                                      ║
║              🎓 AI ENGINEER MASTERCLASS - COMPLETE! 🎓                   ║
║                                                                      ║
╚══════════════════════════════════════════════════════════════════════════════╝

╔══════════════════════════════════════════════════════════════════════════════╗
║                         CERTIFICATE                                  ║
╚══════════════════════════════════════════════════════════════════════════════╝

Congratulations! You have completed the AI Engineer Masterclass!

SKILLS ACQUIRED:
────────────────────────────────────────────────────────────────────────────────────────
✓ Week 1: Python Programming
✓ Week 2: Mathematics for AI  
✓ Week 3: Machine Learning
✓ Week 4: Deep Learning with TensorFlow
✓ Week 5: Quantum Computing
✓ Week 6: Quantum Machine Learning
✓ Week 7: Hybrid Quantum-Classical ML
✓ Week 8: Real-world Applications

────────────────────────────────────────────────────────────────────────────────────────

NEXT STEPS:
────────────────────────────────────────────────────────────────────────────────────────
1. Review and practice each concept
2. Explore the quantum_dl framework in /src/quantum_dl/
3. Build your own projects
4. Participate in Kaggle competitions
5. Read research papers on Quantum ML
6. Apply for internships at AI companies
7. Consider graduate studies

────────────────────────────────────────────────────────────────────────────────────────

RECOMMENDED RESOURCES:
────────────────────────────────────────────────────────────────────────────────────────
BOOKS:
• "Hands-On Machine Learning with Scikit-Learn, Keras, and TensorFlow"
• "Quantum Computation and Quantum Information" - Nielsen & Chuang
• "Deep Learning" - Goodfellow, Bengio, Courville

COURSES:
• Fast.ai Deep Learning courses
• Qiskit Textbook
• MIT OpenCourseWare

────────────────────────────────────────────────────────────────────────────────────────

YOUR PATH TO TOP 10 UNIVERSITIES:
────────────────────────────────────────────────────────────────────────────────────────
Year 1: Master Python & ML fundamentals
Year 2: Deep learning specialization
Year 3: Research experience
Year 4: Publications & internships
Year 5: Graduate applications

────────────────────────────────────────────────────────────────────────────────────────

GOOD LUCK ON YOUR AI JOURNEY! 🚀

══════════════════════════════════════════════════════════════════════════════
══════════════════════════════════════════════════════════════════════════════
""")