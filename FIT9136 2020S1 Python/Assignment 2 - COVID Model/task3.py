"""
Date Created: 2020-06-01
Last Modified: 2020-06-07
"""
# Test scenario A: matches. Because the meeting probability is pretty high and 29 will generate a high viral load.
# Test scenario B: matches. Tested a few times, each time the result was quite different. So the result is really
# unpredictable.
# Test scenario C: matches. There will be a really small population infected but soon the plot is
# flatter since low chance of meeting, low chance of getting infected.

from task2 import *
from matplotlib import pyplot as plt


# to print the simulation result and plot the curve. arguments: days, meeting_probability, patient_zero_health
def visual_curve(days, meeting_probability, patient_zero_health):

    # call run_simulation() to generate a list of daily contagious number
    daily_contagious = run_simulation(days, meeting_probability, patient_zero_health)

    # print the daily number
    for n in range(len(daily_contagious)):
        print("Day "+ str(n+1) + ": " + str(daily_contagious[n]))

    # draw a plot using matplotlib
    # x = [0, 1, 2, ..., days-1]
    # y = daily_contagious
    x_axis = [item for item in range(days)]
    y_axis = daily_contagious
    plt.plot(x_axis, y_axis)
    plt.ylabel("Daily number of contagious people")
    plt.xlabel("Days")
    plt.show()


if __name__ == '__main__':
    test_days = int(input("Please enter an integer number for days to simulate the situation: "))
    test_probability = float(input("Please enter a float number from 0 to 1 for meeting probability: "))
    test_patient_zero = float(input("Please enter a float number for patient zero health point: "))
    visual_curve(test_days, test_probability, test_patient_zero)