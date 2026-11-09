from Register import Register
from user_profile import User

class Login:
    active_session = None

    @classmethod
    def authenticate(cls, username, password):
        user = Register.registered_users.get(username)
        if user and user.password == password:
            cls.active_session = user
            print(f"[LOGIN SUCCESS] Welcome, {username} ({user.role})!")
            return user
        print("[LOGIN FAILED] Invalid username or password.")
        return None

    @classmethod
    def logout(cls):
        if cls.active_session :
            #user_name=cls.active_session.username
            #cls.active_session.logout()
            #cls.active_session = None
            #print(f"[LOGOUT] User '{cls.active_session.username}' logged out.")
        #else:
            print("[LOGOUT] No active session to log out.")
            cls.active_session = None

    @staticmethod
    def login_info():
        return "Login system validates user credentials and maintains current session."
