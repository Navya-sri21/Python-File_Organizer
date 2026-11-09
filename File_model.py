class File:
    total_files = 0

    def __init__(self, filename: str, file_type: str, file_size: float):
        self.filename = filename
        self.file_type = file_type
        self.file_size = file_size  
        File.total_files += 1

    def update_filename(self, new_name: str):
        self.filename = new_name

    def display_info(self, user_type: str = "user"):
        if user_type.lower() == "admin":
            print(f"[ADMIN VIEW] File: {self.filename} | Type: {self.file_type} | Size: {self.file_size} KB")
        else:
            print(f"[USER VIEW] File: {self.filename} ({self.file_type})")

    @staticmethod
    def file_info():
        return "File class models individual file attributes."

    @classmethod
    def get_total_files(cls):
        return cls.total_files
