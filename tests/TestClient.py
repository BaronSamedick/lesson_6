import unittest
from rpc_client import FibonacciRpcClient


class TestClient(unittest.TestCase):
    def setUp(self):
        self.fibonacci_rpc = FibonacciRpcClient()

    def test_call(self):
        self.assertEqual(self.fibonacci_rpc.call(0), 0)
        self.assertEqual(self.fibonacci_rpc.call(1), 1)
        self.assertEqual(self.fibonacci_rpc.call(10), 55)
        self.assertEqual(self.fibonacci_rpc.call(30), 832040)


if __name__ == '__main__':
    unittest.main()
