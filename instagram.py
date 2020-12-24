from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()

driver.get("https://www.instagram.com")

# Sign in
try:
    sign_in = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located(
            (By.XPATH, "//*[@id='loginForm']/div/div[3]"))
    )
    username = driver.find_element_by_name("username")
    password = driver.find_element_by_name("password")

    username.send_keys("alisar.musa")
    password.send_keys("***")

    sign_in.click()
except:
    driver.quit()


def profile_menu():
    # My Profile
    try:
        my_profile = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located(
                (By.XPATH, "//*[@id='react-root']/section/nav/div[2]/div/div/div[3]/div/div[5]/span"))
        )
        my_profile.click()
    except:
        driver.quit()

    # Settings
    try:
        settings = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located(
                (By.XPATH,
                 "//*[@id='react-root']/section/nav/div[2]/div/div/div[3]/div/div[5]/div[2]/div[2]/div[2]/a[3]/div"))
        )
        settings.click()
    except:
        driver.quit()

    # Privacy
    try:
        privacy = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located(
                (By.XPATH, "//*[@id='react-root']/section/main/div/ul/li[7]/a"))
        )
        privacy.click()
    except:
        driver.quit()

    # Account Data
    try:
        account_data = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located(
                (By.XPATH, "//*[@id='react-root']/section/main/div/article/main/section[6]/a"))
        )
        account_data.click()
    except:
        driver.quit()


# Find All Username
def find_all_username(name):
    while True:
        try:
            more_button = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located(
                    (By.XPATH, "//*[@id='react-root']/section/main/div/article/main/button"))
            )
            more_button.click()
        except:
            break
    try:
        section = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located(
                (By.XPATH, "///*[@id='react-root']/section/main/div/article/main/section"))
        )
        f = open(name + ".txt", "w+")
        f.write(section.text)
        f.close()
    except:
        driver.quit()


# You Follow
try:
    accounts_you_follow = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located(
            (By.XPATH, "//*[@id='react-root']/section/main/div/article/main/div/div[2]/section[1]/section[3]/a"))
    )
    accounts_you_follow.click()
except:
    driver.quit()

find_all_username("you_follow")

# Following You
try:
    backHome = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located(
            (By.XPATH, "//*[@id='react-root']/section/nav/div[2]/div/div/div[1]/a/div/div"))
    )
    backHome.click()
except:
    driver.quit()

profile_menu()

try:
    accounts_following_you = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located(
            (By.XPATH, "//*[@id='react-root']/section/main/div/article/main/div/div[2]/section[1]/section[2]/a"))
    )
    accounts_following_you.click()
except:
    driver.quit()

find_all_username("following_you")


# Create Username List
def create_list(name, user_list):
    f = open(name + ".txt", "r")
    for x in f:
        x = x.strip("\n")
        user_list.append(x)


you_follow = []
following_you = []

create_list("you_follow", you_follow)
create_list("following_you", following_you)

# Find Unfollowers
for i in you_follow:
    if i not in following_you:
        print(i)

driver.implicitly_wait(15)

