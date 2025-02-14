import userAgents
import settings
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.keys import Keys
from gologin import GoLogin
import random

import clipboard
import time
import dataReader

class williamhillBot:
    url = 'https://vegas.williamhill.com/'
    driver = None
    data = None
    isGoodReg = None
    isFailedToLoad = False
    errorType = None

    fontsList = ["Bahnschrift", "Bahnschrift Light", "Bahnschrift SemiBold", "Baskerville Old Face", "Bauhaus 93", "Bell MT", "Berlin Sans FB", "Bernard MT Condensed", "Blackadder ITC", "Bodoni MT", "Bodoni MT Black", "Bodoni MT Condensed", "Book Antiqua", "Bookman Old Style", "Bookshelf Symbol 7", "Bradley Hand ITC", "Broadway", "Brush Script MT", "Calibri", "Calibri Light", "Californian FB", "Calisto MT", "Cambria", "Cambria Math", "Candara", "Candara Light", "Castellar", "Centaur", "Century", "Century Gothic", "Century Schoolbook", "Chiller", "Colonna MT", "Comic Sans MS", "Consolas", "Constantia", "Cooper Black", "Copperplate Gothic", "Copperplate Gothic Light", "Corbel", "Corbel Light", "Courier", "Courier New", "Curlz MT", "Ebrima", "Edwardian Script ITC", "Elephant", "Engravers MT", "Felix Titling", "Footlight MT Light", "Forte", "Franklin Gothic Book", "Franklin Gothic Heavy", "Franklin Gothic Medium", "Freestyle Script", "French Script MT", "Gabriola", "Gadugi", "Garamond", "Georgia", "Gigi", "Gill Sans MT", "Gill Sans MT Condensed", "Goudy Old Style", "Goudy Stout", "Haettenschweiler", "Harrington", "Helvetica", "High Tower Text", "HoloLens MDL2 Assets", "Impact", "Imprint MT Shadow", "Informal Roman", "Ink Free", "Javanese Text", "Jokerman", "Juice ITC", "Kristen ITC", "Kunstler Script", "Leelawadee UI", "Lucida Bright", "Lucida Calligraphy", "Lucida Console", "Lucida Fax", "Lucida Handwriting", "Lucida Sans", "Lucida Sans Typewriter", "Lucida Sans Unicode", "MS Gothic", "MS Outlook", "MS PGothic", "MS Reference Sans Serif", "MS Reference Specialty", "MS Sans Serif", "MS Serif", "MS UI Gothic", "MT Extra", "MV Boli", "Magneto", "Maiandra GD", "Malgun Gothic", "Marlett", "Matura MT Script Capitals", "Microsoft Himalaya", "Microsoft JhengHei", "Microsoft JhengHei Light", "Microsoft JhengHei Regular", "Microsoft JhengHei UI", "Microsoft JhengHei UI Light", "Microsoft JhengHei UI Regular", "Microsoft New Tai Lue", "Microsoft PhagsPa", "Microsoft Sans Serif", "Microsoft Tai Le", "Microsoft YaHei", "Microsoft YaHei Light", "Microsoft YaHei UI", "Microsoft YaHei UI Light", "Microsoft Yi Baiti", "MingLiU-ExtB", "MingLiU_HKSCS-ExtB", "Mistral", "Modern No. 20", "Mongolian Baiti", "Monotype Corsiva", "Myanmar Text", "NSimSun", "Niagara Engraved", "Niagara Solid", "Nirmala UI", "Old English Text MT", "Onyx", "PMingLiU-ExtB", "Palace Script MT", "Palatino Linotype", "Papyrus", "Papyrus Condensed", "Parchment", "Perpetua", "Perpetua Titling MT", "Playbill", "Poor Richard", "Pristina", "Ravie", "Roboto", "Rockwell", "Rockwell Condensed", "Segoe MDL2 Assets", "Segoe Print", "Segoe Script", "Segoe UI", "Segoe UI Black", "Segoe UI Emoji", "Segoe UI Historic", "Segoe UI Light", "Segoe UI Semibold", "Segoe UI Symbol", "Showcard Gothic", "SimSun", "SimSun-ExtB", "Sitka Banner", "Sitka Display", "Sitka Heading", "Sitka Small", "Sitka Subheading", "Sitka Text", "Snap ITC", "Stencil", "Sylfaen", "Symbol", "Tahoma", "Tempus Sans ITC", "Times", "Times New Roman", "Trebuchet MS", "Tw Cen MT", "Tw Cen MT Condensed", "Verdana", "Viner Hand ITC", "Vivaldi", "Vladimir Script", "Webdings", "Wide Latin", "Wingdings", "Wingdings 2", "Wingdings 3", "Yu Gothic", "Yu Gothic Light", "Yu Gothic Medium", "Yu Gothic Regular", "Yu Gothic UI", "Yu Gothic UI Light", "Yu Gothic UI Regular", "Yu Gothic UI Semibold"]
    andOs = ["Linux armv8l", "Linux aarch64", "Linux armv7l"]
    resolList = ["224x144", "640x360", "426x240", "1920x1080", "1280x720", "800x480", "1280x768"]


    golProfileId = None
    golProfileName = 'prWill'
    gol = None
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
                "families": self.fontsList[:len(self.fontsList)-1],
                "enableMasking": True,
                "enableDomRect": True
            },
            "mediaDevices": {
                "videoInputs": random.randint(1, 5),
                "audioInputs": random.randint(1, 4),
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

    def __init__(self, data: settings.dataNode, id: int):
        self.data = data
        self.createEnv()


        #print('dbg')
        opts = Options()
        #opts.add_argument('--proxy-server=socks5://' + settings.proxy)
        opts.add_argument(f'user-agent=' + data.userAgent)#userAgents.getUsrAgent())
        opts.add_argument('--disable-blink-features=AutomationControlled')
        #opts.add_argument("lang=en-GB") -> вставить в профиль
        #opts.add_argument('--use-fake-ui-for-media-stream')
        #opts.add_argument('--use-fake-device-for-media-stream')
        #opts.add_argument('--enable-javascript')
        #opts.headless = True #> work in headless (full input streets)
        #opts.add_argument('--disable-gpu')
        #opts.add_argument('--disable-dev-shm-usage')
        #opts.add_argument('--no-sandbox')
        opts.add_argument('--ignore-certificate-errors')
        opts.add_argument('--allow-running-insecure-content')

        opts.add_experimental_option("debuggerAddress", self.debugger_address)


        self.driver = webdriver.Chrome(executable_path="chromedriver.exe", options=opts)
        self.driver.delete_all_cookies()


    def fillReg1(self):
        driver = self.driver
        data = self.data

        WebDriverWait(driver, 50).until(
            EC.visibility_of_element_located((By.XPATH, "//*[@id=\"reg-firstName\"]")))

        driver.find_element(by=By.XPATH, value="//*[@id=\"reg-firstName\"]").send_keys(data.firstName)

        driver.find_element(by=By.XPATH, value="//*[@id=\"reg-lastName\"]").send_keys(data.secondName) #//*[@id=\"reg-dobDay\"]

        #print(dateTime)
        #time.sleep(5)
        driver.find_element(by=By.XPATH, value="//*[@id=\"reg-dobDay\"]").send_keys(data.date[0]) #
        driver.find_element(by=By.XPATH, value="//*[@id=\"cs-registration-component\"]/section/div/section/form/div/section/section[1]/div[4]/div/div/input[2]").send_keys(data.date[1])
        driver.find_element(by=By.XPATH, value="//*[@id=\"cs-registration-component\"]/section/div/section/form/div/section/section[1]/div[4]/div/div/input[3]").send_keys(data.date[2]) #//*[@id=\"reg-dobDay\"]

        driver.find_element(by=By.XPATH, value="//*[@id=\"reg-email\"]").send_keys(data.mail) #

        driver.find_element(by=By.XPATH, value="//*[@id=\"reg-mobile\"]").send_keys(data.phone) #

        clipboard.copy(data.address)



        autoCompleteDone = False
        tries = 0
        while (autoCompleteDone != True) and tries < 5:
            clearBtn = None
            clearBtnIsDisplayed = False
            driver.find_element(by=By.XPATH, value="//*[@id=\"reg-search\"]").send_keys(Keys.CONTROL, 'v')
            time.sleep(4)
            driver.find_element(by=By.XPATH, value="/html/body/div[2]/div/div[1]/section/section/div/section/form/div/section/section[2]/div/div[1]/button").click()

            try:
                WebDriverWait(driver, 5).until(
                    EC.visibility_of_element_located((By.XPATH, '//*[@id=\"cs-registration-component\"]/section/div/section/form/div/section/section[2]/div/a'))
                )
                clearBtn = driver.find_element(by=By.XPATH, value='/html/body/div[2]/div/div[1]/section/section/div/section/form/div/section/section[2]/div/a')
                clearBtnIsDisplayed = clearBtn.is_displayed()

            except Exception as ex:
                if ex == TimeoutException:
                    autoCompleteDone = True

            if (clearBtnIsDisplayed == False) or (autoCompleteDone == True):
                autoCompleteDone = True
            else:
                time.sleep(2)
                tries+=1
                clearBtn.click()

        #time.sleep(999)
        #print('ERRRRRRRRRRR')

        try:
            WebDriverWait(driver, 50).until(
                EC.presence_of_element_located((By.CSS_SELECTOR,
                                   "body > div.pca > div:nth-child(1) > div.pca.pcalist > div.pcaitem.pcafirstitem"))
                )
            driver.find_element(by=By.CSS_SELECTOR,
                                    value="body > div.pca > div:nth-child(1) > div.pca.pcalist > div.pcaitem.pcafirstitem").click()

            WebDriverWait(driver, 50).until_not(
                    EC.visibility_of_element_located((By.CSS_SELECTOR,
                                   "body > div.pca > div:nth-child(1) > div.pca.pcalist > div.pcaitem.pcafirstitem")))
        except Exception as ex:
            self.errorType = 'Address selection Not Found'
            self.isGoodReg = False
            self.isFailedToLoad = False
            return

        WebDriverWait(driver, 50).until(EC.visibility_of_element_located((By.XPATH, "//*[@id=\"reg-submit\"]")))


        driver.find_element(by=By.XPATH, value="//*[@id=\"reg-submit\"]").click()

        clipboard.copy(data.login)
        driver.find_element(by=By.XPATH, value="//*[@id=\"reg-username\"]").send_keys(Keys.CONTROL, 'v')

        clipboard.copy(data.password)
        driver.find_element(by=By.XPATH, value="//*[@id=\"reg-password\"]").send_keys(Keys.CONTROL, 'v')

        select = Select(driver.find_element(by=By.XPATH,  value="//*[@id=\"reg-challenge\"]"))
        select.select_by_visible_text('My first pets name')

        select = Select(driver.find_element(by=By.XPATH,  value="//*[@id=\"reg-depositLimit\"]"))
        select.select_by_visible_text('£1000')

        driver.find_element(by=By.XPATH, value="//*[@id=\"reg-response\"]").send_keys(data.answer)
        driver.find_element(by=By.XPATH, value="//*[@id=\"reg-submit\"]").click()

        WebDriverWait(driver, 50).until(EC.visibility_of_element_located((By.XPATH, '//*[@id=\"cs-registration-component\"]/section/div/section/form/div/div')))

        WebDriverWait(driver, 50).until(
            EC.any_of(
                EC.staleness_of(driver.find_element(by=By.XPATH,
                                                        value='//*[@id=\"cs-registration-component\"]/section/div/section/form/div/div')),
                EC.element_to_be_clickable((By.XPATH,
                                                        '//*[@id=\"reg-submit\"]'))
            ))



#//*[@id=\"cs-registration-component\"]/section/div/section/form/div/section/div[1]/div/p[2]/span/text() #This username is already in use. Choose one of the proposed ones below or enter a different one.
#//*[@id=\"cs-registration-component\"]/section/div/section/form/div/section/div[1]/div/p[2]/span        #Username must not exceed 15 characters
#//*[@id=\"cs-registration-component\"]/section/div/section/form/div/section/div[1]/div/p[2]/span         #Username must be at least 6 characters.
#//*[@id=\"cs-registration-component\"]/section/div/section/form/div/section/div[2]/div/p[2]/span/text()       #Password must have a minimum of 8 characters and contain at least one letter, number and symbol (!#%&()*+,-./:<=>?@^_`|~).
#//*[@id=\"cs-registration-component\"]/section/div/section/form/div/section/div[2]/div/p[2]/span       #Password must not exceed 15 characters



        goodReg = False
        try:
            #//*[@id="cs-registration-component"]/section/div/section/form/div/div[1]/div/div/span
            #Please check the errors in the form below


            '''
            WebDriverWait(driver, 50).until(
                EC.any_of(EC.visibility_of_element_located((By.CSS_SELECTOR, "cs-registration-component > section > div > section > form > div > div.cs-component.cs-component-form-error > div > div > span")),
                          EC.visibility_of_element_located((By.XPATH, "//*[@id=\"cs-registration-component\"]/section/div/section/form/div/div[1]/div/div/span")),
                          EC.visibility_of_element_located((By.XPATH, "//*[@id=\"cs-registration-component\"]/section/div/div/div[1]")),
                          ))
            '''
            #//*[@id=\"cs-registration-component\"]/section/div/div/div[1]/p[2]
            WebDriverWait(driver, 50).until(
                EC.any_of(EC.visibility_of_element_located((By.XPATH, "//*[@id=\"cs-registration-component\"]/section/div/section/form/div/section/div[1]/div/p[2]/span")),
                          EC.visibility_of_element_located((By.XPATH, "//*[@id=\"cs-registration-component\"]/section/div/section/form/div/section/div[2]/div/p[2]/span")),
                          EC.visibility_of_element_located((By.XPATH, "//*[@id=\"cs-registration-component\"]/section/div/section/form/div/div[1]/div/div/span")),
                          EC.visibility_of_element_located((By.XPATH, "//*[@id=\"cs-registration-component\"]/section/div/div/div[1]/p[2]"))
                          ))
            text = ''
            try:
                text = driver.find_element(by=By.XPATH, value='//*[@id=\"cs-registration-component\"]/section/div/section/form/div/section/div[1]/div/p[2]/span').text
            except:
                pass

            try:
                if not text:
                    text = driver.find_element(by=By.XPATH, value='//*[@id=\"cs-registration-component\"]/section/div/section/form/div/section/div[2]/div/p[2]/span').text
                else:
                    text = text + ' and ' + driver.find_element(by=By.XPATH, value='//*[@id=\"cs-registration-component\"]/section/div/section/form/div/section/div[2]/div/p[2]/span').text
            except:
                pass

            try:
                if not text:
                    text = driver.find_element(by=By.XPATH, value='//*[@id=\"cs-registration-component\"]/section/div/section/form/div/div[1]/div/div/span').text
                else:
                    text = text + ' and ' + driver.find_element(by=By.XPATH, value='//*[@id=\"cs-registration-component\"]/section/div/section/form/div/div[1]/div/div/span').text
            except:
                pass

            try:
                if not text:
                    text = driver.find_element(by=By.XPATH, value='//*[@id=\"cs-registration-component\"]/section/div/div/div[1]/p[2]').text
                else:
                    text = text + ' and ' + driver.find_element(by=By.XPATH, value='//*[@id=\"cs-registration-component\"]/section/div/div/div[1]/p[2]').text
            except:
                pass


            self.errorType = text


            goodReg = False
        except Exception as ex:
            #print('a1 ', ex)
            try:
                WebDriverWait(driver, 80).until(
                    EC.any_of(EC.frame_to_be_available_and_switch_to_it((By.NAME, 'deposit-modal__iframe')),
                              EC.visibility_of_element_located((By.XPATH, '/html/body/div[8]/div/div/div/div/div/section/div[2]/div/div/section[1]/svg')),
                              EC.visibility_of_element_located((By.XPATH, '/html/body/div[8]/div/div/div/div/div/section/div[2]/div/div/section[2]/ul/li[1]/a/span[2]')),
                              ))
                goodReg = True
            except Exception as ex:
                #print('ba1 ', ex)
                goodReg = False

        self.isGoodReg = goodReg
        #//*[@id="cs-registration-component"]/section/div/section/form/div/div[1]/div/div/span           =Oops, something went wrong. Please try again later...
        # spinner //*[@id=\"cs-registration-component\"]/section/div/section/form/div/div

        driver.get_screenshot_as_file('screenshots\sc_'+str(data.id)+'_'+str(goodReg)+'.png')
        #print('g5')
        #time.sleep(5)
        #driver.quit()

    def start(self):
        driver = self.driver

        try:
            driver.get(url=self.url)

            time.sleep(5)



            WebDriverWait(driver, 10).until(                                                                   #cookie click
                EC.visibility_of_element_located((By.XPATH, "/html/body/div[2]/div/div/div[3]/div/button")))

            driver.find_element(by=By.XPATH, value="/html/body/div[2]/div/div/div[3]/div/button").click()


            WebDriverWait(driver, 20).until(
                EC.visibility_of_element_located((By.XPATH, "/html/body/div[1]/div/div/div/div/div[1]/div/div/div[2]/div/div[4]/button")))                           #join

            driver.find_element(by=By.XPATH, value="/html/body/div[1]/div/div/div/div/div[1]/div/div/div[2]/div/div[4]/button").click()

            '''
            WebDriverWait(driver, 50).until(
                EC.any_of(
                    EC.presence_of_element_located((By.XPATH, "/html/body/div[3]/div/div/div/div[1]/div[3]/div/a")),
                    EC.presence_of_element_located((By.XPATH, "/html/body/div[4]/div/div/div/div[1]/div[3]/div/a"))
                )
            )

            try:
                driver.find_element(by=By.XPATH, value="/html/body/div[3]/div/div/div/div[1]/div[3]/div/a").click()
            except:
                pass

            try:
                driver.find_element(by=By.XPATH, value="/html/body/div[4]/div/div/div/div[1]/div[3]/div/a").click()
            except:
                pass

            '''


            #WebDriverWait(driver, 20).until(
            #    EC.visibility_of_element_located((By.XPATH, "/html/body/div[5]/div/div/div/div/div/div/div/section/div/div[2]/div[1]/div/div/button")))
            #driver.find_element(by=By.XPATH, value="/html/body/div[5]/div/div/div/div/div/div/div/section/div/div[2]/div[1]/div/div/button").click()

#

            WebDriverWait(driver, 50).until(
                EC.visibility_of_element_located((By.CSS_SELECTOR, 'body > div.ReactModalPortal > div > div > div')))

            WebDriverWait(driver, 50).until_not(
                EC.visibility_of_element_located((By.CSS_SELECTOR, 'body > div.ReactModalPortal > div > div > div')))

            WebDriverWait(driver, 50).until(
                EC.frame_to_be_available_and_switch_to_it((By.NAME, 'cp-registration-frame')))
            self.fillReg1()

        except Exception as ex:
            if 'net::ERR_CONNECTION_RESET' in str(ex):
                self.isFailedToLoad = True
            else:
                print(ex)
        finally:
            driver.close()
            driver.quit()

            self.deleteEnv()




