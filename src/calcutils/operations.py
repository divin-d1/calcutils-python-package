"""Core arithmetic and statistical helper functions for calcutils."""

from typing import Iterable


def add(a: float, b: float) -> float:
    """Return the sum of two numbers."""
    return a + b


def multiply(a: float, b: float) -> float:
    """Return the product of two numbers."""
    return a * b


def average(numbers: Iterable[float]) -> float:
    """Return the arithmetic mean, or ``0.0`` if *numbers* is empty."""
    total = 0.0
    count = 0

    for number in numbers:
        total += number
        count += 1

    if count == 0:
        return 0.0
    return total / count
