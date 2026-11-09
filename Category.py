from File_model import File

class Category:
    total_categories = 0

    def __init__(self, category_name: str, file_extension: str):
        self.category_name = category_name
        self.file_extension = file_extension
        self.files = []
        Category.total_categories += 1

    def add_file(self, file: File):
        if isinstance(file, File):
            self.files.append(file)

    def remove_file(self, filename: str):
        self.files = [f for f in self.files if f.filename != filename]

    @staticmethod
    def category_info():
        return "Category class groups files matching target extensions."

    @classmethod
    def get_total_categories(cls):
        return cls.total_categories
