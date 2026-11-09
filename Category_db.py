from dbconnection import connection_db
class Category:

    def add_category(self, category_name):

        connector = connection_db()
        cursor = connector.cursor()

        query = """
            INSERT IGNORE INTO categories (category_name)
            VALUES (%s)
        """

        cursor.execute(query, (category_name,))
        connector.commit()

        if cursor.rowcount == 1:
            print("Category added successfully.")
        else:
            print("Category already exists.")

        cursor.close()
        connector.close()

    def display_categories(self):

        connector = connection_db()
        cursor = connector.cursor()

        query = "SELECT * FROM categories ORDER BY category_id"
        cursor.execute(query)

        categories = cursor.fetchall()

        for category in categories:
            print(category)

        cursor.close()
        connector.close()
