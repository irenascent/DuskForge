# test_duskforge.py
"""
Tests for DuskForge module.
"""

import unittest
from duskforge import DuskForge

class TestDuskForge(unittest.TestCase):
    """Test cases for DuskForge class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = DuskForge()
        self.assertIsInstance(instance, DuskForge)
        
    def test_run_method(self):
        """Test the run method."""
        instance = DuskForge()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
