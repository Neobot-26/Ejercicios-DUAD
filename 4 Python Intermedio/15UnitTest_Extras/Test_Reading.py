import unittest
from unittest.mock import mock_open,patch

from Reading import read_lines

class TestReadLines(unittest.TestCase):

    def test_read_lines_success(self):
        fake_content_of_file = "Data Line 1\nData Line 2\nData Line 3\n"

        with patch("builtins.open", mock_open(read_data=fake_content_of_file)):
            result = read_lines("text_file.txt")

        self.assertEqual(
            result,
            ["Data Line 1\n", "Data Line 2\n", "Data Line 3\n"]
        )

    def test_file_not_found(self):
        with patch(
            "builtins.open",
            side_effect=FileNotFoundError
        ):
            with self.assertRaises(FileNotFoundError):
                read_lines("file_not_found.txt")


if __name__ == "__main__":
    unittest.main()