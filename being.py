def job_type(job):
    if (job <= 25 or (job >= 4001 and job <= 4049)):
        return "player"
    elif (job >= 46 and job <= 1000):
        return "npc"
    elif (job > 1000 and job <= 2000):
        return "monster"
    elif (job == 45):
        return "portal"

class BeingManager:
    def __init__(self):
	self.container = {}

    def findId(self, name):
	for i in self.container:
	   if self.container[i].name == name:
		return i
	return -10

class Being:
    def __init__(self, being_id, job):
        self.id = being_id
	self.name = ""
	self.x = 0
	self.y = 0
	self.action = ""
	self.job = job
	self.target = 0
	self.type = job_type(job)
