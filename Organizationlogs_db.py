from dbconnection import connection_db

class OrganizationLogs:

    def add_log(self, file_id, action):

        connector = connection_db()
        cursor = connector.cursor()

        query = """
            INSERT INTO organization_logs (file_id, action)
            VALUES (%s, %s)
        """

        cursor.execute(query, (file_id, action))
        connector.commit()

        print("Organization log saved successfully.")

        cursor.close()
        connector.close()

    def display_logs(self):

        connector = connection_db()
        cursor = connector.cursor()

        query = """
            SELECT log_id, file_id, action, action_data
            FROM organization_logs
            ORDER BY log_id
        """

        cursor.execute(query)
        logs = cursor.fetchall()

        for log in logs:
            print(log)

        cursor.close()
        connector.close()
