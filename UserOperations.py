
from dbconnection import connection_db
def registerUser(emailID, uname, pwd):

    connector = connection_db()
    cursor = connector.cursor()
    query = "SELECT emailID FROM users WHERE emailID = %s"
    cursor.execute(query, (emailID,))

    if cursor.fetchone():
        print("This email is already registered!")

    else:
        query = """
            INSERT INTO users (emailID, uname, password)
            VALUES (%s, %s, %s)
        """

        cursor.execute(query, (emailID, uname, pwd))
        connector.commit()

        print("User registered successfully!")
        print("Rows inserted:", cursor.rowcount)

    cursor.close()
    connector.close()

"""login function"""

def login(email, pwd):
    connector = connection_db()
    cursor1 = connector.cursor()
    query = "SELECT * FROM users WHERE emailId=%s"
    cursor1.execute(query, (email,))

    user = cursor1.fetchone()
    cursor1.close()
    connector.close()
    if user is None:
        print("User not found. Please register first.")
    elif user[3] ==pwd :
        print("Login Successful")
        return True
    else:
        print("Incorrect password")
        return False


    
  

