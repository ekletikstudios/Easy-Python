
# GLOBAL
listAsIs = []
listByLastName = []
listByFirstName = []

def readAndSaveTo(filename, list):
    """
    desc: reads lines from a file and appends them to an array.
    param: void
    return: void
    """
    with open (filename, 'r') as file:
        for name in file:
            if name not in list:
                list.append(name)
    file.close()



def writeListToFile(list, filename):
    """
    desc: Opens or creates a file and writes to it.
    param: list, an array
    return: void
    """
    with open (filename, 'r+') as file:
        for name in list:
            if name not in file:
                file.write(name)
    file.close()


def sortByLastName(listBeingSorted, listBeingSaved):
    for name in listBeingSorted:
        name = name.split()
        firstname = name[0]
        lastname = name[1]
        fullname = "{}, {}\n".format(lastname, firstname)
        listBeingSaved.append(fullname)

def sortByFirstName(listBeingSorted, listBeingSaved):
    listBeingSaved = sorted(listBeingSorted)


def performSortingRoutine():
    raw = "studentsRawData.ah"
    lastNameSorted = "studentsByLastName.ah"
    firstNameSorted = "studentsByFirstName.ah"

    readAndSaveTo(raw, listAsIs)
    sortByLastName(listAsIs, listByLastName)

    # readAndSaveTo(raw, listByFirstName)
    # sortByFirstName(listAsIs, listByFirstName)
    # writeListToFile(listByFirstName, firstNameSorted)

    writeListToFile(listByLastName, lastNameSorted)

performSortingRoutine()
