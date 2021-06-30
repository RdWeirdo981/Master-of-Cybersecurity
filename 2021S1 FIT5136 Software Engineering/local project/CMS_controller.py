

def validate_conference_name(name,title,topic):
    if not name:
        print('conference name can not be null')
        return False
    elif not title:
        print('conference title can not be null')
        return False
    elif not topic:
        print('conference topic can not be null')
        return False
    else:
        
        return True


def validate_conference(deadline):
    if not datetime:
        print('deadline can not be null')
        return False
    elif len(deadline) == 12:
        print('You should follow the right fomat to enter')
        return False
    elif not deadline.isdigit():
        print('You can not enter other types except number')
        return False
    else:
        return True 

def validate_chair(chair,chair_list):
    if not chair:
        print('conference chair can not be null ')
        return False
    elif chair not in chair_list:
        print('conference is no has this chair')
        return False
    else:
        return True


def accepted_paper(paper,conference):
    conference.conference_accepted_paper.append(paper)
    return True 

    



        


    
        


