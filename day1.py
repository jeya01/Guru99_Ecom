from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select


def day1():
    driver = webdriver.Chrome()
    driver.implicitly_wait(5)

    url = "http://live.techpanda.org/index.php/"

    driver.get(url)
    driver.maximize_window()
    title1 = driver.title
    print("Home Page:", title1)
    '''Click Mobile'''
    driver.find_element(By.XPATH, "//*[@id='nav']/ol/li[1]/a").click()
    print("Mobile page:", driver.title)

    '''Selecting drop down'''
    element = driver.find_element(By.XPATH,
                                  "//*[@id='top']/body/div/div/div[2]/div/div[2]/div[1]/div[3]/div[1]/div[1]/div/select")
    '''Selecting option from the dropdown'''
    drop = Select(element)
    drop.select_by_index(1)
    # all_option = drop.options
    # for option in all_option:
    #     print(option.text)

    driver.close()

day1()
