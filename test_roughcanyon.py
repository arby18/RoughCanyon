# test_roughcanyon.py
"""
Tests for RoughCanyon module.
"""

import unittest
from roughcanyon import RoughCanyon

class TestRoughCanyon(unittest.TestCase):
    """Test cases for RoughCanyon class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = RoughCanyon()
        self.assertIsInstance(instance, RoughCanyon)
        
    def test_run_method(self):
        """Test the run method."""
        instance = RoughCanyon()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
