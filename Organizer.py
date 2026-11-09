from File_model import File
from Category import Category

class FileOrganizer:
    organizer_count = 0

    def __init__(self):
        self.categories = []
        self.files = []
        FileOrganizer.organizer_count += 1

    def add_category(self, category: Category):
        if isinstance(category, Category):
            self.categories.append(category)

    def add_file(self, file: File):
        if isinstance(file, File):
            self.files.append(file)

    def remove_file(self, filename: str):
        self.files = [f for f in self.files if f.filename != filename]

    def list_files(self, user_role: str = "user"):
        print(f"\n--- Files Managed in Organizer (View: {user_role.upper()}) ---")
        if not self.files:
            print("No files available.")
        for file in self.files:
            file.display_info(user_role)

    @staticmethod
    def organizer_info():
        return "FileOrganizer centralizes file operations and category assignments."

    @classmethod
    def get_organizer_count(cls):
        return cls.organizer_count



