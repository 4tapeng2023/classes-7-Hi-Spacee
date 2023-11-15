from xml_file_processor import FileProcessor

def display_menu():
    print("XML File Processor Menu:")
    print("1. Select file")
    print("2. Add Record")
    print("3. Delete Record")
    print("4. Update Record")
    print("5. Display Records")
    print("6. Exit")

def main():
    processor = FileProcessor()
    currentFile = ""
    while True:
        display_menu()
        choice = input("Enter your choice (1-6): ")

        if choice == "1":
            currentFile = input("Enter the filename to read: ")
            processor.read_file(currentFile)
        elif choice == "2":
            record = input("Enter the new record: ")
            processor.add_record(currentFile, record)
        elif choice == "3":
            record_id = input("Enter the record to delete: ")
            processor.delete_record(currentFile, record_id)
        elif choice == "4":
            record_id = input("Enter the record to update: ")
            new_record = input("Enter the new record: ")
            processor.update_record(currentFile, record_id, new_record)
        elif choice == "5":
            processor.display_records(currentFile)
            input()
        elif choice == "6":
            print("Exiting the program.")
            break
        else:
            print("Invalid choice. Please enter a valid option (1-6).")

if __name__ == "__main__":
    main()
