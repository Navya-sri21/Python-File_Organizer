class User:
    total_users=0
    def __init__(self,username,password,role: str="user"):
        self.username=username       #Instance variables (unique to each object)
        self.password=password  
        self.role=role
        User.total_users+=1    # Increment  class variable on object 
        def display_profile(self):
            print(f"[USER PROFILE] username;{self.username} Role:{self.role}")
@classmethod
def get_total_users(cls):
    return cls.total_users
