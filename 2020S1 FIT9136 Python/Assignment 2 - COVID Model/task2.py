"""
Date Created: 2020-06-01
Last Modified: 2020-06-07
"""
# Task 2: Inherit Person to create Patient. Similar method to load_people() to write load_patient().


from task1 import *
from random import random


# inherit Person to create Patient
class Patient(Person):

    # initialize Patient. inherit methods from Person.
    def __init__(self, first_name, last_name, health):
        super().__init__(first_name, last_name)  # inherit all the methods from Person
        # cite from https://www.w3schools.com/python/python_inheritance.asp
        self.health = health

    # get the Patient's health point. return a float number.
    def get_health(self):
        return self.health

    # set the Patient's health point. check the limitation [0, 100].
    def set_health(self, new_health):
        # an if/else to ensure that the health point will not exceed.
        if 0 <= new_health <= 100:
            self.health = new_health
        elif new_health < 0:
            self.health = 0
        else:
            self.health = 100

    # see if a Patient is contagious. return True if contagious, False if not.
    def is_contagious(self):
        # use round_precise() function to round float to integer
        # since round() function will have a bank round issue
        hp = round_precise(self.get_health())
        if 0 <= hp <= 49:
            return True
        else:
            return False

    # contagious people infect others.
    def infect(self, viral_load):
        hp_before = self.get_health()
        hp_after = 0
        if 0 <= hp_before <= 29:
            hp_after = hp_before - (0.1 * viral_load)
        elif 29 < hp_before < 50:
            hp_after = hp_before - (1.0 * viral_load)
        else:
            hp_after = hp_before - (2.0 * viral_load)
        self.set_health(hp_after)  # set_health() will automatically check the lower limit for 0.

    # sleep to get health point +5
    def sleep(self):
        new_point = self.get_health() + 5
        self.set_health(new_point)  # set_health() will automatically check the upper limit for 100.


# this is a more precise function to round float number. .5 will always round up to the next upper/lower int.
# this function avoid bank round issue so that like 46.5 will be rounded to 47 rather than 46.
# but actually we don't need this to do this task since the only situation we need a round() is to comparing HP with 49.
# and 49 is an odd number thus don't have bank round issue.
def round_precise(number):
    if int(number) % 2 != 0:
        return round(number)
    else:
        int_number = int(number)
        if number < 0:
            new_number = int_number - number
        else:
            new_number = number - int_number
        if new_number == 0:
            return number
        elif new_number < 0.5:
            return int_number
        else:
            if number < 0:
                return int_number-1
            else:
                return int_number+1


# inherit the linear search from task1.
def linear_search(the_list, name):  # define a linear search to find the position of specific name
    for n in range(len(the_list)):
        if the_list[n].get_name() == name:
            return n
    return False


# generate the outcome based on the meeting probability. return T/F for whether meeting happens.
def is_visited(probability):
    rand = random()
    if rand < probability:
        return True
    else:
        return False


# use argument health to calculate and return viral load
def cal_viral_load(health):
    return 5 + ((health - 25) ** 2) / 62


# the whole simulation process. return a list of daily number of contagious people.
def run_simulation(days, meeting_probability, patient_zero_health):

    # load patients and assign HP = average 75 to every Patient in the list
    # set the first person as patient zero by assigning patient_zero_health to him/her
    patients = load_patients(75)
    patients[0].set_health(patient_zero_health)
    contagious_number = []

    # Each day
    for day in range(days):

        # meetings in a day
        for patient in patients:  # each person
            for friend in patient.get_friends():  # each friend of that person
                if is_visited(meeting_probability):
                    if patient.is_contagious():
                        viral_load = cal_viral_load(patient.get_health())
                        friend.infect(viral_load)
                    if friend.is_contagious():
                        viral_load = cal_viral_load(friend.get_health())
                        patient.infect(viral_load)

        # the reason why we restart a loop is: we should iterate all patients then call is_contagious() to check.
        contagious_current = 0
        for patient in patients:
            # count the number of current contagious people after all meeting
            if patient.is_contagious():
                contagious_current += 1

            # each person has some sleep.
            patient.sleep()

        # record contagious number in each day
        contagious_number.append(contagious_current)

    return contagious_number


# same as load_people() but with another arguement initial health. return a list of Patients.
def load_patients(initial_health):
    try:
        open_file = open("a2_sample_set.txt", 'r')  # open file

        # patients_list = [Patient1, Patient2, ...]
        patients_list = []
        for line in open_file.readlines():
            split_line = line.strip("\n").split(": ")
            patient_name = split_line[0].split()
            patients_list.append(Patient(patient_name[0], patient_name[1], initial_health))

        open_file.seek(0, 0)  # cite from https://pscustomobject.github.io/python/Python-Reset-Read-Write-Position/

        # inherit add_friend() to add Friends to Patients
        patient = 0
        for line in  open_file.readlines():
            split_line = line.strip("\n").split(": ")
            friend_name = split_line[1].split(", ")
            for n in range(len(friend_name)):
                m = linear_search(patients_list, friend_name[n])
                patients_list[patient].add_friend(patients_list[m])
            patient += 1

        return patients_list

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

    test_result_1 = run_simulation(15, 0.8, 49)
    print(test_result_1)
    print(len(test_result_1))

    print("\n")

    test_result_2 = run_simulation(40, 1, 1)
    print(test_result_2)
    print(len(test_result_2))


