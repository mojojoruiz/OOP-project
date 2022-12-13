class Laboratory:

    def __init__(self, lab_name, cost):
        self.lab_name = lab_name
        self.cost = cost

    def formatLabInfo(self):
        return f"{self.lab_name}_{self.cost}"

    def addLabToFile(self):
        f = open("files\laboratories.txt", 'a')
        f.write(self.formatLabInfo())
        f.close()

    def enterLaboratoryInfo(self):
        lab_name = input("Enter Laboratory facility:")
        cost = input("Enter Laboratory cost:")
        lab_name = Laboratory(lab_name, cost)
        

    def readLaboratoriesFile(self):
        with open('files\laboratories.txt') as f:
            labList = [line.rstrip('\n') for line in f]
        f.close()
        return labList
        

    def displayLabsList(self):
        print("Name \t\t\tCost \n")
        for i in range(len(self.readLaboratoriesFile())):
            if i != 0:
                word = self.readLaboratoriesFile()[i].split("_")
                name = word[0]
                cost = word[1]
                print(name + " \t\t\t" + cost + "\n")

    def writeListOfLabsToFile(self):
        with open('files\laboratories.txt') as f:
            f.write(self.readLaboratoriesFile())



class Management:

    def displayMenu(self):
        while 1 == 1:
            print("Welcome to Alberta Hospital (AH) Managment system")
            num = int(input("Select from the following options, or select 0 to stop:"))
            if num == 0:
                break
            elif num == 1:
                #need to talk with group member who made the doctor class before I can finish this
                break
            elif num == 2:
                #need to talk with group member who made the facilities class before I can finish this
                break
            elif num == 3:
                lab5 = Laboratory('lab5', 250)
                numLab = 1
                while 1 == 1:
                    numLab = input("Laboratories Menu:\n1 - Display laboratories list\n2 - Add laboratory\n3 - Back to the Main Menu\n")
                    if numLab == 1:
                        lab5.displayLabsList()
                    elif numLab == 2:
                        lab5.enterLaboratoryInfo()
                    elif numLab == 3:
                        break

#user = Management()
#user.displayMenu()
#I need my groups work and input to be able to finish the display menu.
#Because of this, in order to run my code I have the following lines for testing purposes.

input("Laboratories Menu:\n1 - Display laboratories list\n2 - Add laboratory\n3 - Back to the Main Menu\n\n")
lab5 = Laboratory('lab5', 250)
lab5.displayLabsList()
input("Back to previous menu\nLaboratories Menu:\n1 - Display laboratories list\n2 - Add laboratory\n3 - Back to the Main Menu\n\n")
input("Enter Laboratory facility:\n")
input("Enter Laboratory cost:\n")
lab5.addLabToFile()
input("Back to previous menu\nLaboratories Menu:\n1 - Display laboratories list\n2 - Add laboratory\n3 - Back to the Main Menu\n\n")
lab5.displayLabsList()
input("Back to previous menu\nLaboratories Menu:\n1 - Display laboratories list\n2 - Add laboratory\n3 - Back to the Main Menu\n\n")