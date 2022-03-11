
def gai_info(car):
    import time
    from selenium import webdriver
    from selenium.webdriver.common.keys import Keys
    from selenium.webdriver.common.by import By
    import random
    from fake_useragent import UserAgent
    from bs4 import BeautifulSoup
    from vin01_info import basic_vin01_info



    url = 'https://xn--90adear.xn--p1ai/check/auto/'


    # useragent = UserAgent()
    options = webdriver.ChromeOptions()
    # options.add_argument(f"user-agent={useragent.random}")
    # options.add_argument('headless')
    #set proxy
    #options.add_argument("--proxy-server=138.128.91.65:8888")

    driver = webdriver.Chrome(
        options=options
    )

    try:
        # check_vin = basic_vin01_info(car)
        # print(check_vin)
        # vin = check_vin[2]
        # print(vin)
        vin = 'TMBDK41U878855903'
        driver.get(url=url)
        time.sleep(2)
        search = driver.find_element(By.XPATH, '//*[@id="checkAutoVIN"]')
        search.send_keys(vin)
        time.sleep(5)
        driver.find_element(By.XPATH, '//*[@id="checkAutoHistory"]/p[4]/a').click()
        time.sleep(10)

        # search = driver.find_element(By.XPATH, '//*[@id="num"]')
        # search.send_keys(car)
        # time.sleep(0.5)
        # driver.find_element(By.XPATH, '//*[@id="searchByGosNumberButton"]').click()
        # time.sleep(5)
        # driver.find_element(By.XPATH, '//*[@id="getCheckButton"]').click()
        # time.sleep(2)






    except Exception as ex:
        print(ex)
        return None
    finally:
        driver.close()
        driver.quit()
        # return all_info


if __name__ == '__main__':

    car1 = 'А086ЕО116'
    # car1 = input('input car number: ')
    print(gai_info(car1))



