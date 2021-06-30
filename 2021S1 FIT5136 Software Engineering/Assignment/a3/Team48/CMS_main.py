import re
import datetime

class CMS:
    list_of_topics = ["Artificial Intelligence", "Cybersecurity", "Cloud Computing", "Data Analysis",
                      "Communication and Transportation"]
    list_of_keywords = ["AI", "Security", "Cloud Computing", "High Performance", "Data",
                        "Protocol", "Neural Network"]
    list_of_qualification = ["Less than diploma", "Diploma", "Bachelor", "Master", "PhD",
                             "Higher than PhD"]

    # For getting information
    def get_user_list(self):
        with open("user_db.txt", 'r') as user_db:
            lines = user_db.readlines()[1:]
            user_list = []
            for line in lines:
                single_user = line[:-1].split(', ')
                user_list.append(single_user)
        return user_list

    def show_user_list(self):
        list1 = []
        list2 = []
        s = 1
        with open('user_db.txt','r') as file:
            lines = file.readlines()[1:]
            for line in lines:
                list3 = line.split(', ')
                list2.append(str(s))
                list2.append(list3[2])
                list2.append(list3[8])
                list1.append(list2)
                list2 = []
                s += 1
            return list1

    def get_user_info(self, user_email, user_password):
        user_list = self.get_user_list()
        for user in user_list:
            if user[2] == user_email and user[3] == user_password:
                return user

    def show_conference_list(self):
        with open('conference_db.txt', 'r+') as conference_db:
            lines = conference_db.readlines()[1:]
            i = 1
            list2 = []
            list1 = []
            for line in lines:
                list1 = line.split()
                list2.append(list1)


            return list2

    def get_conference_list(self):
        with open("conference_db.txt", 'r') as conference_db:
            lines = conference_db.readlines()[1:]
            conference_list = []
            for line in lines:
                single_conference = line[:-1].split(', ')
                conference_list.append(single_conference)
        return conference_list

    def get_paper_list(self):
        with open("paper_db.txt", 'r') as paper_db:
            lines = paper_db.readlines()[1:]
            paper_list = []
            for line in lines:
                single_paper = line[:-1].split(', ')
                paper_list.append(single_paper)
        return paper_list

    def get_conference_topic_list(self):
        list_of_topics = ["0 - Artificial Intelligence", "1 - Cybersecurity", "2 - Cloud Computing",
                          "3 - Data Analysis", "4- Communication and Transportation"]
        self.list_of_topics = list_of_topics


    # For main page
    def user_login(self, user_email, user_password):
        user_list = self.get_user_list()
        for user in user_list:
            if user[2] == user_email and user[3] == user_password:
                return True
        return False

    def user_registration(self, new_user):
        new_user.save_user()

    # Verify
    def verify_register_email_exist(self, email):
        user_list = self.get_user_list()
        for user in user_list:
            if email == user[2]:
                return False
        return True
    def verify_register_email(self, email):
        if "@" in email and "." in email:
            return True
        return False

    def verify_register_password(self, password):
        if len(password) < 8 or not re.search("[a-z]", password) or not re.search("[A-Z]", password) or not re.search(
                "[0-9]", password):
            return False
        return True

    def verify_register_qualification(self, hq):
        if hq not in ["1", "2", "3", "4", "5","6"]:
            return False
        return True

    def verify_register_topics(self, topics):
        if topics not in ["1", "2", "3", "4","5"]:
            return False
        return True

    def verify_register_phone(self, phone):
        if len(str(phone)) == 10:
            return True
        return False

    def verify_admin(self, a_user):
        if a_user.get_admin_permission() == "True":
            return True
        return False

class Conference:
    def __init__(self, conference_name, conference_title, conference_topics, submit_deadline_year,
                 submit_deadline_month, submit_deadline_day, conference_chair):
        self.set_conference_name(conference_name)
        self.set_conference_title(conference_title)
        self.set_conference_topics(conference_topics)
        self.set_submit_deadline_year(submit_deadline_year)
        self.set_submit_deadline_month(submit_deadline_month)
        self.set_submit_deadline_day(submit_deadline_day)
        self.set_conference_chair(conference_chair)
        # self.set_conference_accepted_paper(conference_accepted_paper)

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

    def get_conference_accepted_paper(self):
        return self.conference_accepted_paper

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
        self.conference_chair = chair
        return True

    def set_conference_accepted_paper(self, paper):
        self.conference_accepted_paper = paper
        return True

    # Save conference
    def save_conference(self):
        new_conference = [self.conference_name, self.conference_title, self.conference_topics,
                          self.submit_deadline_year, self.submit_deadline_month,
                          self.submit_deadline_day, self.conference_chair]
        with open("conference_db.txt", 'a+') as conference_db:
            conference_db.write(", ".join(new_conference) + "\n")

