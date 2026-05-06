"""
Utils Module
==========
Logging and utility functions.
"""

import sys
from loguru import logger
from functools import wraps
from time import perf_counter
from typing import Callable, Any


def setup_logging(level: str = "INFO", format: str = None):
    """
    Setup loguru logging.
    
    Args:
        level: Log level (TRACE, DEBUG, INFO, WARNING, ERROR)
        format: Custom log format
    """
    if format is None:
        format = (
            "<green>{time:YYYY-MM-DD HH:mm:ss}</green> | "
            "<level>{level: <8}</level> | "
            "<cyan>{name}</cyan>:<cyan>{function}</cyan>:<cyan>{line}</cyan> | "
            "<level>{message}</level>"
        )
    
    logger.remove()
    logger.add(sys.stderr, level=level, format=format)


def log_execution(func: Callable) -> Callable:
    """Decorator to log function execution time."""
    @wraps(func)
    def wrapper(*args, **kwargs) -> Any:
        start = perf_counter()
        result = func(*args, **kwargs)
        elapsed = perf_counter() - start
        logger.info(f"{func.__name__} executed in {elapsed:.4f}s")
        return result
    return wrapper


def handle_errors(func: Callable) -> Callable:
    """Decorator to handle and log errors."""
    @wraps(func)
    def wrapper(*args, **kwargs) -> Any:
        try:
            return func(*args, **kwargs)
        except Exception as e:
            logger.error(f"Error in {func.__name__}: {e}")
            raise
    return wrapper


# Initialize logging
setup_logging()

__all__ = ["logger", "setup_logging", "log_execution", "handle_errors"]