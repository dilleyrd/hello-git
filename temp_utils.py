"""
Pure conversion functions so they are easy to test.
"""

def c_to_f(celsius: float) -> float:
    """Convert Celsius to Fahrenheit."""
    return celsius * 9.0 / 5.0 + 32.0

def f_to_c(fahrenheit: float) -> float:
    """Convert Fahrenheit to Celsius."""
    return (fahrenheit - 32.0) * 5.0 / 9.0

def c_to_k(celsius: float) -> float:
    """Convert Celsius to Kelvin."""
    return celsius + 273.15

def k_to_c(kelvin: float) -> float:
    """Convert Kelvin to Celsius."""
    return kelvin - 273.15