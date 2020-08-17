from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait as Wait
from selenium.common.exceptions import NoSuchElementException
import time

#INPUT YOUR EMAIL ID AND PASSWORD
email_ID = str(input("Enter your email id: "))
pass_word = str(input("Enter your password: "))

#LOCATE THE PATH OF YOUR WEBDRIVER
PATH = "F:\chrome_driver\chromedriver.exe" #path can be different 
driver = webdriver.Chrome(PATH)

#OPEN THE URL
driver.maximize_window()

driver.get("https://www.facebook.com/login")

try:
	#LOCATE THE ELEMENTS OF THE WEBPAGE
	email = driver.find_element(By.ID, "email")
	passwd = driver.find_element(By.ID, "pass")
	login = driver.find_element(By.NAME, "login")
	Wait(driver, 10) #wait until the elements are found
	
	#FILLS UP YOUR EMAIL ID ONE BY ONE
	for i in email_ID:
		email.send_keys(i)
		time.sleep(0.25)

	#FILLS UP YOUR PASSWORD ONE BY ONE
	for i in pass_word:
		passwd.send_keys(i)
		time.sleep(0.25)

	time.sleep(1.0)
	login.click() #clicks onto the login button
#EXCEPTION HANDLING
except NoSuchElementException:
	print("Error: element does not exist")