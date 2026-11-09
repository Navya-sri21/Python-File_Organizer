from dbconnection import connection_db


class FileOrganizer:

    def list_files(self):

        connector = connection_db()
        cursor = connector.cursor()

        query = """
            SELECT f.file_id, f.file_name, f.extension,
                   f.file_size, c.category_name, f.file_path
            FROM files f
            LEFT JOIN categories c
                ON f.category_id = c.category_id
            ORDER BY f.file_id
        """

        cursor.execute(query)

        files = cursor.fetchall()

        print("\n--- FILE ORGANIZER ---")

        if not files:
            print("No files available.")

        for file in files:
            print(
                "ID:", file[0],
                "| Name:", file[1],
                "| Extension:", file[2],
                "| Size:", file[3],
                "| Category:", file[4],
                "| Path:", file[5]
            )

        cursor.close()
        connector.close()

    def organize_files(self, folder_path):
        print("Organizing files...")
        print("Selected folder:", folder_path)