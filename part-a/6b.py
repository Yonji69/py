import os
import zipfile

def create_zip(folder_path, zip_file_name):
    try:
        with zipfile.ZipFile(zip_file_name, "w") as zip_file:
            for root, _, files in os.walk(folder_path):
                for file in files:
                    file_path = os.path.join(root, file)
                    arcname = os.path.relpath(file_path, folder_path)
                    zip_file.write(file_path, arcname)
            print(f"ZIP file '{zip_file_name}' created successfully.")
    except Exception as e:
        print(f"Error occurred: {e}")

if __name__ == "__main__":
    folder_path = input("Enter the folder path to zip: ")
    zip_file_name = input("Enter the name of the ZIP file to create: ")
    create_zip(folder_path, zip_file_name)
