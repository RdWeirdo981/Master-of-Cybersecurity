import re
import datetime


class CMS:
    list_of_topics = ["0 - Artificial Intelligence", "1 - Cybersecurity", "2 - Cloud Computing", "3 - Data Analysis",
                      "4- Communication and Transportation"]
    list_of_keywords = ["AI", "Security", "Cloud Computing", "High Performance", "Data", "Protocol", "Neural Network"]
    list_of_qualification = ["0 - Less than diploma", "1 - Diploma", "2 - Bachelor", "3 - Master", "4 - PhD",
                             "5 - Others"]

    def get_user_list(self):
        with open("user_db.txt", 'r') as user_db:
            lines = user_db.readlines()[1:]
            user_list = []
            for line in lines:
                single_user = line[:-1].split(',')
                user_list.append(single_user)
        return user_list

    def get_conference_list(self):
        with open("conference_db.txt", 'r') as conference_db:
            lines = conference_db.readlines()[1:]
            conference_list = []
            for line in lines:
                single_conference = line[:-1].split(',')
                conference_list.append(single_conference)
        return conference_list

    def user_login(self, user_email, user_password):
        user_list = self.get_user_list()
        for user in user_list:
            if user[2] == user_email and user[3] == user_password:
                return True
        return False

    def user_registration(self, first_name, last_name, user_email, user_password, highest_qualification,
                          user_occupation, employer_details, mobile_number, interest_area):
        new_user = User(first_name, last_name, user_email, user_password, highest_qualification, user_occupation,
                        employer_details, mobile_number, interest_area)
        new_user.save_user()

    def verify_register_password(self, password):
        if len(password) < 8 or not re.search("[a-z]", password) or not re.search("[A-Z]", password) or not re.search(
                "[0-9]", password):
            return False
        return True

    def verify_register_qualification(self, hq):
        if hq not in ["0", "1", "2", "3", "4", "5"]:
            return False
        return True

    def verify_register_topics(self, topics):
        if topics not in ["0", "1", "2", "3", "4"]:
            return False
        return True

    def verify_register_phone(self, phone):
        if len(str(phone)) == 10:
            return True
        return False


class conference:
    def __init__(self, conference_name, conference_title, conference_topics, submit_deadline_year,
                 submit_deadline_month, submit_deadline_day, conference_chair):
        self.set_conference_name(conference_name)
        self.set_conference_title(conference_title)
        self.set_conference_topics(conference_topics)
        self.set_submit_deadline_year(submit_deadline_year)
        self.set_submit_deadline_month(submit_deadline_month)
        self.set_submit_deadline_day(submit_deadline_day)
        self.set_conference_chair(conference_chair)

    # Accessor
    def get_conference_name(self):
        return self.conference_name

    def get_conference_title(self):
        return self.conference_title

    def get_conference_topics(self):
        return self.conference_topics

    def get_submit_deadline_year(self):
        return self.submit_deadline_year

    def get_submit_deadline_month(self):
        return self.submit_deadline_month

    def get_submit_deadline_day(self):
        return self.submit_deadline_day

    def get_conference_chair(self):
        return self.conference_chair

    # Mutator
    def set_conference_name(self, name):
        self.conference_name = name
        return True

    def set_conference_title(self, title):
        self.conference_title = title
        return True

    def set_conference_topics(self, topics):
        self.conference_topics = topics
        return True

    def set_submit_deadline_year(self, year):
        self.submit_deadline_year = year
        return True

    def set_submit_deadline_month(self, month):
        self.submit_deadline_month = month
        return True

    def set_submit_deadline_day(self, day):
        self.submit_deadline_day = day
        return True

    def set_conference_chair(self, chair):
        self.get_conference_chair = chair
        return True

    # Save conference
    def save_conference(self):
        new_conference = [self.conference_name, self.conference_title, self.conference_topics,
                          self.submit_deadline_year, self.submit_deadline_month,
                          self.submit_deadline_day, self.conference_chair]
        with open("conference_db.txt", 'a+') as conference_db:
            conference_db.write(", ".join(new_conference) + "\n")


