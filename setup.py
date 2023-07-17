#clear the file of any previous settings
def initWriteToFile():
    x = open("data/private.py", "w")
    x.write('')
# write to file function, everything must be preceise
def writetofile(key,value, timephase):
    x = open("data/private.py", "a")
    x.write(key)
    x.write(" = ")
    # timeToWait should not be written with "" in the file and boolean values
    if timephase == "int":
        x.write(value)
        x.write('\n')
    if timephase == "str":
        x.write('"')
        x.write(value)
        x.write('"\n')
    if timephase == "bool":
        x.write(value)
        x.write('\n')
    x.close()
#time to wait
def getTimeToWait():
    timetowait= input("how much time to wait? (seconds) \n")
    writetofile(key="timetowait",value=timetowait, timephase="int")
#APIkey
def getAPIKey():
    APIKey= input("Please input APIKey \n")
    writetofile(key="apikey", value=APIKey, timephase="str")
#reciever
def getRecieverAdress():
    recieveradress= input("What is the recievers adress ?")
    writetofile(key="recieveradress", value=recieveradress, timephase="str")
def getSignUpEmail():
    signupemail= input("What is the sign up email ?")
    writetofile(key="signupemail", value=signupemail, timephase="str")
#Terminal Activation
def getTerminalActivation():
    TerminalActivate = str(input("Would you like The terminal to print The info? (Y/n)")).strip().lower()
    match(TerminalActivate):
        case "":
            writetofile(key="TerminalActivated", value="True", timephase="bool")
        case "yes":
            writetofile(key="TerminalActivated", value="True", timephase="bool")
        case "y":
            writetofile(key="TerminalActivated", value="True", timephase="bool")
        case "no" :
            writetofile(key="TerminalActivated", value="False", timephase="bool")
        case "n" :
            writetofile(key="TerminalActivated", value="False", timephase="bool")
#Main
def getInformation():
        initWriteToFile()
        getTimeToWait()
        getAPIKey()
        getSignUpEmail()
        getRecieverAdress()
        getTerminalActivation()
        #here you may add a check funtion that checks the file
        print("Settings have been modified, Please run 'run.py'")
getInformation()
#Init
