#Aliya Tyshkanbayeva
#Homework3

def getYear(date):
    return date // 10000

#Given integer date returns
#the month as an integer
def getMonth(date):
    return ((date // 100) % 100)

#Given integer date returns
#the day as an integer
def getDay(date):
    return date % 100

# function to read the given file and output the list of lists
# with dates and temps
def readNOAA(filename):
    dateList = []
    file = open(filename)
    for line in file:
        splitlist = []
        if(line[0] == "G"):
            l = line.split()
            splitlist.append(int(l[4]))
            splitlist.append(int(l[6])) 
            dateList.append(splitlist)
    file.close()
    return dateList


def isValidDay(date):
    
    year = getYear(date)
    month = getMonth(date)
    day = getDay(date)

    monthsWith31 = [1, 3, 5, 7, 8, 10, 12]
    monthsWith30 = [4, 6, 9, 11]
    
    if(month in monthsWith31):
        return(day >= 1 and day <=31)
    elif(month in monthsWith30):
        return(day >= 1 and day <=30)
    elif(month == 2 and isLeap(year)):
        return(day >=1 and day <=29)
    elif(month == 2 and not isLeap(year)):
        return(day >=1 and day <= 28)
    else:
        return False


def isValidDate(date):
    return (isInRange(date) and isValidMonth(date) and isValidDay(date))

def isInRange(date):
    return (date >= 17520914 and date <= 20180117)

def isValidMonth(date):
    month = getMonth(date)
    return (month >= 1 and month <= 12)


# printing out the early spring years, meaning 7 consecutive days 
def listEarlySpringYears(dateList):
    yearList=[]
    counter = 0    
    for i in dateList:
        if(i[1] >= 32 and isInSpringRange(i[0]) == True):
            counter+=1
        else:
            counter = 0
        if(counter >= 7):
            yearList.append(getYear(i[0]))
    for each in yearList:
        if(isValidDate(each) != True):
            yearList.remove(each)
    yearList = set(yearList)
    yearList = list(yearList)
    return yearList
                       
   
def isInSpringRange(date):
    if(getMonth(date) == 3 or getMonth(date) == 4 or getMonth(date) == 5):
        return True

def storeYears(filename, yearList):
    file = open(filename, 'w')
    for year in yearlist:
        file.write(str(year) + '\n')
    file.close()
    
def main():
    espYears = readNOAA("temps.txt")
    print(listEarlySpringYears(espYears))


main()
