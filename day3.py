import time

from selenium import webdriver
from selenium.webdriver.common.by import By


def day3():
    driver = webdriver.Chrome()
    driver.set_page_load_timeout(5)
    url = "http://live.techpanda.org/index.php/"

    driver.get(url)
    driver.maximize_window()

    '''Click on Mobile link'''
    driver.find_element(By.XPATH, "//*[@id='nav']/ol/li[1]/a").click()

    time.sleep(3)
    '''Click add to cart'''
    driver.find_element(By.XPATH,"//*[@id='top']/body/div/div/div[2]/div/div[2]/div[1]/div[3]/ul/li[1]/div/div[3]/button").click()

    '''clear the quantity box'''
    driver.find_element(By.XPATH,"//*[@id='shopping-cart-table']/tbody/tr/td[4]/input").clear()

    '''give 1000 as input '''
    driver.find_element(By.XPATH, "//*[@id='shopping-cart-table']/tbody/tr/td[4]/input").send_keys(1000)

    '''click update button'''
    driver.find_element(By.XPATH,"//*[@id='shopping-cart-table']/tbody/tr/td[4]/button").click()

    '''print the error message'''
    print(driver.find_element(By.XPATH,"//*[@id='top']/body/div/div/div[2]/div/div/div/ul/li/ul/li/span").text)

    '''click empty cart link'''
    driver.find_element(By.XPATH," //*[@id='empty_cart_button']").click()

    '''verify the message SHOPPING CART IS EMPTY '''
    cart_empty = driver.find_element(By.XPATH,"//*[@id='top']/body/div/div/div[2]/div/div/div/h1").text
    if cart_empty == "SHOPPING CART IS EMPTY":
        print("The cart is empty")
    else:
        print("cart is not cleared")

    time.sleep(3)
    driver.close()

day3()
