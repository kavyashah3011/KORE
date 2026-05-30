import unittest
from core.intent_parser import IntentParser
from utils.logger import setup_logging


class TestIntentParser(unittest.TestCase):
    def setUp(self):
        self.logger = setup_logging()
        self.parser = IntentParser(self.logger)

    def test_valid_open_app(self):
        payload = {"action": "open_app", "app": "notepad"}
        out = self.parser.parse(payload)
        self.assertIsNotNone(out)
        self.assertEqual(out.get("action"), "open_app")


if __name__ == "__main__":
    unittest.main()
