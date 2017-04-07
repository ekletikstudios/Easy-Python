# Python libraries...
import array
import datetime
from random import *

"""
    Code by: Leo Neto
    This file contains the blueprint of a Student object.

    Useful information before you proceed:

    TOKENS and GeneratedID():
    Tokens will be used to generate IDs for the students.
    Student ID must be 10-digit long. IDs must start with either L, Z, R, or S.
    CriarID() is the method responsible for checking and randomizing the tokens.
    The structrue and logic for creating student IDs is as follows:
    (ltoken) + (lengthOfName) + (ttoken) + (2 x mtoken) + (ztoken) + (dtoken)
    i.e.   R 10 74 MP 5 EN

    Info():
    This class has a Info() method to be used to output all non-default information about any
    instance of the Student class. If any property within the object is left "Unspecified" or
    left to its default value, such information will be omitted while outputing to stdout. All information is,
    however, output when the objects are saved.

    Sample Output -------------
    Nome: Jonathan Daniel
    Tel.: 555 555 5555
    Email: jonathandaniel@uluz.edu
    Course: Computer Engineering
    Speciality: Microprocessors
    Enrollment: January 2015
    Graduation: December de 2019
    ID: L3014UI9MZ
    ----------------------------

    CHANGE:
    These set of methods will allow for the specified parameters to be changed.

    MudarEmail():
    EmailId() will check the database of students for username@schooldomain.edu matches.
    If the username is taken, a new email should be assigned to the user.

    Salvar():
    Every instance of the Student class can be saved to a file using the Salvar() method.
    The output of every save is stored in a file called students.lz. Note that the file is open in -a append mode.

    Logs:
    This set of methods will save information about specific activities on a dedicated file for future refence.

    ReportarHack():
    Much like the logs, this method outputs detailed information about an attempted change in StudentID or EmailID for a given user.
    The output records the date of the incident, YY-MM-DD, along with information about the user who attempted the change,
    as well as the permission codes and tokens utilized for the hack.

"""

# _____Start of Student Class________________

