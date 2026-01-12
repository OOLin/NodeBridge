# test_nodebridge.py
"""
Tests for NodeBridge module.
"""

import unittest
from nodebridge import NodeBridge

class TestNodeBridge(unittest.TestCase):
    """Test cases for NodeBridge class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = NodeBridge()
        self.assertIsInstance(instance, NodeBridge)
        
    def test_run_method(self):
        """Test the run method."""
        instance = NodeBridge()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
