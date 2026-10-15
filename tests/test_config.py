from __future__ import annotations

import unittest

from phoenix_config import validate_environment


class ValidateEnvironmentTests(unittest.TestCase):
    def test_normalizes_allowed_environment(self) -> None:
        self.assertEqual(validate_environment(" Staging "), "staging")

    def test_rejects_empty_environment(self) -> None:
        with self.assertRaisesRegex(
            ValueError,
            "Deployment environment is required",
        ):
            validate_environment("  ")

    def test_rejects_unsupported_environment(self) -> None:
        with self.assertRaises(ValueError) as error:
            validate_environment("qa")

        for environment in ("development", "staging", "production"):
            with self.subTest(environment=environment):
                self.assertIn(environment, str(error.exception))


if __name__ == "__main__":
    unittest.main()
