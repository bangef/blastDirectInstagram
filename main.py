#import lib and ignore warning decepretion log
from warnings import filterwarnings
filterwarnings("ignore")
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time, random, json, getpass

# array sebagai penampung dari data json
datasList = []

# membuka file data.txt, dan merubahnya menjadi dictionary value
with open('data.txt') as f:
    for jsonObj in f :
        dataDict = json.loads(jsonObj)
        datasList.append(dataDict)



#varibel penampung user instagram
myUsername = input("Masukan username anda : ")
myPassword = getpass.getpass(prompt="Masukan password anda : ")



#memberikan lama delay saat pesan users 1 sudah selesai:
between_massages = input(int("Masukan delay antar pesan : "))

browser = webdriver.Chrome('chromedriver.exe')

#authorization:
def auth(username, password):
    try:
        browser.get('https://www.instagram.com')
        time.sleep(random.randrange(2, 4))


        inputUsername = browser.find_element_by_name('username')
        inputPassword = browser.find_element_by_name('password')

        inputUsername.send_keys(username)
        time.sleep(random.randrange(1,2))
        inputPassword.send_keys(password)
        time.sleep(random.randrange(1,2))
        inputPassword.send_keys(Keys.ENTER)

    except Exception as err:
        print(err)
        browser.quit()

# sending massage
def sendMassage(data):
    try:
        browser.find_element_by_xpath('/html/body/div[1]/section/nav/div[2]/div/div/div[3]/div/div[2]/a').click()
        time.sleep(random.randrange(1, 3))

        browser.find_element_by_xpath('/html/body/div[5]/div/div/div/div[3]/button[2]').click()
        time.sleep(random.randrange(2, 3))

        browser.find_element_by_xpath('/html/body/div[1]/section/div/div[2]/div/div/div[2]/div/div[3]/div/button').click()
        time.sleep(random.randrange(1, 2))
        
        for data in datasList :

            inputUsersnameMassage = browser.find_element_by_name('queryBox')
            inputUsersnameMassage.send_keys(data["username"])
            time.sleep(random.randrange(4,5))

            browser.find_element_by_xpath('/html/body/div[5]/div/div/div[2]/div[2]/div[1]').click()
            time.sleep(random.randrange(4,5))            

            browser.find_element_by_xpath('/html/body/div[5]/div/div/div[1]/div/div[2]/div/button').click()
            time.sleep(random.randrange(4,5))

            makeTamplateWord(data["name"], data["massage"])
            
            time.sleep(random.randrange(4,5))

            browser.find_element_by_xpath('/html/body/div[1]/section/div/div[2]/div/div/div[2]/div[2]/div/div[2]/div/div/div[3]/button').click()
            time.sleep(random.randrange(4,5))

            print("pesan atas nama", data["username"], "berhasil terkirim")
            time.sleep(between_massages)

            browser.find_element_by_xpath('/html/body/div[1]/section/div/div[2]/div/div/div[1]/div[1]/div/div[3]/button').click()

        browser.quit()
    except Exception as err:
        print(err)
        browser.quit()

def makeTamplateWord(a, b):

    def enter2time():
        webdriver.ActionChains(browser).key_down(Keys.SHIFT).key_down(Keys.ENTER).key_up(Keys.ENTER).key_down(Keys.ENTER).key_up(Keys.ENTER).key_up(Keys.SHIFT).perform()
    def enter():
        webdriver.ActionChains(browser).key_down(Keys.SHIFT).key_down(Keys.ENTER).key_up(Keys.ENTER).key_up(Keys.SHIFT).perform()
    bar1 = browser.find_element_by_xpath('/html/body/div[1]/section/div/div[2]/div/div/div[2]/div[2]/div/div[2]/div/div/div[2]/textarea')
    bar1.send_keys(b)
    enter2time()
    bar1.send_keys(a)

# run program:
auth(myUsername, myPassword)
time.sleep(random.randrange(5,6))
sendMassage(datasList)

