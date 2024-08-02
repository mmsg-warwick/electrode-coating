"""
Copyright (c) 2024 Felix Watson. All rights reserved.

electrode-coating: An electrode coating modelling project that uses the PyBaMM framework
"""
__version__ = "0.1.0"
import pybamm
from .entry_point import Model, parameter_sets, models

__all__ = [
    "__version__",
    "pybamm",
    "parameter_sets",
    "Model",
    "models",
]
