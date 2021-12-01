from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
import time

driver = webdriver.Chrome('/home/tnelms/bin/selenium/chromedriver')

# A test to show that the title does not contain tacos
def test_titleFail():
    titleFail("tacos")

# A test to show that the title contains Hudl
def test_titlePass():
    titleFail("Hudl")


# This test verifies that an incorrect login will load the "Need Help" option for the user.
def test_login_fail():
    base_login("selenium", "selenium")
    error = driver.find_element_by_class_name("need-help").text
    print(error)
    assert "Need help?" in error
    driver.close

# This test logs in to the user's home and verifies by clicking on the menu icon.  Had to include a wait for visibility 
# Add valid username and password to validate
def test_login_pass():

    driver.implicitly_wait(3)
    base_login("", "")
 
    menu = WebDriverWait(driver,15).until(
        EC.visibility_of_element_located((By.CSS_SELECTOR, "div.hui-secondarynav__open-menu > div > div"))
        )
    
    menu.click()
    driver.close

# I've tried about every combination of close, quit, and stop client and I can't kill the window. :/
def test_teardown():
    driver.stop_client
    driver.quit

def base_login(user, passwd):
    driver.get("https://www.hudl.com/login")

    username = driver.find_element_by_id("email")
    password = driver.find_element_by_id("password")
    logIn = driver.find_element_by_id("logIn")

    username.clear()
    password.clear()
    username.send_keys(user)
    password.send_keys(passwd)

    logIn.click()


def titleFail(title):
    driver.get("https://www.hudl.com/login")
    assert title in driver.title
    driver.close

# test_login_fail()
# test_titleFail() 
# test_titlePass() 
# test_login_pass()
