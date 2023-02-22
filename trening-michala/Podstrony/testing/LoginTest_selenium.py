from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as excon
from selenium.webdriver.support.wait import WebDriverWait
from selenium.common.exceptions import TimeoutException
import time
import datetime


def make_screenshot(driver):
    teraz=datetime.datetime.now()
    driver.get_screenshot_as_file(f"screen{teraz.strftime('%H--%M--%S')}.png")


def check_if_logged(driver):
    span_navbar(driver)

    return check_if_already_visible(driver, By.ID, "menu")


def logout(driver):
    span_navbar(driver)
    print(1)
    if check_if_already_visible(driver, By.ID, "logout"):
        print("2")
        logout_button = driver.find_element(By.ID, "logout")
        print("3")
        try:
            logout_button.click()
        except:
            print("nie Wylogowano uzytkownika")
        return True


def login(username, password, driver):
    pass


def go_to_login_page(driver):
    span_navbar(driver)
    if check_if_already_visible(driver,By.ID,"login"):
        loginrefbutton = driver.find_element(By.ID, "login")
        loginrefbutton.click()


def go_to_signup_page(driver):
    span_navbar(driver)
    try:
        check_if_already_visible(driver,By.ID,"sign_up")
        driver.find_element(By.ID, "sign_up").click()
    except:
        make_screenshot(driver)


def signup(driver, username, password, email):
    if check_if_already_visible(driver, By.ID, "email") and check_if_already_visible(driver, By.ID, "name") and check_if_already_visible(driver, By.ID, "password1") and check_if_already_visible(driver, By.ID, "password2"):
        emailform = driver.find_element(By.ID, "email")
        nameform = driver.find_element(By.ID, "name")
        passwordform = driver.find_element(By.ID, "password1")
        confirmpasswordform = driver.find_element(By.ID, "password2")
        submitbutton = driver.find_element(By.XPATH, "/html/body/button")
        emailform.clear()
        nameform.clear()
        passwordform.clear()
        confirmpasswordform.clear()
        emailform.send_keys(email)
        nameform.send_keys(username)
        passwordform.send_keys(password)
        confirmpasswordform.send_keys(password)
        submitbutton.click()
        print("allfound")


def span_navbar(driver):
    if check_if_already_visible(driver,By.CLASS_NAME,"navbar-toggler"):
        spanbutton = driver.find_element(By.CLASS_NAME,"navbar-toggler")
        print(spanbutton.get_attribute("aria-expanded"))
        if not spanbutton.get_attribute("aria-expanded"):
            spanbutton.click()
            print("span button clicked")


def logut_if_logged_in(driver):
    if check_if_logged(driver):
        logout(driver)


def check_if_already_visible(driver,bywhat,valueofwhat):
    timeout = 3
    message = "nie znaleziono elementu w 3 s"
    found = excon.visibility_of_element_located([bywhat,valueofwhat])
    try:
        WebDriverWait(driver,timeout).until(found,message)
        return True
    except:
        return False


def creating_multiple_accounts(driver):
    for i in range(10):
        logut_if_logged_in(driver)
        go_to_signup_page(driver)
        username = "TestUser"+str(i)
        password = "TestUserPassword"+str(i)+"."
        email = str(i)+"@testmail.com"
        signup(driver, username, password, email)


options = webdriver.ChromeOptions()
#options.add_argument("headless")
driver = webdriver.Chrome(options=options)
driver.get("http://127.0.0.1:5000/")
try:
    creating_multiple_accounts(driver)
except:
    make_screenshot(driver)
time.sleep(3)
make_screenshot(driver)

