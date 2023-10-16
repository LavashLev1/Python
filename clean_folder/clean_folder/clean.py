import os
import sys

def clean_folder(path):
    # Реалізація розбору папки
    # Наприклад, виведення списку файлів у папці:
    for root, dirs, files in os.walk(path):
        for file in files:
            print(os.path.join(root, file))

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: clean-folder <folder_path>")
        sys.exit(1)

    folder_path = sys.argv[1]
    clean_folder(folder_path)