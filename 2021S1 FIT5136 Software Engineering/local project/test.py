import datetime
def get_conference_list():
    with open("conference_db.txt", 'r') as conference_db:
        lines = conference_db.readlines()[1:]
        conference_list = []
        for line in lines:
            single_conference = line[:-1].split(',')
            conference_list.append(single_conference)
    return conference_list

def generate_conference_report():
    conference_list = get_conference_list()
    for conference in conference_list:
        print("Conference name" + conference[0])
        print("Conference title" + conference[1])
        print("Conference topics: " + conference[2])
        submit_deadline = datetime.datetime(int(conference[3]), int(conference[4]), int(conference[5]))
        print("Paper submit deadline: " + str(submit_deadline))
        print("Conference chair" + conference[6])
        print("Accepted paper: " + str(len(conference) - 7))
        for item in conference[7:]:
            print(item)
        print("\n")

generate_conference_report()