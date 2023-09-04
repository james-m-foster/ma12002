"""Jupyter setup for MA12002"""
import pytest

def run_tests():
    """Run pytest on all tests in the current notebook"""
    pytest.main(args=["-v","--tb=short","--color=yes","--timeout=5","-W ignore::DeprecationWarning"])