"""
Date Created: 2020-06-01
Last Modified: 2020-06-07
"""
# Task 1 is mainly for creating Person class and load_people() function.


# create the Person class
class Person:

    # initialize the Person class. arguments: first_name, last_name.
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name
        self.friend_list = []  # f_l = [Friend1, Friend2, ...]

    # add friend to this Person. argument: another Person class as the Person's friend.
    def add_friend(self, friend_person):
        self.friend_list.append(friend_person)

    # return a string as the Person's fullname
    def get_name(self):
        full_name = self.first_name + " " + self.last_name
        return full_name

    # return a list of the Person's Friends
    def get_friends(self):
        return self.friend_list


# define a linear search to find the position of specific name.
# if found: return the position. if not, return False.
def linear_search(the_list, name):
    for n in range(len(the_list)):
        if the_list[n].get_name() == name:
            return n
    return False


# read the sample file and assign these names to Person class. return a list of Person.
def load_people():
    try:
        open_file = open("a2_sample_set.txt", 'r')  # open file

        # convert each line into one list
        # that contains 2 sublist: person_name and friend_name
        # person_name: ['first_name', 'last_name']
        # friend_name: ['f1_fullname', 'f2_fullname', ...]

        # person_list to create a list containing Person
        person_list = []
        for line in open_file.readlines():
            split_line = line.strip("\n").split(": ")
            person_name = split_line[0].split()
            person_list.append(Person(person_name[0], person_name[1]))  # person_list = [Person1, Person2, ...]

        # return to the beginning of the file to read through Friends
        open_file.seek(0, 0)  # cite from https://pscustomobject.github.io/python/Python-Reset-Read-Write-Position/

        # call addFriend() to build the connection
        # linear search to find the where friend is
        person = 0  # star from the first person
        for line in open_file.readlines():
            split_line = line.strip("\n").split(": ")
            friend_name = split_line[1].split(", ")
            for no in range(len(friend_name)):
                member = linear_search(person_list, friend_name[no])
                person_list[person].add_friend(person_list[member])
            person += 1

        return person_list

    except FileNotFoundError:
        print("Could not find a2_sample_set.txt")
        return False
    except IOError:
        print("Could not open a2_sample_set.txt")
        return False
    except:
        print("Unknown Error.")
        return False
    finally:
        try:
            open_file.close()
        except IOError:
            print("Could not close a2_sample_set.txt")
        except:
            print("Unknown Error for closing the file.")


if __name__ == '__main__':

    new_list = load_people()

    # Now we have:
    # new_list = [Person1, Person 2, ...]

    if new_list:  # only new_list is created can the below code run

        # load_people() should return a list
        print("load_people() type: ", type(new_list))
        # get_name() should return a string
        print("get_name() type: ", type(new_list[0].get_name()))
        # get_friends() should return a list
        print("get_friends() type: ", type(new_list[0].get_friends()),"\n")

        for n in range(len(new_list)):

            # Print 200 persons' fullname
            print("Person ", n + 1, ": ", new_list[n].get_name())

            # Print each person's friends
            f_list = new_list[n].get_friends()  # f_list = [Friend1, Friend2, ...]
            for m in range(len(f_list)):
                print("Friend ", m + 1, ": ", f_list[m].get_name())
            print("\n")

        print("Creation success.")

    else:
        print("Creation failed.")
