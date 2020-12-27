import selenium
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
import time



TheSite = input("What website would you like?\ncostco\ntarget\nwalmart\n\n>> ")


if TheSite == str("target"):
    PATH = "C:\Program Files (x86)\chromedriver.exe"
    driver = webdriver.Chrome(PATH)
    driver.get("https://www.target.com/")
    TargetItem = input("\nWhat item would you like to search for? >> ")
    targetsearch = driver.find_element_by_id("search")
    targetsearch.send_keys(TargetItem)
    targetsearch.send_keys(Keys.RETURN)

    anelement = WebDriverWait(driver,10).until(
        EC.presence_of_element_located((By.XPATH, "/html/body/div[1]/div/div[3]/div[2]/nav/div[1]/form/button[2]"))
    )
    anelement.click()

    target = WebDriverWait(driver,10).until(
        EC.presence_of_element_located((By.XPATH, "/html/body/div[1]/div/div[3]/div[2]/nav/div[1]/form/button[2]"))
    )
    target.click()



    asktarget = input("Would you like to search for another item? (y/n) >> ")
    if asktarget == str("y"):
        continueshopping = WebDriverWait(driver,10).until(
            EC.presence_of_element_located((By.XPATH, "/html/body/div[11]/div/div/div/div/div/div/div[2]/div[1]/button"))
        )
        continueshopping.click()

    else:
        print("Done")



if TheSite == str("walmart"):
    PATH = "C:\Program Files (x86)\chromedriver.exe"
    driver = webdriver.Chrome(PATH)
    driver.get("https://www.walmart.com/")
    WalmartItem = input("\nWhat item would you like to search for? >> ")
    print("Loading...")
    walmartsearch = driver.find_element_by_id("global-search-input")
    walmartsearch.send_keys(WalmartItem)
    walmartsearch.send_keys(Keys.RETURN)

    try:
        anelement = WebDriverWait(driver,10).until(
            EC.presence_of_element_located((By.LINK_TEXT, "Add to cart"))
        )
        anelement.click()


    except:
        print("Error Code 1")
        walmartsearch.clear()

    MoreWalmart = input("Would you like to add another item? (y/n) >> ")
    print("Loading...")

    if MoreWalmart == str("y"):
        secondWalmart = input("What item would you like to search for? >> ")
        secondWalmart = driver.find_element_by_id("global-search-input")
        secondWalmart.send_keys(WalmartItem)
        secondWalmart.send_keys(Keys.RETURN)


    if MoreWalmart == str("n"):
        print("Your list: " + str(WalmartItem))






if TheSite == str("costco"):
    PATH = "C:\Program Files (x86)\chromedriver.exe"
    driver = webdriver.Chrome(PATH)
    driver.get("https://www.costco.com/")
    CostcoItem = input("\nWhat item would you like to search for?\n >> ")
    costcosearch = driver.find_element_by_id("search-field")
    costcosearch.send_keys(CostcoItem)
    costcosearch.send_keys(Keys.RETURN)

    try:
        element = WebDriverWait(driver,10).until(
            EC.presence_of_element_located((By.XPATH, "/html/body/header/div[2]/div/div/div[2]/div[2]/div/div[2]/div/form/div[2]/button"))
        )
        element.click()

    except:
        time.sleep(200)
        driver.quit()


    ClickCostco = WebDriverWait(driver,10).until(
        EC.presence_of_element_located((By.CLASS_NAME, "thumbnail"))
    )
    ClickCostco.click()
    CostcoOne = driver.current_url

    CostcoAskAgain = input("Do you want to search for another item? (y/n)\n >> ")

    if CostcoAskAgain == str("y"):
        costconumbertwo = input("What item would you like to search for?\n >> ")

        #add rest of code here

    else:
        print("Your list of items: " +'"'+ str(CostcoOne)+'"')




    # costcoclick = driver.find_element_by_xpath("/html/body/header/div[2]/div/div/div[2]/div[2]/div/div[2]/div/form/div[2]/button")
    # costcoclick.click()

