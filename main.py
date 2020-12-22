from selenium import webdriver
from selenium.common.exceptions import ElementClickInterceptedException, NoSuchElementException
import time

GMAIL = ""
PASSWORD = ""
Chrome_driver_path= r"C:\Users\14014\Desktop\100 days of code course Jupiter note book files\Web development topics\Chrome driver\chromedriver.exe"
driver = webdriver.Chrome(executable_path=Chrome_driver_path)
driver.get("https://tinder.com/")


time.sleep(3)
login_button = driver.find_element_by_xpath('//*[@id="content"]/div/div[1]/div/main/div[1]/div/div/div/div/header/div/div[2]/div[2]/button/span')
login_button.click()

time.sleep(3)
google_login = driver.find_element_by_xpath('//*[@id="modal-manager"]/div/div/div[1]/div/div[3]/span/div[1]/div/button/span[2]')
google_login.click()

time.sleep(2)
base_window = driver.window_handles[0]
googe_window = driver.window_handles[1]
driver.switch_to.window(googe_window)
print(driver.title)

time.sleep(2)
email = driver.find_element_by_xpath('//*[@id="identifierId"]')
email.send_keys(GMAIL)
next_tag = driver.find_element_by_class_name("VfPpkd-RLmnJb")
next_tag.click()


time.sleep(2)
password = driver.find_element_by_xpath('//*[@id="password"]/div[1]/div/div[1]/input')
password.send_keys(PASSWORD)
next_1 = driver.find_element_by_class_name("VfPpkd-RLmnJb")
next_1.click()

time.sleep(5)
allow_location_button = driver.find_element_by_xpath('//*[@id="modal-manager"]/div/div/div/div/div[3]/button[1]/span')
allow_location_button.click()
notifications_button = driver.find_element_by_xpath('//*[@id="content"]/div/div[2]/div/div/div[1]/button/span')
notifications_button.click()

time.sleep(1)
cookies = driver.find_element_by_xpath('//*[@id="content"]/div/div[2]/div/div/div[1]/button')
cookies.click()

for n in range(10):
    time.sleep(2)
    print("PASSED")
    try:
        liked_botton = driver.find_element_by_xpath('//*[@id="content"]/div/div[1]/div/main/div[1]/div/div/div[1]/div/div[2]/div[4]/button/span/svg')
        liked_botton.click()
    except ElementClickInterceptedException:

        try:
            match_popup = driver.find_element_by_css_selector(".itsAMatch a")
            match_popup.click()
        except NoSuchElementException:

            time.sleep(2)


driver.quit()