# class Paper:

class User:

    def __init__(self, first_name, last_name, user_email, user_password, highest_qualification, user_occupation,
                 employer_details, mobile_number, interest_area):
        self.set_first_name(first_name)
        self.set_last_name(last_name)
        self.set_user_email(user_email)
        self.set_user_password(user_password)
        self.set_highest_qualification(highest_qualification)
        self.set_user_occupation(user_occupation)
        self.set_employer_details(employer_details)
        self.set_mobile_number(mobile_number)  # 10-dig number
        self.set_interest_area(interest_area)

    # Accessor
    def get_first_name(self):
        return self.first_name

    def get_last_name(self):
        return self.last_name

    def get_user_email(self):
        return self.user_email

    def get_user_password(self):
        return self.user_password

    def get_highest_qualification(self):
        return self.highest_qualification

    def get_user_occupation(self):
        return self.user_occupation

    def get_employer_details(self):
        return self.employer_details

    def get_mobile_number(self):
        return self.mobile_number

    def get_interest_area(self):
        return self.interest_area

    # Mutator
    def set_first_name(self, fn):
        self.first_name = fn

    def set_last_name(self, ln):
        self.last_name = ln

    def set_user_email(self, email):
        self.user_email = email

    def set_user_password(self, pw):  # pw invalidation check in CMS class
        self.user_password = pw

    def set_highest_qualification(self, hq):  # qualification check in CMS class
        self.highest_qualification = hq

    def set_user_occupation(self, occupation):
        self.user_occupation = occupation

    def set_employer_details(self, employer):
        self.employer_details = employer

    def set_mobile_number(self, phone):  # phone number check in CMS class
        self.mobile_number = phone

    def set_interest_area(self, topics):  # interest area check in CMS class
        self.interest_area = topics

    # Save User into user_db
    def save_user(self):
        new_user = [self.first_name, self.last_name, self.user_email, self.user_password, self.highest_qualification,
                    self.user_occupation, self.employer_details, self.mobile_number, self.interest_area, "False"]
        with open("user_db.txt", 'a+') as user_db:
            user_db.write(", ".join(new_user) + "\n")


class Admin:
    system = CMS()

    # Generate User report
    def generate_user_report(self):
        user_list = self.system.get_user_list()
        for user in user_list:
            print("First name: " + user[0])
            print("Last name: " + user[1])
            print("User email: " + user[2])
            print("Highest Qualification: " + user[4])
            print("Occupation: " + user[5])
            print("Employer details: " + user[6])
            print("Mobile number: " + user[7])
            print("Interest area: " + user[8])
            print("Admin permission: " + user[9])
            print("\n")

    # Generate Conference report
    def generate_conference_report(self):
        conference_list = self.system.get_conference_list()
        for conference in conference_list:
            print("Conference name: " + conference[0])
            print("Conference title: " + conference[1])
            print("Conference topics: " + conference[2])
            submit_deadline = datetime.datetime(int(conference[3]), int(conference[4]), int(conference[5]))
            print("Paper submit deadline: " + str(submit_deadline))
            print("Conference chair" + conference[6])
            print("Accepted paper: " + str(len(conference) - 7))
            for item in conference[7:]:
                print(item)
            print("\n")


# class Admin:
#     def adminmethod(self):
#         self.firstname = []
#         self.lastname = []
#         self.useremail = []
#         self.highestqualification = []
#         self.useroccupation = []
#         self.employerdetails = []
#         self.mobilenumber = []
#         self.interestarea = []

