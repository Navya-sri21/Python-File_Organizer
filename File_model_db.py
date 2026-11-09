from dbconnection import connection_db


class File:

    def add_file(self, filename, extension, file_size,
                 category_id, file_path):

        connector = connection_db()
        cursor = connector.cursor()

        query = """
            INSERT INTO files
            (file_name, extension, file_size, category_id, file_path)
            VALUES (%s, %s, %s, %s, %s)
        """

        values = (
            filename,
            extension,
            file_size,
            category_id,
            file_path
        )

        cursor.execute(query, values)
        connector.commit()

        print("File added successfully.")
        print("File ID:", cursor.lastrowid)

        cursor.close()
        connector.close()

    def display_files(self):

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

        for file in files:
            print(file)

        cursor.close()
        connector.close()
