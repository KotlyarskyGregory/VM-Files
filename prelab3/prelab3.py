class Robot:
    def __init__(self, id_number, status, location):
        self.id_number = id_number
        self.status = status
        self.location = location

    def __str__(self):
        return f"ID number: {self.id_number}\nStatus: {self.status}\nLocation: {self.location}"

    def moveBot(self, newLocation):
        self.location = newLocation

    def changeStatus(self):
        if (self.status == "offline") :
            self.status = "online"
        else:
            self.status = "offline"

        


robot1 = Robot(1234, "online", "A3")

print(f"{robot1}\n")

robot1.moveBot("A5")
robot1.changeStatus()

print(f"{robot1}\n")