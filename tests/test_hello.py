import subprocess
import sys
import unittest
from pathlib import Path

from hello import greet


ROOT = Path(__file__).resolve().parents[1]


class HelloTest(unittest.TestCase):
    def test_named_greeting(self):
        self.assertEqual(greet("Torii"), "Hello, Torii!")

    def test_default_cli(self):
        result = subprocess.run([sys.executable, str(ROOT / "hello.py")], check=True, capture_output=True, text=True)
        self.assertEqual(result.stdout, "Hello, world!\n")

    def test_named_cli(self):
        result = subprocess.run([sys.executable, str(ROOT / "hello.py"), "Torii"], check=True,
                                capture_output=True, text=True)
        self.assertEqual(result.stdout, "Hello, Torii!\n")
