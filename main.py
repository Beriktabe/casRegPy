import userAgents
from selenium import webdriver
from websitesBots.williamhillBot import williamhillBot
from websitesBots.mrqBot import mrqBot
from settings import dataNode
import time
import subprocess
import os

from threading import Thread
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options


import dataReader
##
#url='https://bingo.williamhill.com/en-gb/promotions/promotion/s10g20-im-1103'
##
#dr = uc.Chrome(driver_executable_path=ChromeDriverManager(log_level=0).install())
#dr.get(url)
#time.sleep(4000)
#va = dataReader.readByIndex(1)


def threaded_function(arg):
    opts = Options()
    opts.add_argument('--proxy-server=socks5://' + arg)
    driver = webdriver.Chrome(service=Service(ChromeDriverManager(log_level=0).install()), options=opts)
    driver.get('https://2ip.ru/')
    time.sleep(200)



#Autoproxytool.exe -freeport=all
goodsReg = []
badsReg = []

#subprocess.run(["911re\ProxyTool\AutoProxyTool.exe", "-freeport=all"])
#subprocess.run(["911re\ProxyTool\AutoProxyTool.exe", "-changeproxy/GB", "-proxyport=20001"])
#subprocess.run(["911re\ProxyTool\AutoProxyTool.exe", "-changeproxy/GB", "-proxyport=20003"])
'''
time.sleep(10)

thread1 = Thread(target=threaded_function, args=('127.0.0.1:20003',))
thread1.start()
thread2 = Thread(target=threaded_function, args=('127.0.0.1:20004',))
thread2.start()
'''
proxySwitch = 0

for i in range(1, 900):
    reg = open("reg.txt", "a")
    #try:
    tempDataNode = dataReader.readByIndex(i)
    ll = mrqBot(tempDataNode, 0)#williamhillBot(tempDataNode, 0)
    ll.start()
    #except TimeoutError:
        #print('ERR ' + str(tempDataNode.id))
        #proxySwitch+=1
        #reg.close()
        #continue

#good reg /html/body/div[8]/div/div/div/div/div/section/div[2]/div/div/section[1]/svg
    #/html/body/div[8]/div/div/div/div/div/section/div[2]/div/div/section[2]/ul/li[1]/a/span[2]
    #if ll.isFailedToLoad:
    #    subprocess.run(["911re\ProxyTool\AutoProxyTool.exe", "-changeproxy/GB", "-proxyport=20001"])
    #    time.sleep(5)
    #    ll = williamhillBot(tempDataNode, 0)
    #    ll.start()

    if ll.isGoodReg:
        print('GOOD REG: ', tempDataNode.login, '  | row: ', i)
        goodsReg.append(i)
    else:
        print('BAD REG: ', i, ' | Reason: ', ll.errorType)
        badsReg.append(i)
        proxySwitch+=1
        if proxySwitch >= 10:
            subprocess.run(["911re\ProxyTool\AutoProxyTool.exe", "-changeproxy/GB", "-proxyport=20001"])
            proxySwitch = 0
            time.sleep(5)

    reg.write(str(tempDataNode.id) + ': ' + str(ll.isGoodReg) + ' | Reason: ' + str(ll.errorType) + '\n')
    reg.close()



print('----------------------------------------------------------------')
for i in goodsReg:
    print(i , ', ')
print('----------------------------------------------------------------')





#Message: unknown error: net::ERR_CONNECTION_RESET  -> reconnect proxy