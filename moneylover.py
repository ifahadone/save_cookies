import pickle
import secret
from selenium import webdriver
import time

options = webdriver.ChromeOptions()
# options.add_argument("--user-data-dir=/Users/me/Library/Application Support/Google/Chrome/Default")
# options.add_argument('--profile-directory=Profile 2')
driver = webdriver.Chrome('./driver/chromedriver', options=options)

driver.get('https://web.moneylover.me/')


def sign_in_get_cookies():
    time.sleep(3)
    login_email = '/html/body/div[1]/div/div[2]/div/div[2]/div[3]/form/div[1]/div/div[1]/div/input'
    login_paswd = '/html/body/div[1]/div/div[2]/div/div[2]/div[3]/form/div[2]/div/div[1]/div[1]/input'
    login_button = '/html/body/div[1]/div/div[2]/div/div[2]/div[3]/form/button'
    driver.find_element_by_xpath(login_email).send_keys(secret.moneyloverEmail)
    driver.find_element_by_xpath(login_paswd).send_keys(secret.moneyloverPswd)
    driver.find_element_by_xpath(login_button).click()
    input("wait")

    # STORE Cookies | PICKLE
    pickle.dump(driver.get_cookies(),
                open("cookies.pkl", "wb"))
    print('Saved')


def add_cookies():
    # ADD Cookies | PICKLE
    time.sleep(3)
    driver.delete_all_cookies()
    time.sleep(2)
    cookies = pickle.load(open("/Volumes/WorkLoad/Repositories/Implement/Payment-Invoice/Temp/cookies.pkl", "rb"))
    for cookie in cookies:
        print(cookie)
        driver.add_cookie(cookie)
    time.sleep(3)


if __name__ == '__main__':
    #ADD COOKIE
    # add_cookies()
    #SIGN IN AND SAVE COOKIES
    # sign_in_get_cookies()
    driver.get('https://web.moneylover.me/')
    # time.sleep(1)
    driver.refresh()
