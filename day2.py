import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select


def day2():
    driver = webdriver.Chrome()
    driver.implicitly_wait(5)

    url = "http://live.techpanda.org/index.php/"

    driver.get(url)
    driver.maximize_window()
    title1 = driver.title
    print("Home Page:", title1)
    '''Click mobile'''
    driver.find_element(By.XPATH, "//*[@id='nav']/ol/li[1]/a").click()
    print("Mobile page:", driver.title)

    '''select the product price in mobile page'''
    out = driver.find_element(By.CSS_SELECTOR,"#product-price-1 > span").text

    '''Click sony Xperia'''
    driver.find_element(By.XPATH,"//*[@id ='product-collection-image-1']").click()

    '''find the price after clicking Xperia'''
    out1=driver.find_element(By.CSS_SELECTOR,"#product-price-1 > span").text

    '''Verify the price'''
    if out1 == out:
        print("Price matches")
    else:
        print("Price doesnt match")

    time.sleep(5)
    driver.close()



day2()