#         openfile = open("user_db.txt", "r")
#         next(openfile)
#         for line in openfile:
#             linelist = line.split(", ")
#             firstname.append(linelist[0])
#             lastname.append(linelist[1])
#             useremail.append(linelist[2])
#             highestqualification.append(linelist[4])
#             useroccupation.append(linelist[5])
#             employerdetails.append(linelist[6])
#             mobilenumber.append(linelist[7])
#             interestarea.append(linelist[8].split("\n")[0])

#     def get_all_firstname(self):
#         return self.firstname

#     def get_all_lastname(self):
#         return self.lastname

#     def get_all_useremail(self):
#         return self.useremail

#     def get_all_highestqualification(self):
#         return self.highestqualification

#     def get_all_useroccupation(self):
#         return self.useroccupation

#     def get_all_employerdetails(self):
#         return self.employerdetails

#     def get_all_mobilenumber(self):
#         return self.mobilenumber

#     def get_all_interestarea(self):
#         return self.interestarea


# class Chair:
#     # add paper
#     def add_paper(self, paper):
#         paper_name = paper.get_paper_name()
#         system = CMS()
#         conference_list = system.get_conference_list()
#         # Find conference in conference_db


#             conference_db.write(", ".join(new_user) + "\n")

# class Author:

# class Reviewer:

# class Evaluation:

# class Notification:

