

import UserOperations

from FileOrganizer_db import FileOrganizer
from Category_db import Category
from Organizationlogs_db import OrganizationLogs



print("WELCOME TO SMART FILE ORGANIZER")



while True:

    print("\n========== MAIN MENU ==========")



    choice = input("Enter your choice:1. Register 2. Login 3. Exit: ")


    # REGISTRATION

    if choice == "1":

        email = input("Enter an Email: ")
        name = input("Enter a Name: ")
        pwd = input("Enter a Password: ")

        UserOperations.registerUser(email, name, pwd)


    # LOGIN

    elif choice == "2":

        email = input("Enter an Email: ")
        pwd = input("Enter a Password: ")

        status = UserOperations.login(email, pwd)


        if status:

            print("\nLogin Successful!")

            # CREATE OBJECTS

            organizer = FileOrganizer()
            category = Category()
            logs = OrganizationLogs()


            # FILE ORGANIZER MENU

            while True:

                print("\n========== FILE ORGANIZER MENU ==========")

                print("1. Organize Files")
                print("2. View Files")
                print("3. View Categories")
                print("4. View Organization History")
                print("5. Logout")

                option = input("Enter your choice: ")


                # ORGANIZE FILES

                if option == "1":

                    folder_path = input("Enter folder path: ")

                    organizer.organize_files(folder_path)


                # DISPLAY FILES

                elif option == "2":

                    organizer.list_files()


                # DISPLAY CATEGORIES

                elif option == "3":

                    category.display_categories()


                # DISPLAY ORGANIZATION LOGS

                elif option == "4":

                    logs.display_logs()


                # LOGOUT

                elif option == "5":

                    print("Logout Successful!")

                    break


                else:

                    print("Invalid choice!")


        else:

            print("Login Failed! Please try again.")


    # EXIT

    elif choice == "3":

        print("Thank you for using Smart File Organizer!")

        break


    else:

        print("Invalid choice! Please enter 1, 2 or 3.")