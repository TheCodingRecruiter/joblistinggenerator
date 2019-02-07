class Hiring:
    
    def __init__(self, title, skills, location):
        self.title = title
        self.skills = skills
        self.location = location
    
    def listjob(self):
        print('We have a current job opening for a ' + str(self.title) + ' who is skilled in ' + str(self.skills) + '. The position is located in ' + str(self.location) + '.  Apply today if you are interested' )
    
pythondev = Hiring('Python Dev', 'Django/Flask, Machine Learning', 'Des Moines, IA')
javadev = Hiring('Java Developer', 'Hibernate/Spring, AWS, Rest', 'Dallas, TX')

pythondev.listjob()
javadev.listjob()
    
    
