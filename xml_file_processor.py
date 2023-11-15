import xml.etree.ElementTree as ET

class FileProcessor:
    def __init__(self) -> None:
        self.tree = None
        self.root = None
    def read_file(self, filename):
        try:
            self.tree = ET.parse(filename)
            self.root = self.tree.getroot()
            return self.tree
        except FileNotFoundError:
            print(f"File '{filename}' not found.")
        except ET.ParseError:
            print(f"Error parsing '{filename}' as an XML file.")
        return None

    def add_record(self, filename, record):
        try:
            record_element = ET.Element("record")
            record_element.text = record
            self.root.append(record_element)
            
            self.tree.write(filename)
            print(f"Record added to '{filename}': {record}")
        except FileNotFoundError:
            print(f"File '{filename}' not found.")
        except ET.ParseError:
            print(f"Error parsing '{filename}' as an XML file.")

    def delete_record(self, filename, record_id):
        try:
            for record_element in self.root.findall("record"):
                if record_element.text == record_id:
                    self.root.remove(record_element)
                    self.tree.write(filename)
                    print(f"Record deleted from '{filename}': {record_id}")
                    return
            print(f"Record '{record_id}' not found in '{filename}'")
        except FileNotFoundError:
            print(f"File '{filename}' not found.")
        except ET.ParseError:
            print(f"Error parsing '{filename}' as an XML file.")

    def update_record(self, filename, record_id, new_record):
        try:
            for record_element in self.root.findall("record"):
                if record_element.text == record_id:
                    record_element.text = new_record
                    self.tree.write(filename)
                    print(f"Record updated in '{filename}': {record_id} -> {new_record}")
                    return
            print(f"Record '{record_id}' not found in '{filename}'")
        except FileNotFoundError:
            print(f"File '{filename}' not found.")
        except ET.ParseError:
            print(f"Error parsing '{filename}' as an XML file.")

    def display_records(self, filename):
        try:
            records = [record_element.text for record_element in self.root.findall("record")]
            if records:
                print(f"Records in '{filename}':")
                for idx, record in enumerate(records, start=1):
                    print(f"{idx}. {record}")
            else:
                print(f"No records found in '{filename}'")
        except FileNotFoundError:
            print(f"File '{filename}' not found.")
        except ET.ParseError:
            print(f"Error parsing '{filename}' as an XML file.")

# Example usage:
processor = FileProcessor()
processor.read_file("data.xml")
processor.add_record("data.xml", "New Record")
processor.delete_record("data.xml", "Record to Delete")
processor.update_record("data.xml", "Record to Update", "Updated Record")
processor.display_records("data.xml")
