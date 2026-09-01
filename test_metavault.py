# test_metavault.py
"""
Tests for MetaVault module.
"""

import unittest
from metavault import MetaVault

class TestMetaVault(unittest.TestCase):
    """Test cases for MetaVault class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = MetaVault()
        self.assertIsInstance(instance, MetaVault)
        
    def test_run_method(self):
        """Test the run method."""
        instance = MetaVault()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
