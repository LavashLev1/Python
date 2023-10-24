import shutil
import os
import unicodedata

def normalize(text):
    # Транслітерація кирилічних символів на латиницю
    normalized_text = ''.join(c if unicodedata.category(c) in ('Ll', 'Lu', 'Nd', 'Zs') else '_' for c in text)
    # Заміна всіх символів, окрім літер латинського алфавіту та цифр, на '_'
    return normalized_text

def sort_folder(folder_path):
    # Перелік розширень для різних категорій
    image_extensions = ('JPEG', 'PNG', 'JPG', 'SVG')
    video_extensions = ('AVI', 'MP4', 'MOV', 'MKV')
    document_extensions = ('DOC', 'DOCX', 'TXT', 'PDF', 'XLSX', 'PPTX')
    audio_extensions = ('MP3', 'OGG', 'WAV', 'AMR')
    archive_extensions = ('ZIP', 'GZ', 'TAR')

    # Цільові папки для різних категорій
    target_folders = {
        'images': 'images',
        'videos': 'videos',
        'documents': 'documents',
        'audio': 'audio',
        'archives': 'archives',
    }

    # Переміщення файлів та папок у відповідні категорії
    for root, dirs, files in os.walk(folder_path):
        for file in files:
            file_path = os.path.join(root, file)
            file_extension = file.split('.')[-1].upper()
            normalized_file_name = normalize(file)

            if file_extension in image_extensions:
                target_folder = target_folders['images']
            elif file_extension in video_extensions:
                target_folder = target_folders['videos']
            elif file_extension in document_extensions:
                target_folder = target_folders['documents']
            elif file_extension in audio_extensions:
                target_folder = target_folders['audio']
            elif file_extension in archive_extensions:
                target_folder = target_folders['archives']
                # Розпаковка архіву
                shutil.unpack_archive(file_path, os.path.join(root, normalized_file_name))
                continue  # Перейти до наступного файлу після розпаковки архіву
            else:
                # Розширення невідомої категорії
                continue  # Перейти до наступного файлу

            target_folder_path = os.path.join(root, target_folder)
            os.makedirs(target_folder_path, exist_ok=True)
            shutil.move(file_path, os.path.join(target_folder_path, normalized_file_name))

    # Видалення порожніх папок
    for root, dirs, files in os.walk(folder_path, topdown=False):
        for dir in dirs:
            dir_path = os.path.join(root, dir)
            if not os.listdir(dir_path):
                os.rmdir(dir_path)

if __name__ == "__main__":
    import sys

    if len(sys.argv) != 2:
        print("Usage: python sort.py <folder_path>")
        sys.exit(1)

    folder_path = sys.argv[1]
    sort_folder(folder_path)