class Paper:
    def __init__(self,filename, paper_title, paper_topics, paper_keywords, author_names, paper_submit_year, paper_submit_month,
                 paper_submit_day, conference_name, paper_status, reviewer1, reviewer2, reviewer3):
        self.filename = filename
        self.set_paper_title(paper_title)
        self.set_paper_topics(paper_topics)
        self.set_paper_keywords(paper_keywords)
        self.set_author_names(author_names)
        self.set_paper_submit_year(paper_submit_year)
        self.set_paper_submit_month(paper_submit_month)
        self.set_paper_submit_day(paper_submit_day)
        self.set_conference_name(conference_name)
        self.set_paper_status(paper_status)
        self.reviewer1 = reviewer1
        self.reviewer2 = reviewer2
        self.reviewer3 = reviewer3
    # Accessor
    def get_paper_title(self):
        return self.paper_title

    def get_paper_topics(self):
        return self.paper_topics

    def get_paper_keywords(self):
        return self.paper_keywords

    def get_author_names(self):
        return self.author_names

    def get_paper_submit_year(self):
        return self.paper_submit_year

    def get_paper_submit_month(self):
        return self.paper_submit_month

    def get_paper_submit_day(self):
        return self.paper_submit_day

    def get_conference_name(self):
        return self.conference_name

    def get_paper_status(self):
        return self.paper_status

    # Mutator
    def set_paper_title(self, paper_title):
        self.paper_title = paper_title
        return True

    def set_paper_topics(self, paper_topics):
        self.paper_topics = paper_topics
        return True

    def set_paper_keywords(self, paper_keywords):
        self.paper_keywords = paper_keywords
        return True

    def set_author_names(self, author_names):
        self.author_names = author_names
        return True

    def set_paper_submit_year(self, paper_submit_year):
        self.paper_submit_year = paper_submit_year
        return True

    def set_paper_submit_month(self, paper_submit_month):
        self.paper_submit_month = paper_submit_month
        return True

    def set_paper_submit_day(self, paper_submit_day):
        self.paper_submit_day = paper_submit_day
        return True

    def set_conference_name(self, conference_name):
        self.conference_name = conference_name
        return True

    def set_paper_status(self, paper_status):
        self.paper_status = paper_status
        return True

    # Save paper in db
    def save_paper(self):
        new_paper = [self.filename, self.paper_title, self.paper_topics, self.paper_keywords, self.author_names,
                     self.paper_submit_year, self.paper_submit_month, self.paper_submit_day, self.conference_name,
                     self.paper_status,self.reviewer1, self.reviewer2, self.reviewer3]
        with open("paper_db.txt", 'a+') as paper_db:
            paper_db.write(", ".join(new_paper) + "\n")

class User:

    def __init__(self, first_name, last_name, user_email, user_password, highest_qualification, user_occupation,
                 employer_details, mobile_number, interest_area, admin_permission):
        self.set_first_name(first_name)
        self.set_last_name(last_name)
        self.set_user_email(user_email)
        self.set_user_password(user_password)
        self.set_highest_qualification(highest_qualification)
        self.set_user_occupation(user_occupation)
        self.set_employer_details(employer_details)
        self.set_mobile_number(mobile_number)  # 10-dig number
        self.set_interest_area(interest_area)
        self.set_admin_permission(admin_permission)  # True or False, str

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

    def get_admin_permission(self):
        return self.admin_permission

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

    def set_admin_permission(self, permission):
        self.admin_permission = permission

    # Save User into user_db
    def save_user(self):
        new_user = [self.first_name, self.last_name, self.user_email, self.user_password, self.highest_qualification,
                    self.user_occupation, self.employer_details, self.mobile_number, self.interest_area,
                    self.admin_permission]
        with open("user_db.txt", 'a+') as user_db:
            user_db.write(", ".join(new_user) + "\n")

class AdminFeatures:
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
            print("Conference chair: " + conference[6])
            print("Accepted paper: " + str(len(conference) - 7))
            for item in conference[7:]:
                print(item)
            print("\n")

# class ChairFeatures:

