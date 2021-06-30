class conference:
    def __init__(self,conference_name,conference_title, conference_topics,conference_submit_deadline,conference_chair,):
        self.set_conference_name = conference_name
        self.set_conference_title = conference_title
        self.set_conference_topics = conference_topics
        self.set_conference_submit_deadline = conference_submit_deadline
        self.set_conference_chair = conference_chair
        self.conference_accepted_paper = []
    
    def get_conference_name(self):
        return self.conference_name
    
    def get_conference_title(self):
        return self.conference_title
    
    def get_conference_topics(self):
        return self.conference_topics
    
    def get_conference_submit_deadline(self):
        return self.conference_submit_deadline

    def get_conference_chair(self):
        return self.conference_chair
        

    def get_conference_accepted_paper():
        return self.get_conference_accepted_paper
    
    def set_conference_name(name):
        self.conference_name = name
        return True
        
    def set_conference_title(title): 
        self.conference_title = title
        return True

    def set_conference_topics(topics): 
        self.conference_topics = topics
        return True

    def set_conference_submit_deadline(datetime): 
        self.datetime = datetime
    
    def set_conference_chair(chair):
        self.get_conference_chair = chair
    
    def set_conference_accepted_paper(paper): 
        self.get_conference_accepted_paper = paper


    