class Student(object):
    # ___________Properties__________________
    ltoken = ['L','Z','R','S']                                                          # Code: 1
    mtoken = ['M','N','P','W','Q','D','F','C','B','T','V','X','Y']                      # Code: 2
    dtoken = ['EN','CI','LG','CM','ST','FI','EC']                                       # Code: 3
    ttoken = [30,42,16,81,61,72,15,50,38,49,14,55,74,62,24,64,32,93,95,59,44,11,10,77]  # Code: 4
    ztoken = [0,1,2,3,4,5,6,7,8,9]                                                      # Code: 5
    master = ['A','G','H','J','K','U','E','I']                                          # Code: 6

    #____________ Methods____________________

    # Student Class Constructor
    def __init__(self, firstname, lastname):
        object.__init__(self)
        self.name = firstname.capitalize()
        self.surname = lastname.capitalize()
        self.email = self.name.lower() + self.surname.lower() + '@uluz.edu'
        self.tel   = 0                       # NO output if default value
        self.course = "Undefined"            # NO output if default value
        self.speciality = "Undefined"        # NO output if default value
        self.enrollment = 11999              # No output if default value
        self.graduation = 11999              # No output if default value
        self.id = self.GenerateID()
        self.createdon = datetime.date.today()
        self.LogNewStudent()

    def FullName(self):
        return '{} {}'.format(self.name, self.surname)

    def LengthOfName(self):
        length = len(self.FullName())-1
        if(length<10):
            variation = 10-length
            length=length + variation
        return length

    def GenerateID(self):
        range  = len(self.ltoken)
        block1 = str(self.ltoken.pop(randrange(range)))
        block2 = str(self.LengthOfName())

        range  = len(self.ttoken)
        block3 = str(self.ttoken.pop(randrange(range)))

        range  = len(self.mtoken)
        block4 = str(self.mtoken.pop(randrange(range)))

        range  = len(self.ztoken)
        block5 = str(self.ztoken.pop(randrange(range)))

        range  = len(self.dtoken)
        block6 = str(self.dtoken.pop(randrange(range)))

        id = block1 + block2 + block3 + block4 + block5 + block6
        return id # This is a massive ID string...

    def GenerateEmail(self):
        self.rt = randint(0,99)
        self.rt = str(self.rt)
        self.email = self.name.lower() + self.surname.lower() + self.rt + '@uluz.edu'
        print(self.email)

    def Who(self):
        print("Name: {}".format(self.FullName()))
        if(self.tel!=0):
            print("Tel.: {}".format(self.tel))
        print("Email: {}".format(self.email))
        if(self.course!="Undefined"):
            print("Course: {}".format(self.course))
        if(self.speciality!="Undefined"):
          print("Speciality: {}".format(self.speciality))
        if(self.enrollment!=11999):
            print("Enrollment: {}".format(self.enrollment))
        if(self.graduation!=11999):
            print("Graduation: {}".format(self.graduation))
        print("ID: {}".format(self.id))

    def ChangeCourse(self, c):
        self.course = c
        # return
        self.LogNewCourse()

    def ChangeSpeciality(self, e):
        self.speciality = e

    def ChangeEnrollment(self, data):
        self.enrollment = data

    def ChangeGraduation(self, grad):
        self.graduation = grad

    def ChangeID(self):
        # Only run with a password.
        if(self.SystemPermission()):
            self.id = self.GenerateID()
        else:
            self.ReportHack("ID")

    def ChangeEmailID(self):
        if (self.SystemPermission()):
            self.email = self.GenerateEmail()
        else:
            self.ReportHack("Email")

    def Save(self):
        with open('students.lz', 'a') as file:

            if file != "":
                file.write("\n") # adding space between each student entry
            file.write("{}\n".format(self.name))
            file.write("{}\n".format(self.surname))
            file.write("{}\n".format(self.email))
            file.write("{}\n".format(self.course))
            file.write("{}\n".format(self.speciality))
            file.write("{}\n".format(self.enrollment))
            file.write("{}\n".format(self.graduation))
            file.write("{}\n".format(self.id))
            file.close()

    def ReportHack(self, systemInfo):
        print("Permission denied\n")

        thisDate = datetime.date.today()
        thisHour = thisDate.toordinal()

        with open('IDHack.lz', 'a') as file:
            file.write("ERROR -2P: The user {}, with ID {}, tried to change their {}.\n".format(self.FullName(),self.id,systemInfo))
            file.write("The token used was: '{}'.\n".format(self.UsedToken()))
            file.write("This incident happened on {}.\n".format(thisDate))
            file.close()



    def LogNewStudent(self):
        with open ('ChangeLog.lz', 'a') as file:
            thisDate = datetime.date.today()
            file.write('{} was added on {}.\n'.format(self.FullName(),thisDate))
            file.close()

    def LogNewID(self):
        with open ('ChangeLog.lz', 'a') as file:
            thisDate = datetime.date.today()
            file.write('New ID generated for {} on {}.\n'.format(self.FullName(),thisDate))
            file.close()

    def LogNewCourse(self):
        with open ('ChangeLog.lz', 'a') as file:
            thisDate = datetime.date.today()
            file.write('Course, {}, added to {} on {}.\n'.format(self.course,self.FullName(),thisDate))
        file.close()

    def LogNewSpeciality(self):
        with open ('ChangeLog.lz', 'a') as file:
            thisDate = datetime.date.today()
            file.write('Speciality, {}, added to {} on {}.\n'.format(self.course,self.FullName(),thisDate))
        file.close()



    def SystemPermission(self):
        code = input("Code: ")
        self.SetToken(code)
        if(code == "UEI644"):
            permission = True
        else:
            permission = False
        return permission

    def SetToken(self, token):
        self.__usedToken = token
    def UsedToken(self):
        return self.__usedToken

######## End of Student Class_______________________



def main():
    firstname = input("First name: ")
    lastname  = input("Last name: ")
    person    = Student(firstname, lastname)
    person.Who()


if __name__ == "__main__":
    main()
