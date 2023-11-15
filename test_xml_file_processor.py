import unittest
import os
from xml_file_processor import FileProcessor

# Test XML file path
test_data_filename = "test_data.xml"

class TestFileProcessor(unittest.TestCase):
    def setUp(self):
        # Create a test XML file with sample data
        with open(test_data_filename, "w") as file:
            file.write('<data>\n  <record>Record 1</record>\n  <record>Record 2</record>\n</data>')

    def tearDown(self):
        # Remove the test XML file after testing
        os.remove(test_data_filename)

    def test_read_file(self):
        processor = FileProcessor()
        root = processor.read_file(test_data_filename)
        self.assertIsNotNone(root)
        self.assertEqual(len(root.findall("record")), 2)

    def test_add_record(self):
        processor = FileProcessor()
        processor.add_record(test_data_filename, "New Record")
        root = processor.read_file(test_data_filename)
        self.assertIsNotNone(root)
        records = root.findall("record")
        self.assertEqual(len(records), 3)
        self.assertEqual(records[2].text, "New Record")

    def test_delete_record(self):
        processor = FileProcessor()
        processor.delete_record(test_data_filename, "Record 1")
        root = processor.read_file(test_data_filename)
        self.assertIsNotNone(root)
        records = root.findall("record")
        self.assertEqual(len(records), 1)
        self.assertEqual(records[0].text, "Record 2")

    def test_update_record(self):
        processor = FileProcessor()
        processor.update_record(test_data_filename, "Record 2", "Updated Record")
        root = processor.read_file(test_data_filename)
        self.assertIsNotNone(root)
        records = root.findall("record")
        self.assertEqual(len(records), 2)
        self.assertEqual(records[1].text, "Updated Record")

    def test_display_records(self):
        processor = FileProcessor()
        with unittest.mock.patch("builtins.print") as mock_print:
            processor.display_records(test_data_filename)
            mock_print.assert_called_with("Records in 'test_data.xml':\n1. Record 1\n2. Record 2")

if __name__ == "__main__":
    unittest.main()
