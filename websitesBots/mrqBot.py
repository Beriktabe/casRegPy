import settings
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.keys import Keys
from gologin import GoLogin
import time
import random

class mrqBot:
    url = 'https://mrq.com/signup/account-details?redirect=%2Fsecure%2Fslots%2Fsquealin-riches'
    driver = None
    data = None
    isGoodReg = None
    isFailedToLoad = False
    errorType = ''

    fontsList = ["Bahnschrift", "Bahnschrift Light", "Bahnschrift SemiBold", "Baskerville Old Face", "Bauhaus 93", "Bell MT", "Berlin Sans FB", "Bernard MT Condensed", "Blackadder ITC", "Bodoni MT", "Bodoni MT Black", "Bodoni MT Condensed", "Book Antiqua", "Bookman Old Style", "Bookshelf Symbol 7", "Bradley Hand ITC", "Broadway", "Brush Script MT", "Calibri", "Calibri Light", "Californian FB", "Calisto MT", "Cambria", "Cambria Math", "Candara", "Candara Light", "Castellar", "Centaur", "Century", "Century Gothic", "Century Schoolbook", "Chiller", "Colonna MT", "Comic Sans MS", "Consolas", "Constantia", "Cooper Black", "Copperplate Gothic", "Copperplate Gothic Light", "Corbel", "Corbel Light", "Courier", "Courier New", "Curlz MT", "Ebrima", "Edwardian Script ITC", "Elephant", "Engravers MT", "Felix Titling", "Footlight MT Light", "Forte", "Franklin Gothic Book", "Franklin Gothic Heavy", "Franklin Gothic Medium", "Freestyle Script", "French Script MT", "Gabriola", "Gadugi", "Garamond", "Georgia", "Gigi", "Gill Sans MT", "Gill Sans MT Condensed", "Goudy Old Style", "Goudy Stout", "Haettenschweiler", "Harrington", "Helvetica", "High Tower Text", "HoloLens MDL2 Assets", "Impact", "Imprint MT Shadow", "Informal Roman", "Ink Free", "Javanese Text", "Jokerman", "Juice ITC", "Kristen ITC", "Kunstler Script", "Leelawadee UI", "Lucida Bright", "Lucida Calligraphy", "Lucida Console", "Lucida Fax", "Lucida Handwriting", "Lucida Sans", "Lucida Sans Typewriter", "Lucida Sans Unicode", "MS Gothic", "MS Outlook", "MS PGothic", "MS Reference Sans Serif", "MS Reference Specialty", "MS Sans Serif", "MS Serif", "MS UI Gothic", "MT Extra", "MV Boli", "Magneto", "Maiandra GD", "Malgun Gothic", "Marlett", "Matura MT Script Capitals", "Microsoft Himalaya", "Microsoft JhengHei", "Microsoft JhengHei Light", "Microsoft JhengHei Regular", "Microsoft JhengHei UI", "Microsoft JhengHei UI Light", "Microsoft JhengHei UI Regular", "Microsoft New Tai Lue", "Microsoft PhagsPa", "Microsoft Sans Serif", "Microsoft Tai Le", "Microsoft YaHei", "Microsoft YaHei Light", "Microsoft YaHei UI", "Microsoft YaHei UI Light", "Microsoft Yi Baiti", "MingLiU-ExtB", "MingLiU_HKSCS-ExtB", "Mistral", "Modern No. 20", "Mongolian Baiti", "Monotype Corsiva", "Myanmar Text", "NSimSun", "Niagara Engraved", "Niagara Solid", "Nirmala UI", "Old English Text MT", "Onyx", "PMingLiU-ExtB", "Palace Script MT", "Palatino Linotype", "Papyrus", "Papyrus Condensed", "Parchment", "Perpetua", "Perpetua Titling MT", "Playbill", "Poor Richard", "Pristina", "Ravie", "Roboto", "Rockwell", "Rockwell Condensed", "Segoe MDL2 Assets", "Segoe Print", "Segoe Script", "Segoe UI", "Segoe UI Black", "Segoe UI Emoji", "Segoe UI Historic", "Segoe UI Light", "Segoe UI Semibold", "Segoe UI Symbol", "Showcard Gothic", "SimSun", "SimSun-ExtB", "Sitka Banner", "Sitka Display", "Sitka Heading", "Sitka Small", "Sitka Subheading", "Sitka Text", "Snap ITC", "Stencil", "Sylfaen", "Symbol", "Tahoma", "Tempus Sans ITC", "Times", "Times New Roman", "Trebuchet MS", "Tw Cen MT", "Tw Cen MT Condensed", "Verdana", "Viner Hand ITC", "Vivaldi", "Vladimir Script", "Webdings", "Wide Latin", "Wingdings", "Wingdings 2", "Wingdings 3", "Yu Gothic", "Yu Gothic Light", "Yu Gothic Medium", "Yu Gothic Regular", "Yu Gothic UI", "Yu Gothic UI Light", "Yu Gothic UI Regular", "Yu Gothic UI Semibold"]
    andOs = ["Linux armv8l", "Linux aarch64", "Linux armv7l"]
    resolList = ["224x144", "640x360", "426x240", "1920x1080", "1280x720", "800x480", "1280x768"]

    golProfileName = 'prMRQ'
    gol = None
    golProfileId = None
    debugger_address = None

    def createEnv(self):
        random.shuffle(self.fontsList)
        random.shuffle(self.andOs)
        random.shuffle(self.resolList)

        self.gol = GoLogin({
            "token": settings.glToken,
        })

        self.profile_id = self.gol.create({
            "name": self.golProfileName,
            "os": 'android',
            "navigator": {
                "language": 'enGB,en;q=0.9,en-GB;q=0.8,en-US;q=0.7',
                "userAgent": self.data.userAgent,
                "resolution": self.resolList[0],
                "platform": self.andOs[0],
                "maxTouchPoints": 5
            },
            "proxyEnabled": True,
            "proxy": {
                "mode": "socks5",
                "host": "127.0.0.1",
                "port": 20001,
                "username": "",
                "password": ""
            },
            "webRTC": {
                "mode": "alerted",
                "enabled": True,
                "customize": True,
                "localIpMasking": False,
                "fillBasedOnIp": True
            },
            "fonts": {
                "families": self.fontsList[:12],
                "enableMasking": True,
                "enableDomRect": True
            },
            "mediaDevices": {
                "videoInputs": random.randint(1, 5),
                "audioInputs": random.randint(1, 5),
                "audioOutputs": 1,
                "enableMasking": True
            },
            "canvas": {
                "mode": "off",
                "noise": 0
            }
        });

        self.gol.update({
            "id": str(self.profile_id),
            "name": self.golProfileName,
        });


        self.gol = GoLogin({
            "token": settings.glToken,
            "profile_id": str(self.profile_id),
        })

        self.debugger_address = self.gol.start()

    def deleteEnv(self):
        self.gol.stop()
        self.gol.delete(self.golProfileId)

    def fillReg1(self):
        driver = self.driver

        WebDriverWait(driver, 20).until(
            EC.visibility_of_element_located(
                (By.XPATH, "//*[@id=\"username\"]")))

        driver.find_element(by=By.XPATH,
                            value="//*[@id=\"username\"]").send_keys(self.data.login)

        driver.find_element(by=By.XPATH,
                            value="//*[@id=\"email\"]").send_keys(self.data.mail)

        driver.find_element(by=By.XPATH,
                            value="//*[@id=\"password\"]").send_keys(self.data.password)

        logErrorSpan = "/html/body/div[2]/div/div[3]/div[2]/div/div/div/div/div[2]/span/div/form/div[1]/div/label/span"
        mailErrorSpan = "/html/body/div[2]/div/div[3]/div[2]/div/div/div/div/div[2]/span/div/form/div[2]/div/label/span"
        passErrorSpan = "/html/body/div[2]/div/div[3]/div[2]/div/div/div/div/div[2]/span/div/form/div[3]/div[1]/label/span"

        logErrorElements = []
        mailErrorElements = []
        passErrorElements = []

        try:
            WebDriverWait(driver, 5).until(
                EC.any_of(
                    EC.visibility_of_element_located((By.XPATH, logErrorSpan)),
                    EC.visibility_of_element_located((By.XPATH, mailErrorSpan)),
                    EC.visibility_of_element_located((By.XPATH, passErrorSpan))
            ))

            logErrorElements = driver.find_elements(by=By.XPATH, value=logErrorSpan)
            mailErrorElements = driver.find_elements(by=By.XPATH, value=mailErrorSpan)
            #print(mailErroElements[0].text)
            passErrorElements = driver.find_elements(by=By.XPATH, value=passErrorSpan)

        except Exception as ex:
            if ex != TimeoutException:
                print(ex)

        if logErrorElements:
            self.errorType += logErrorElements[0].text + ' |+| '

        if mailErrorElements:
            self.errorType += mailErrorElements[0].text + ' |+| '

        if passErrorElements:
            self.errorType += passErrorElements[0].text + ' |+| '

        if self.errorType:
            self.isGoodReg = False
            return

        WebDriverWait(driver, 50).until(
            EC.element_to_be_clickable((By.XPATH, "//*[@id=\"signupBox\"]/div/div[2]/span/div/form/div[4]/button")))

        driver.find_element(by=By.XPATH, value="//*[@id=\"signupBox\"]/div/div[2]/span/div/form/div[4]/button").click()
        self.fillReg2()
        #//*[@id="signupBox"]/div/div[2]/span/div/form/div[4]/button

        #//*[@id="signupBox"]/div/div[2]/span/div/form/div[2]/div/label/span  #Awkward... This email address is already being used.
        #//*[@id="signupBox"]/div/div[2]/span/div/form/div[1]/div/label/span  #Somebody's already swiped this funky username – think again!
        #//*[@id="signupBox"]/div/div[2]/span/div/form/div[3]/div[1]/label/span #At least 6 characters. At least 1 capital & 1 lowercase letter.

    def fillReg2(self):
        driver = self.driver

        WebDriverWait(driver, 20).until(
            EC.visibility_of_element_located(
                (By.XPATH, "//*[@id=\"firstName\"]")))

        driver.find_element(by=By.XPATH, value="//*[@id=\"firstName\"]").send_keys(self.data.firstName)

        driver.find_element(by=By.XPATH, value="//*[@id=\"lastName\"]").send_keys(self.data.secondName)

        driver.find_element(by=By.XPATH, value="//*[@id=\"phoneNumber\"]").send_keys(self.data.phone)


        select = Select(driver.find_element(by=By.XPATH,  value="//*[@id=\"datepicker__select--day\"]"))
        select.select_by_visible_text(str(self.data.date[0]))

        select = Select(driver.find_element(by=By.XPATH,  value="//*[@id=\"datepicker__select--month\"]"))
        select.select_by_index(self.data.date[1])

        select = Select(driver.find_element(by=By.XPATH,  value="//*[@id=\"datepicker__select--year\"]"))
        select.select_by_visible_text(str(self.data.date[2]))

        driver.find_element(by=By.XPATH, value="//*[@id=\"query\"]").send_keys(self.data.address)
        try:
            WebDriverWait(driver, 20).until(
                EC.visibility_of_element_located(
                    (By.XPATH, "/html/body/div[2]/div/div[3]/div[2]/div/div[1]/div/div/div[2]/span/div/form/div[5]/div[1]/div[2]/div/div/span[1]")))
            print()
            tries = 0
            while tries < 5:
                if driver.find_element(by=By.XPATH,
                                       value="/html/body/div[2]/div/div[3]/div[2]/div/div[1]/div/div/div[2]/span/div/form/div[5]/div[1]/div[2]/div/div/span[1]").text != 'Loading...':
                    break
                else:
                    tries += 1
                    time.sleep(1)
            if tries >= 5:
                self.errorType = 'Cant find address'
                return
            #time.sleep(555)
            driver.find_element(by=By.XPATH, value="/html/body/div[2]/div/div[3]/div[2]/div/div[1]/div/div/div[2]/span/div/form/div[5]/div[1]/div[2]/div/div/span[1]").click()

        except Exception as ex:
            if ex == TimeoutException:
                self.errorType = 'Cant find address selection'
            return

        #time.sleep(50)
        driver.find_element(by=By.XPATH, value="//*[@id=\"signupBox\"]/div/div[2]/span/div/form/div[6]/button").click()
        #/html/body/div[2]/div/div[3]/div[2]/div/div/div/div/div[2]/span/div/form/div[6]/button


        input('GGGGGGGG')
        #pass

    def fillReg3(self):
        #//*[@id="agreeTerms"]       #checkBox
        #//*[@id="agreeResponsible"]
        #//*[@id="signupBox"]/div/div[2]/span/div/form/div[3]/button btn
        pass
    def endReg(self):

        #//*[@id="addPaymentBox"]/div/div/span/div/span/div/div[1]/span/form/div/button[2]/span       #btn

        #//*[@id="addPaymentBox"]/div/div/span/div/span/div/div[1]/form/div/button/span            #btn
        pass
        #//*[@id="firstName"]         #/html/body/div[2]/div/div[3]/div[2]/div/div[1]/div/div/div[2]/span/div/form/div[1]/div[2]/div/label/span
        #//*[@id="lastName"]          #/html/body/div[2]/div/div[3]/div[2]/div/div[1]/div/div/div[2]/span/div/form/div[2]/div/label/span

    #//*[@id="datepicker__select--day"]       #/html/body/div[2]/div/div[3]/div[2]/div/div[1]/div/div/div[2]/span/div/form/div[3]/div[2]/label/span
    #//*[@id="datepicker__select--month"]
    #//*[@id="datepicker__select--year"]

    #//*[@id="phoneNumber"]        #/html/body/div[2]/div/div[3]/div[2]/div/div[1]/div/div/div[2]/span/div/form/div[4]/div/div/label/span
    #//*[@id="query"]
    #//*[@id="signupBox"]/div/div[2]/span/div/form/div[5]/div[1]/div[2]/div/div/span
#//*[@id="query"]
    def __init__(self, data: settings.dataNode, id: int):
        self.data = data
        self.createEnv()

        opts = Options()
        opts.add_experimental_option("debuggerAddress", self.debugger_address)

        self.driver = webdriver.Chrome(executable_path="chromedriver.exe", options=opts)
        self.driver.delete_all_cookies()

    def start(self):
        try:
            driver = self.driver
            driver.get(url=self.url)

            self.fillReg1()

            time.sleep(10)

            #//*[@id=\"username\"]
        except Exception as ex:
            print(ex)
        finally:
            self.driver.close()
            self.driver.quit()
            self.deleteEnv()