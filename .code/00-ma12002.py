"""Jupyter setup for MA12002"""

# Add code directory to path to pick up model solutions
import sys
import os

sys.path.insert(0, os.path.expanduser("~") + "/ma12002/.code/")

# Make pytest and ipytest available
import pytest
import ipytest

def run_tests_pytest():
    """Run pytest on all tests in the current notebook"""
    pytest.main(
        args=[
            "-v",
            "--tb=short",
            "--color=yes",
            "--timeout=5",
            "-W ignore::DeprecationWarning",
        ]
    )

def run_tests():
    """Run ipytest on all tests in the current notebook"""
    ipytest.run(
        "-v", module=__import__("__main__")
    )