class AuthorFeatures:
    # upload paper
    def verify_filename(self, filename):
        if filename[-4:] == ".txt" or filename[-4:]==".pdf":
                return True
        return False
    def verify_keywords(self, kw):
        if kw not in ["1", "2", "3", "4","5","6","7"]:
            return False
        return True
    def verify_conference(self, conference, conference_list):
        if (conference-1) in range(len(conference_list)):
                return True
        else:
            return False
    def verify_paper_submit_deadline(self, conference_name, year, month, day):
        sys = CMS()
        conference_list = sys.get_conference_list()
        for single_conference in conference_list:
            if single_conference[0] == conference_name:
                conference = single_conference
                break
        current_time = datetime.datetime(year,month,day)
        conference_deadline = datetime.datetime(int(conference[3]), int(conference[4]), int(conference[5]))
        if current_time > conference_deadline:
            return False
        return True
    def get_notification_list(self):
        with open("notification_db.txt", 'r') as noti_db:
            lines = noti_db.readlines()[1:]
            noti_list = []
            for line in lines:
                single_noti = line[:-1].split(', ')
                noti_list.append(single_noti)
        return noti_list
    
class ReviewerFeatures:
    def get_paper_list(self):
        with open("paper_db.txt", 'r') as paper_db:
            lines = paper_db.readlines()[1:]
            paper_list = []
            for line in lines:
                single_paper = line[:-1].split(', ')
                paper_list.append(single_paper)
        return paper_list

    def get_review_paper_list(self, user_email):
        paper_list = self.get_paper_list()
        review_paper_list = []
        for paper in paper_list:
            if user_email in paper[10:14]:
                review_paper_list.append(paper[1])
        return review_paper_list

    def verify_paper_choice(self, choice, paper_list):
        if choice > 0 and choice < len(paper_list):
            return True
        return False

class Evaluation:

    def __init__(self, paper, reviewer, evaluation):
        self.set_paper(paper)
        self.set_reviewer(reviewer)
        self.set_evaluation(evaluation)
    
    def get_paper(self):
        return self.paper   
    def get_reviewer(self):
        return self.reviewer
    def get_evaluation(self):
        return self.evalutation
    
    def set_paper(self, paper):
        self.paper = paper
        return True
    def set_reviewer(self, reviewer):
        self.reviewer = reviewer
        return True
    def set_evaluation(self, evaluation):
        self.evaluation = evaluation
        return True

class Notification:
    def __init__(self, paper, author, status, time):
        self.set_paper(paper)
        self.set_author(author)
        self.set_status(status)
        self.set_time(time)

    def get_paper(self):
        return self.paper()
    def get_status(self):
        return self.status()
    def get_time(self):
        return self.time()
    def get_author(self):
        return self.author()

    def set_paper(self, paper):
        self.paper = paper
        return True
    def set_status(self, status):
        self.status = status
        return True
    def set_time(self,time):
        self.time = time
        return True
    def set_author(self, author):
        self.author = author
        return True

    def save_noti(self, status):
        self.set_status(status)
        new_noti = [self.paper, self.author, self.status, str(self.time)]
        with open("notification_db.txt", 'a+') as noti_db:
            noti_db.write(", ".join(new_noti) + "\n")

