"""
@description:


#star date: 5.1
#last modified: 5.2

# Read data and calculate the stock and revenue at the end of a year

"""
from typing import Dict

initial_rrp = 705 # initial RRP
initial_dis = 36 # initial distribution number

# create the function that read data in dictionary type
def read_data():
    f = open("AU_INV_START.txt.txt", 'r')
    lines = f.read().splitlines()
    # read file and split lines without '\n'
    # citing:https://stackoverflow.com/questions/3277503/how-to-read-a-file-line-by-line-into-a-list
    start_info = {'start_year': lines[0], 'start_stock': lines[1], 'start_revenue': lines[2]}
    return start_info

# calculate total stock remaining and total revenue of a single year's cycle
def cal_stock_revenue(which_year):

    # read data by using read_data()
    initial_info = read_data()

    # if it is a leap year
    if which_year % 4 == 0 and  which_year %100 != 0:
        feb_days = 29
    elif which_year % 400 == 0:
        feb_days = 29
    else:
        feb_days = 28

    # if it is a crisis year
    if (which_year - 2009) % 11 <= 2 and which_year > 2003:
        # 1st year
        if (which_year - 2009) % 11 == 0:
            # rrp from Jan to Feb
            rrp_1t2 = initial_rrp * 1.1 # crisis causes increase 10%
            # distribution from Jan to Feb
            dis_1t2 = int(initial_dis * 0.8) # crisis causes decrease 20%
         # 2nd year
        elif (which_year - 2009) % 11 == 1:
            # rrp from Jan to Feb
            rrp_1t2 = initial_rrp * 1.05 # crisis causes increase 5%
            # distribution from Jan to Feb
            dis_1t2 = int(initial_dis * 0.9) # crisis causes decrease 10%
        # 3rd year
        elif (which_year - 2009) % 11 == 2:
            # rrp from Jan to Feb
            rrp_1t2 = initial_rrp * 1.03 # crisis causes increase 3%
            # distribution from Jan to Feb
            dis_1t2 = int(initial_dis * 0.95) # crisis causes decrease 5%
    else:
        # rrp from Jan to Feb
        rrp_1t2 = initial_rrp  # no crisis causes increase 3%
        # distribution from Jan to Feb
        dis_1t2 = int(initial_dis) # no crisis causes decrease 5%

    rrp_3t6 = rrp_1t2 / 1.2 # after peak season
    rrp_7t10 = rrp_3t6 * 1.05 # financial year inflation
    rrp_11t12 = rrp_7t10 * 1.2 # peak season begin
    dis_3t6 = int(dis_1t2 / 1.35) # after peak season
    dis_7t10 = int(dis_3t6 * 1.1) # financial year inflation
    dis_11t12 = int(dis_7t10 * 1.35) # peak season begin

    # quantity in each month
    qty1 = dis_1t2 * 31
    qty2 = dis_1t2 * feb_days
    qty3 = qty5 = dis_3t6 * 31
    qty4 = qty6 = dis_3t6 *30
    qty7 = qty8 = qty10 = dis_7t10 * 31
    qty9 = dis_7t10 * 30
    qty11 = dis_11t12 * 30
    qty12 = dis_11t12 *31




# write data function
def write_data():
