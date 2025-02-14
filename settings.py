

proxy = '127.0.0.1:20001'
dataFile = 'workDB.xlsx'
amountOfThreads = 2
proxyPorts = [20001, 20002]
glToken = "**************************************************************************************************************************************"

class dataNode:

    url = ''

    driver = None
    data = None
    isGoodReg = None
    isFailedToLoad = False
    errorType = None


    def __init__(self, id=None, userAgent = None, firstName=None, secondName=None, date=[0, 0, 0], phone=None, address=None, mail=None, login=None, password=None, answer=None):

        self.id = id
        self.userAgent = userAgent
        self.firstName = firstName
        self.secondName = secondName
        self.date = date
        self.phone = phone
        self.address = address
        self.mail = mail
        self.login = login
        self.password = password
        self.answer = answer

