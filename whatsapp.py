from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome([driver path]) #specify the path to chromedriver.exe

driver.get('http://web.whatsapp.com')

name = input('Enter the name of user or group : ')
msg = input('Enter the message : ')
count = int(input('Enter the count : '))

#Scan the code before proceeding further
input('Enter anything after scanning QR code')

user = driver.find_element_by_xpath('//span[@title = "{}"]'.format(name)) #these html tags may change, inpect element to verify and change
user.click()

msg_box = driver.find_element_by_class_name('_13mgZ')#these html tags may change, inpect element to verify and change

for i in range(count):
    msg_box.send_keys(msg)
    driver.find_element_by_class_name('_3M-N-').click()#these html tags may change, inpect element to verify and change
