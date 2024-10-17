from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

proxies = []
failed = []
sender = []

class proxy:

    def __init__(self, ip, name):
        self.ip = ip
        self.region, self.name = self.getRegionName(name)

    def getRegionName(self, name):
        lst = name.split(" ")
        return lst[0], lst[1]
    
    def printInfos(self):
        print(f'IP Adress: {self.ip}')
        print(f'Device: {self.region} {self.name}')

proxy1 = proxy("192.168.0.1", "SMA 05")
proxy1.printInfos()


# Get iproxy scraping working
# Figure out how to stay loged in
# Get all elements
# Filter by class AND use a ReGex in order to filter IPs
# If a online proxy finds itself on a failed list, remove it from the failed list
# Get its ip, if the filter fails, that specifc proxy is saved as failed
# If the failed proxy is in the failed list, ignores
# Else stores it on the senders list
# Goes one by one on the senders list
# Get its name (It will determinate the group and the proxy itself) 
# Send a message like "Proxy sma 01 está offline"
# Resets the proxies list (keeps stored the failed list)
# Resets the senders list
# Waits 5 minutes

