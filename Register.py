from user_profile import User# importing first file name and class name
class Register:
    registered_users={} # class variable storing username
    @classmethod
    def register_user(cls,username:str,password:str,role:str="user"):
        if username in cls.registered_users:
            print(f"[REGISTER FAILED] Username '{username}' already exists!")
            return False
        new_user = User(username, password, role)
        cls.registered_users[username] = new_user
        print(f"[REGISTER SUCCESS] User '{username}' registered successfully.")
        return True

    @staticmethod
    def register_info():
        return "Register system enforces unique usernames and initializes User accounts."
        