class UserInterface:
    new_system = CMS()

    def display_title_box(self):
        print("**************************************")
        print("*                                    *")
        print("*    Conference Management System    *")
        print("*                                    *")
        print("**************************************")

    # Main display
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
            flag2 = False
            while not flag2:
                choice = input("Do you want to login by this credential? Y/N: ")
                if choice == "Y" or choice == "y":
                    flag2 = True
                    print("Login success. Jumping to the Home page...")
                    user_info = self.new_system.get_user_info(user_email, user_password)
                    a_user = User(user_info[0], user_info[1], user_info[2], user_info[3], user_info[4], user_info[5],
                                  user_info[6], user_info[7], user_info[8], user_info[9])
                    self.display_home_page(a_user)
                elif choice == "N" or choice == "n":
                    flag2 = True
                    print("Login cancel. Back to main page...")
                    self.display_main_page()
                else:
                    print("Invalid input. Try again.")
        else:
            self.display_main_page()

    def display_register_page(self):
        self.display_title_box()
        print("Please fill your personal information to finish the registration.")

        first_name = input("First name: ")
        last_name = input("Last name: ")
        flag_email = False
        while not flag_email:
            user_email = input("Email: ")
            flag_email = self.new_system.verify_register_email(user_email)
            if not flag_email:
                print("Invalid format. Please enter a valid email with '@' and '.'")
            else:
                flag_email = self.new_system.verify_register_email_exist(user_email)
                if not flag_email:
                    print("Email already exists. Try another one.")
            

        print(
            "Notice: Password should be at least 8 characters long, must include 1 lower case, 1 upper case, and 1 number.")  # validation check
        flag_password = False
        while not flag_password:
            user_password = input("Password: ")
            flag_password = self.new_system.verify_register_password(user_password)
            if not flag_password:
                print("Invalid Password! Try again.")

        print(
            "Notice: please enter the number fit your highest qualification from the following list.")  # validation check
        for index in range(len(self.new_system.list_of_qualification)):
            print(index+1, " - ", self.new_system.list_of_qualification[index])
        flag_qualification = False
        while not flag_qualification:
            choice = input("Highest qualification: ")
            flag_qualification = self.new_system.verify_register_qualification(choice)
            if not flag_qualification:
                print("Invalid qualification. Please choose from the list.")
        if flag_qualification:
            for qualification in self.new_system.list_of_qualification:
                if self.new_system.list_of_qualification[int(choice)-1] == qualification:
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

        new_user = User(first_name, last_name, user_email, user_password, highest_qualification, user_occupation,
                        employer_details, mobile_number, interest_area, "False")

        # confirmation
        print("Please choose your action forward.")
        print("1 - Submit your registration")
        print("2 - Cancel registration and return to main page")
        choice_flag = False
        while not choice_flag:
            choice = input("Enter your choice: ")
            if choice == "1":
                choice_flag = True
                self.new_system.user_registration(new_user)
                print("You've created a new account. Jumping to the Home page...")
                self.display_home_page(new_user)
            elif choice == "2":
                choice_flag = True
                print("Returning to the main page...")
                self.display_main_page()
            else:
                print("Please only choose from 1 or 2.")

    # Home display
    def display_home_page(self, a_user):
        self.display_title_box()
        print("Please choose the user type: ")
        print("1 - Chair")
        print("2 - Author")
        print("3 - Reviewer")
        print("4 - Admin")
        print("5 - Return to main page")
        choice_flag = False
        while not choice_flag:
            choice = input("Enter your choice from 1 to 5: ")
            if choice == "1":
                choice_flag = True
                self.display_chair_page(a_user)
            elif choice == "2":
                choice_flag = True
                self.display_author_page(a_user)
            elif choice == "3":
                choice_flag = True
                self.display_reviewer_page(a_user)
            elif choice == "4":
                permission = self.new_system.verify_admin(a_user)
                if permission == True:
                    choice_flag = True
                    self.display_admin_page(a_user)
                else:
                    print("You don't have Admin permission. Try other actions.")
            elif choice == "5":
                choice_flag = True
                self.display_main_page()
            else:
                print("Please only enter number 1 to 5.")

    # Chair features
    def display_chair_page(self, a_user):
        self.display_title_box()
        print('1 - Create conference')
        print('2 - Modify conference ')
        print('3 - Assign papers')
        print("4 - Make decision on a paper")
        print('5 - Return back to home page')
        choice_flag = True
        while choice_flag:
            choice = input('Please enter your choice: ')
            if not choice.isdigit() or not choice:
                print('You can only enter the operation number and do not enter empty.')
            if choice == '1':
                choice_flag = False
                con1 = self.display_conference_create(a_user, self.new_system)
                con1.save_conference()
                print('created conference successful')
                self.display_chair_page(a_user)
            elif choice == '2':
                choice_flag = False
                new_con1 = self.display_conference_modify(a_user, self.new_system)
                new_con1.save_conference()
                print('changed conference successful')
                self.display_chair_page(a_user)
            elif choice == '3':
                choice_flag = False
                p1 = self.display_assign_page(a_user)
                p1.save_paper()
                print('assign successful')
                self.display_chair_page(a_user)
            elif choice == '4':
                choice_flag = False
                self.display_review_evaluation(a_user)
            elif choice == '5':
                choice_flag  =False
                self.display_home_page(a_user)
            else:
                print('This enter is not operation number, try again.')
        # self.display_chair_page()

    def display_conference_create(self, user, system):
        con_name = input('please enter conference name:  ')
        con_title = input('please enter conference title:  ')
        flag = True
        while flag:
            list1 = system.list_of_topics
            i = 1
            for s in list1:
                print(str(i) + s+ ' ', end='')
                i += 1
            topic_num = input('please select conference topic from this list:  ')
            try:    
                topic_num = int(topic_num)
                con_topic = list1[topic_num-1]
                flag = False
            except:
                print('Please only enter number of choice.')
        flag1 = True
        while flag1:
            deadline_year = input('please enter submit deadline Year:  ')
            deadline_month = input('please enter submit deadline Month:  ')
            deadline_day = input('please enter submit deadline day:  ')
            if deadline_year and deadline_month and deadline_month:
                if deadline_year.isdigit() and deadline_month.isdigit() and deadline_day.isdigit():
                    if len(deadline_year) != 4:
                        print('please enter suitable Year')
                    elif int(deadline_year) > 2050:
                        print('Hi, you  set   ' + str(
                            deadline_year) + '   become deadline, nobody want to wait in this time')
                    elif int(deadline_month) > 12 or int(deadline_month) < 1:
                        print('Are you serious? Month must between 1-12')
                    elif int(deadline_day) > 31 or int(deadline_day) < 1:
                        print('Are you serious? day must between 1-31')
                    else:
                        chair = user.get_user_email()
                        flag1 = False
                else:
                    print('please enter suitable year')
            else:
                print('can not enter empty')
        con1 = Conference(con_name, con_title, con_topic, deadline_year, deadline_month, deadline_day, chair)
        return con1

    def display_conference_modify(self, user, system):

        con_list = self.new_system.show_conference_list()
        i = 1
        for s in con_list:
            print(str(i)+' -- ',end='')
            for s1 in s:
                print(s1 + ' ',end='')
            print('\n')
            i += 1 
        print('\n')
        number = input('please select the conference 1on which you want to change: ')
        number = int(number)
        print('1-conference_name ,2-conference_title ,3-conference_topics ,4-submit_deadline')
        n1 = input('please enter what you want to change: ')
        n1 = int(n1)

        with open('conference_db.txt', 'r')as f:
            lines = f.readlines()[number]
            list1 = lines.split(', ')
            name = list1[0]
        with open('conference_db.txt', 'r') as filename:
            lines = filename.readlines()
        with open('conference_db.txt', 'w') as file:
            for line in lines:
                if name in line:
                    continue
                file.write(line)
        if n1 == 1:
            con_name = input('please enter new conference name:  ')
            new_con = Conference(con_name, list1[1], list1[2], list1[3], list1[4], list1[5], list1[6])
            return new_con
        elif n1 == 2:
            con_title = input('please enter new conference title:  ')
            new_con = Conference(list1[0], con_title, list1[2], list1[3], list1[4], list1[5], list1[6])
            return new_con
        elif n1 == 3:
            flag = True
            while flag:
                topic_list = system.list_of_topics
                i = 1
                for s in topic_list:
                    print(str(i) + s + '  ', end='')
                    i  += 1
                print('\n')
                topic_num = input('please select new conference topic from this list:  ')
                topic_num = int(topic_num)
                try:
                    con_topic = topic_list[topic_num-1]
                    print(con_topic)
                    flag = False
                    new_con = Conference(list1[0], list1[1], con_topic, list1[3], list1[4], list1[5], list1[6])
                    return new_con
                except IndexError:
                    print('Hi Wake up, you just can enter the number from list')
        elif n1 == 4:
            flag1 = True
            while flag1:
                deadline_year = input('please enter new submit Year:  ')
                deadline_month = input('please enter new submit Month:  ')
                deadline_day = input('please enter new submit day:  ')
                if deadline_year and deadline_month and deadline_month:
                    if deadline_year.isdigit() and deadline_month.isdigit() and deadline_day.isdigit():
                        if len(deadline_year) != 4:
                            print('please enter  suitable Year')
                        elif int(deadline_year) > 2050:
                            print('Hi, you  set   ' + str(
                                deadline_year) + '   become deadline, nobody want to wait in this time')
                        elif int(deadline_month) > 12 or int(deadline_month) < 1:
                            print('Are you serious? Month must between 1-12')
                        elif int(deadline_day) > 31 or int(deadline_day) < 1:
                            print('Are you serious? day must between 1-31')
                        else:
                            flag1 = False
                            chair = user.last_name

                            new_con = Conference(list1[0], list1[1], list1[2], deadline_year, deadline_month,
                                                 deadline_day,
                                                 chair)
                            return new_con
                    else:
                        print('please enter right format')

    def display_review_evaluation(self, a_user):
        print("Select Paper for Review")
        with open("evaluation_db.txt", 'r') as eva_db:
            lines = eva_db.readlines()[1:]
            evaluation_list = []
            for line in lines:
                single_eva = line[:-1].split(', ')
                evaluation_list.append(single_eva)
        paper_list = []
        for index in range(len(evaluation_list)):
            if evaluation_list[index][4] == a_user.get_user_email():
                if evaluation_list[index][1] not in paper_list:
                    paper_list.append(evaluation_list[index][1])
                    print(len(paper_list), " - ", "Paper: ", evaluation_list[index][1], "| Author: ", evaluation_list[index][5])
        
        choice_flag = False
        while not choice_flag:
            try:
                paper_choice = int(input("Enter your choice: "))
                if paper_choice in range(len(paper_list)+1):
                    choice_flag = True
                else:
                    print("Wrong index. Try again.")
            except:
                print("Please only enter number.")

        paper_name = paper_list[paper_choice-1]
        for index in range(len(evaluation_list)):
            if evaluation_list[index][1] == paper_name:
                author_name = evaluation_list[index][5]
                print("Reviewer: ", evaluation_list[index][2], " | ", "Evaluation: ", evaluation_list[index][3])
        
        print("Choose your action forward: ")
        print("1 - Make final decision")
        print("2 - Return to the paper choice")
        print("3 - Return to chair page")

        choice_flage2 = False
        while not choice_flage2:
            choice = input("Enter your choice: ")
            if choice == "1":
                choice_flage2 = True
                self.display_final_decision(a_user, paper_name, author_name)
            elif choice == "2":
                choice_flage2 = True
                self.display_review_evaluation(a_user)
            elif choice == "3":
                choice_flage2 = True
                self.display_chair_page(a_user)
            else:
                print("Please only enter 1, 2, or 3.")
        
    def display_final_decision(self, a_user, paper_name, author_name):
        print("Do you want to accept or reject the paper? Enter the number below.")
        print("1 - Accept")
        print("2 - Reject")
        print("3 - Return to the previous page")
        
        choice_flag = False
        new_noti = Notification(paper_name, author_name, "Not Assign", datetime.datetime.now())
        while not choice_flag:
            choice = input("Enter your choice: ")
            if choice == "1":
                new_noti.save_noti("Accepted")
                print("Paper accepted. The notification has been sent to the author.")
                print("Jumping to the Chair page...")
                choice_flag = True
                self.display_chair_page(a_user)
            elif choice == "2":
                new_noti.save_noti("Rejected")
                print("Paper rejected. The notification has been sent to the author.")
                print("Jumping to the Chair page...")
                choice_flag = True
                self.display_chair_page(a_user)
            elif choice == "3":
                choice_flag = True
                self.display_review_evaluation(a_user)
            else:
                print("Invalid input. Try again.")

    def display_assign_page(self, a_user):
        print('These papers have not been assigned to review')
        list1 = self.new_system.get_paper_list()
        i = 1
        list2 = []
        for s in list1:
            if s[9] == 'Not Assigned':
                list2.append(s)
                print('(' + str(i) + ')', end='')
                for s1 in s:
                    print(s1 + '  ', end='')
                i = i + 1
                print('\n')
        num = input('enter number for which paper you want to assign')
        num = int(num)
        list3 = list2[num - 1]
        print('    ')
        flag = True
        while flag:
            s2 = self.new_system.show_user_list()
            for s4 in s2:
                for s3 in s4:
                    print(s3 + ' ', end='')
                print('\n')
            num1 = input('Select the first assigned reviewer serial number')
            num1 = int(num1)
            review1 = s2[num1 - 1][1]
            print(review1)

            num2 = input('Select the second assigned reviewer serial number')
            num2 = int(num2)
            review2 = s2[num2 - 1][1]
            print(review2)

            num3 = input('Select the third assigned reviewer serial number')
            num3 = int(num3)
            review3 = s2[num3 - 1][1]
            print(review3)
            if num1 == num2 or num1 == num3 or num2 == num3:
                print('You can not double assign same person')
            else:
                paper1 = Paper(list3[0], list3[1], list3[2], list3[3], list3[4], list3[5], list3[6], list3[7],
                               list3[8], list3[9], review1, review2, review3)
                with open('paper_db.txt', 'r')as f:
                    lines = f.readlines()[num]
                    list1 = lines.split(', ')
                    name = list1[0]
                with open('paper_db.txt', 'r') as filename:
                    lines = filename.readlines()
                with open('paper_db.txt', 'w') as file:
                    for line in lines:
                        if name in line:
                            continue
                        file.write(line)
                return paper1
                            
                

                

    # Author features
    def display_author_page(self, a_user):  # done
        self.display_title_box()
        a_author = AuthorFeatures()
        print("Please choose your actions as an Author.")
        print("1 - Upload a paper")
        print("2 - View notification")
        print("3 - Return to home page")
        choice_flag = False
        while not choice_flag:
            choice = input("Enter your choice from 1, 2 or 3: ")
            if choice == "1":
                choice_flag = True
                self.display_upload_paper(a_user, a_author)
            elif choice == "2":
                choice_flag = True
                self.display_view_notification(a_user, a_author)
            elif choice == "3":
                choice_flag = True
                self.display_home_page(a_user)
            else:
                print("Please only choose from 1 or 2.")

     # Author features
   
    def display_upload_paper(self, a_user, a_author):
        self.display_title_box()
        print("Please enter the paper information below.")
        
        path_flag = False
        print("Notice: filename can only have extension .txt or .pdf ")
        while not path_flag:
            file_name = input("Filename: ")
            path_flag = a_author.verify_filename(file_name)
            if path_flag:
                break
            else:
                print("Invalid file format. Please only upload .txt or .pdf.")
        
        paper_title = input("Paper title: ")
        paper_topics = self.display_topics_choosing()
        
        paper_keywords = []
        print("Notice: please enter the number fit your paper's keywords from the following list.")
        for index in range(len(self.new_system.list_of_keywords)):
            print(index+1," - ",self.new_system.list_of_keywords[index])
        
        flag_continue = False
        while not flag_continue:
            flag_kw = False
            while not flag_kw:
                choice = input("Keywords: ")
                flag_kw = a_author.verify_keywords(choice)
                if not flag_kw:
                    print("Invalid choice. Please only enter the number.")
            if flag_kw:
                paper_keywords.append(self.new_system.list_of_keywords[int(choice)-1])
            choice_continue = input("Do you want to add another keywords? Enter Y/N: ")
            if choice_continue != "Y" and choice_continue != "y":
                flag_continue = True

        author_names = a_user.get_user_email()

        flag_conference = False
        while not flag_conference:
            print("Choose the conference you want to submit your paper to. Only enter number.")
            conference_list = self.new_system.get_conference_list()
            for index in range(len(conference_list)):
                print(index+1, conference_list[index][0])
            try:
                conference_choice = int(input("Conference: "))
                flag_conference = a_author.verify_conference(conference_choice, conference_list)
                if flag_conference:
                    conference_name = conference_list[conference_choice-1][0]
                else:
                    print("Invalid choice. Try again.")
            except:
                print("Please only enter number.")

        current_time = datetime.datetime.now()
        paper_submit_year = current_time.year
        paper_submit_month = current_time.month
        paper_submit_day = current_time.day
            
        flag_choice = False
        while not flag_choice:
            choice_action = input("Choose your actions: 1 - Upload paper, 2 - Return to the Author page: ")
            if choice_action == "1":
                flag_choice = True
                flag_deadline = a_author.verify_paper_submit_deadline(conference_name, paper_submit_year, paper_submit_month, paper_submit_day)
                if flag_deadline:
                    paper_status = "Not Assigned"
                    new_paper = Paper(file_name, paper_title, paper_topics, paper_keywords, author_names, paper_submit_year, paper_submit_month, paper_submit_day, conference_name, paper_status, "N/A", "N/A", "N/A")
                    print("Uploaded successfully. Jump back to Author page...")
                    self.display_author_page(a_user)
                else:
                    paper_status = "Refused"
                    new_paper = Paper(file_name, paper_title, paper_topics, paper_keywords, author_names, paper_submit_year, paper_submit_month, paper_submit_day, conference_name, paper_status, "N/A", "N/A", "N/A")
                    print("Exceed submit deadline. Paper is uploaded and automatically refused.")
                    print("Jumping back to the Author page...")
                    self.display_author_page(a_user)
            elif choice_action == "2":
                flag_choice = True
                print("Upload cancled. Jump back to Author page...")
                self.display_author_page(a_user)
            else:
                print("Invalid input. Try again.")
  
    def display_view_notification(self, a_user, a_author):
        self.display_title_box()
        noti_list = a_author.get_notification_list()
        count = 0
        for single_noti in noti_list:
            if single_noti[1] == a_user.get_user_email():
                count += 1
                print("Notification ", count)
                print("Paper: ", single_noti[0])
                print("Author: ", single_noti[1])
                print("Paper status: ", single_noti[2])
                print("Status changed at: ", single_noti[3])
    
        print("Please choose your action forward: ")
        print("1 - Return to author page")
        print("2 - Return to home page")

        choice_flag = False
        while not choice_flag:
            choice = input("Enter your choice: ")
            if choice == "1":
                choice_flag = True
                self.display_author_page(a_user)
            elif choice == "2":
                choice_flag = True
                self.display_home_page(a_user)
            else:
                print("Invalid choice. Try again.")

    # Reviewer features
    def display_reviewer_page(self, a_user):  # sprint4
        self.display_title_box()
        new_reviewer = ReviewerFeatures()
        print("Please choose your actions below.")
        print("1 - Write evaluation")
        print("2 - Return to home page")
        choice_flag = False
        while not choice_flag:
            choice = input("Enter your choice from 1 or 2: ")
            if choice == "1":
                choice_flag = True
                self.display_reviewer_select_paper(a_user, new_reviewer)
            elif choice == "2":
                choice_flag = True
                self.display_home_page(a_user)
            else:
                print("Please only choose from 1 or 2.")

    def display_reviewer_select_paper(self, a_user, new_reviewer):
        self.display_title_box()
        print("Please select a paper you want to write evaluation first.")
        print("Notice: You should only enter the index number of listed paper.")
        paper_list = new_reviewer.get_review_paper_list(a_user.get_user_email())
        if paper_list == []:
            print("You are not assigned any paper. Jumping to the Reviewer page...")
            self.display_reviewer_page(a_user)
        for index in range(len(paper_list)):
            print(index+1, "-", paper_list[index])
        choice_flag = False
        while not choice_flag:
            try:
                choice = int(input("Enter your choice: "))
                choice_flag = new_reviewer.verify_paper_choice(choice, paper_list)
                if choice_flag:
                    print("Paper selected. Jumping to the Evaluation page...")
                    paper_name = paper_list[choice-1]
                    self.display_reviewer_write_evaluation(paper_name, a_user)
                else:
                    print("Invalid choice. Try again.")
            except:
                print("Please only enter number.")

    def display_reviewer_write_evaluation(self, paper_name, a_user):
        self.display_title_box()
        print("Paper chosen: ", paper_name)
        print("Reviewer: ", a_user.get_first_name(), a_user.get_last_name())
        
        evaluation_flag = False
        while not evaluation_flag:
            evaluation = input("Write your evaluation: ")
            if evaluation != "":
                evaluation_flag = True
            else:
                print("Empty input. Try again.")
        
        submit_flag = False
        while not submit_flag:
            choice = input("Do you want to submit your evaluation? Y/N: ")
            if choice == "Y" or choice == "y":
                submit_flag = True
                print("Evaluation submitted. Jumping back to Reviewer page...")
                new_evaluation = Evaluation(paper_name, a_user.get_user_email(), evaluation)
                self.display_reviewer_page(a_user)
            elif choice == "N" or choice == "n":
                submit_flag = True
                print("Submission canceled. Please choose your actions to forward.")
                print("1 - Rewrite evaluation")
                print("2 - Return to the Paper Selected page")
                print("3 - Return to the Reviewer page")
                choice2 = input("Enter your choice: ")
                if choice2 == "1":
                    self.display_reviewer_write_evaluation(paper_name, a_user)
                elif choice2 == "2":
                    self.display_reviewer_select_paper(a_user)
                elif choice2 == "3":
                    self.display_reviewer_page(a_user)
                else:
                    submit_flag = False
                    print("Invalid input. Try again.")
            else:
                submit_flag = False
                print("Invalid input. Try again.")

    # Admin features
    def display_admin_page(self, a_user):
        self.display_title_box()
        new_admin = AdminFeatures()
        print("Please choose your actions.")
        print("1 - Generate user report")
        print("2 - Generate conference report")
        print("3 - Return to home page")
        choice_flag = False
        while not choice_flag:
            choice = input("Enter your choice from 1 or 3: ")
            if choice == "1":
                choice_flag = True
                self.display_generate_user(a_user, new_admin)
            elif choice == "2":
                choice_flag = True
                self.display_generate_conference(a_user, new_admin)
            elif choice == "3":
                choice_flag = True
                self.display_home_page(a_user)
            else:
                print("Please only choose from 1 or 3.")

    def display_generate_user(self, a_user, new_admin):
        self.display_title_box()
        new_admin.generate_user_report()
        self.display_admin_return(a_user)

    def display_generate_conference(self, a_user, new_admin):
        self.display_title_box()
        new_admin.generate_conference_report()
        self.display_admin_return(a_user)

    def display_admin_return(self, a_user):
        print("Please choose your actions.")
        print("1 - Return to the admin page")
        print("2 - Return to home page")
        print("3 - Return to main page")
        choice_flag = False
        while not choice_flag:
            choice = input("Enter your choice from 1 to 3: ")
            if choice == "1":
                choice_flag = True
                self.display_admin_page(a_user)
            elif choice == "2":
                choice_flag = True
                self.display_home_page(a_user)
            elif choice == "3":
                choice_flag = True
                self.display_main_page()
            else:
                print("Invalid input. Try again.")

    # Additional display (for convienience)
    def display_topics_choosing(self):  # used in registration, reviewer, paper, conference to choose topics
        print("Notice: please enter the number fit your interest area from the following list.")
        topic_list = self.new_system.list_of_topics
        for index in range(len(topic_list)):
            print(index+1, " - ", topic_list[index])

        flag_topics = False
        while not flag_topics:
            choice = input("Interest area: ")
            flag_topics = self.new_system.verify_register_topics(choice)
            if not flag_topics:
                print("Invalid topics. Please choose from the list.")
        if flag_topics:
                interest_area = topic_list[int(choice)-1]
        return interest_area


if __name__ == "__main__":
    conference_management_system = UserInterface()
    conference_management_system.display_main_page()