class UserInterface:
    new_system = CMS()

    def display_title_box(self):
        print("**************************************")
        print("*                                    *")
        print("*    Conference Management System    *")
        print("*                                    *")
        print("**************************************")

    def display_main_page(self):
        self.display_title_box()
        print("Welcome to Conference Management System. Please choose to login or create an account.")
        print("1. Login")
        print("2. Create an account")
        user_input = input("Enter your choices from 1 or 2: ")
        if user_input == "1":
            self.display_login_page()
        elif user_input == "2":
            self.display_register_page()
        else:
            print("Invalid input. Please only enter 1 or 2.")
            self.display_main_page()

    def display_login_page(self):
        self.display_title_box()
        print("Login using your email and password.")
        flag = False
        count = 0
        while not flag:
            count += 1
            user_email = input("Enter your email: ")
            user_password = input("Enter your password: ")
            flag = self.new_system.user_login(user_email, user_password)
            if not flag and count == 3:
                print("Exceed 3 times. Back to main page.")
                break
            elif not flag:
                print("Invalid email or password. Try again.")
        if flag:
            print("Login success. Jumping to the Home page...")
            self.display_home_page()
        else:
            print("Login failed. Back to Main page.")
            self.display_main_page()

    def display_register_page(self):
        self.display_title_box()
        print("Please fill your personal information to finish the registration.")

        first_name = input("First name: ")
        last_name = input("Last name: ")
        user_email = input("Email: ")

        print(
            "Notice: Password should be at least 8 characters long, must include 1 lower case, 1 upper case, and 1 number.")  # validation check
        flag_password = False
        while not flag_password:
            user_password = input("Password: ")
            flag_password = self.new_system.verify_register_password(user_password)
            if not flag_password:
                print("Invalid Password. Try again.")

        print(
            "Notice: please enter the number fit your highest qualification from the following list.")  # validation check
        print(self.new_system.list_of_qualification)
        flag_qualification = False
        while not flag_qualification:
            choice = input("Highest qualification: ")
            flag_qualification = self.new_system.verify_register_qualification(choice)
            if not flag_qualification:
                print("Invalid qualification. Please choose from the list.")
        if flag_qualification:
            for qualification in self.new_system.list_of_qualification:
                if self.new_system.list_of_qualification[int(choice)] == qualification:
                    highest_qualification = qualification

        user_occupation = input("Occupation: ")
        employer_details = input("Employer details: ")

        print("Notice: mobile number should be a 10-digit number.")
        flag_phone = False
        while not flag_phone:
            try:
                mobile_number = int(input("Mobile number: "))
                flag_phone = self.new_system.verify_register_phone(mobile_number)
                if not flag_phone:
                    print("Number has to be 10 digit. Try again.")
            except:
                print("Please only enter number.")
        if flag_phone:
            mobile_number = str(mobile_number)

        interest_area = self.display_topics_choosing()  # validation check

        self.new_system.user_registration(first_name, last_name, user_email, user_password, highest_qualification,
                                          user_occupation, employer_details, mobile_number, interest_area)
        # confirmation
        print("Please choose your action forward.")
        print("1 - Submit your registration")
        print("2 - Cancel registration and return to main page")
        choice_flag = False
        while not choice_flag:
            choice = input("Enter your choice: ")
            if choice == "1":
                choice_flag = True
                print("You've created a new account. Jumping to the Home page...")
                self.display_home_page()
            elif choice == "2":
                choice_flag = True
                print("Returning to the main page...")
                self.display_main_page()
            else:
                print("Please only choose from 1 or 2.")

    def display_topics_choosing(self):  # used in registration, register, paper, conference to choose topics
        print("Notice: please enter the number fit your interest area from the following list.")
        print(self.new_system.list_of_topics)
        flag_topics = False
        while not flag_topics:
            choice = input("Interest area: ")
            flag_topics = self.new_system.verify_register_topics(choice)
            if not flag_topics:
                print("Invalid topics. Please choose from the list.")
        if flag_topics:
            for topics in self.new_system.list_of_topics:
                if self.new_system.list_of_topics[int(choice)] == topics:
                    interest_area = topics
        return interest_area

    def display_home_page(self):
        self.display_title_box()
        print("Please choose the user type: ")
        print("1- Chair")
        print("2 - Author")
        print("3 - Reviewer")
        print("4 - Admin")
        print("5 - Return to main page")
        choice_flag = False
        while not choice_flag:
            choice = input("Enter your choice from 1 to 5: ")
            if choice == "1":
                choice_flag = True
                self.display_chair_page()
            elif choice == "2":
                choice_flag = True
                self.display_author_page()
            elif choice == "3":
                choice_flag = True
                self.display_reviewer_page()
            elif choice == "4":
                choice_flag = True
                self.display_admin_page()
            elif choice == "5":
                choice_flag = True
                self.display_main_page()
            else:
                print("Please only enter number 1 to 5.")

    def display_chair_page(self):
        self.display_title_box()

    def display_author_page(self):
        self.display_title_box()

    def display_reviewer_page(self):
        self.display_title_box()

    def display_admin_page(self):
        self.display_title_box()
        print("Please choose your actions.")
        print("1 - Generate user report")
        print("2 - Generate conference report")
        print("3 - Return to home page")
        choice_flag = False
        while not choice_flag:
            choice = input("Enter your choice from 1 or 3: ")
            if choice == "1":
                choice_flag = True
                self.display_generate_user()
            elif choice == "2":
                choice_flag = True
                self.display_generate_conference()
            elif choice == "3":
                choice_flag = True
                self.display_home_page()
            else:
                print("Please only choose from 1 or 3.")

    def display_generate_user(self):
        self.display_title_box()
        new_admin = Admin()
        new_admin.generate_user_report()
        self.display_admin_return()

    def display_generate_conference(self):
        self.display_title_box()
        new_admin = Admin()
        new_admin.generate_conference_report()
        self.display_admin_return()

    def display_admin_return(self):
        print("Please choose your actions.")
        print("1 - Return to the admin page")
        print("2 - Return to home page")
        print("3 - Return to main page")
        choice_flag = False
        while not choice_flag:
            choice = input("Enter your choice from 1 to 3: ")
            if choice == "1":
                choice_flag = True
                self.display_admin_page()
            elif choice == "2":
                choice_flag = True
                self.display_home_page()
            elif choice == "3":
                choice_flag = True
                self.display_main_page()
            else:
                print("Invalid input. Try again.")


if __name__ == "__main__":
    conference_management_system = UserInterface()
    conference_management_system.display_main_page()
