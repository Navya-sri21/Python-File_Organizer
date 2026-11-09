import UserOperations
import main_db1
from Register import Register
from login import Login
from File_model import File
from Category import Category
from Organizer import FileOrganizer



def main():
    print("=== 1. USER REGISTRATION ===")
    Register.register_user("john_doe", "pass123", "user")
    Register.register_user("admin_alice", "admin456", "admin")
    
    print("\n=== 2. AUTHENTICATION (LOGIN) ===")
    user_session = Login.authenticate("admin_alice", "admin456")

    if user_session:
        print("\n=== 3. FILE ORGANIZER OPERATIONS ===")
        # Create Files
        doc = File("Project_Report.pdf", "PDF Document", 512.0)
        img = File("Chart.png", "PNG Image", 128.5)

        # Create Category & Add File
        docs_cat = Category("Documents", ".pdf")
        docs_cat.add_file(doc)

        # Create Organizer & Populate
        organizer = FileOrganizer()
        organizer.add_category(docs_cat)
        organizer.add_file(doc)
        organizer.add_file(img)

        # List files using logged-in user's role
        organizer.list_files(user_session.role)

        print("\n=== 4. SYSTEM COUNTERS & LOGOUT ===")
        print("Total Registered Users:", len(Register.registered_users))
        print("Total Files Created:", File.get_total_files())
        print("Total Categories Created:", Category.get_total_categories())
        
        Login.logout()

if __name__ == "__main__":
    main()
