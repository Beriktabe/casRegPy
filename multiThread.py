import subprocess
import settings
import dataReader
from websitesBots.williamhillBot import williamhillBot

class multiThread:

    threadsHandler = []
    #threads = 0
    portFormard = []

    def _workThread(self, proxy:int, id:int, dataNode:settings.dataNode):
        bot = williamhillBot(dataNode, id)
        bot.start()

        pass

    def __init__(self, portForward:list, range:tuple): #threads:int,
        #self.threads = threads
        self.portFormard = portForward



    def start(self):

        for i in self.portFormard:
            proxy = "-proxyport=" + str(i)
            subprocess.run(["911re\ProxyTool\AutoProxyTool.exe", "-changeproxy/GB", proxy])
        tempDataNode = dataReader.readByIndex(0)
        thread1 = Thread(target=self._workThread, args=('127.0.0.1:20003', 0, tempDataNode,))
        thread1.start()