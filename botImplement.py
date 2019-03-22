from selenium  							import webdriver
from selenium.webdriver.firefox.options import Options
import time 
import commentBot   					as bot

pTime = time.time()

username = "hahayeahbot"
password = "123123123JK"
tryTime  = 10
subjects  = ["nastyfeminism"]
headless = True
dateDict = {}
message  = open("message.txt").read()

#create driver instance and log in
options = Options()  
options.headless = False
driver = webdriver.Firefox(options = options)

bot.logIn(driver, username, password, tryTime)

dateDict = bot.comment(username, password, driver, tryTime, subjects, message, headless, dateDict)

while True:
	cTime = time.time()
	if (cTime - pTime) % (60*5) == 0 :
		for subject in subjects:
			dateDict = bot.comment(username, password, driver, tryTime, subject, message, headless, dateDict)