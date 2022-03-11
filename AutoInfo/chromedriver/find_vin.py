import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import random
from fake_useragent import UserAgent
from bs4 import BeautifulSoup

url = 'https://vin01.ru/'


useragent = UserAgent()
options = webdriver.ChromeOptions()
options.add_argument(f"user-agent={useragent.random}")
# options.add_argument('headless')
#set proxy
#options.add_argument("--proxy-server=138.128.91.65:8888")

driver = webdriver.Chrome(
    options=options
)

try:
    car = 'У932НР116'
    driver.get(url=url)
    time.sleep(2)
    search = driver.find_element(By.XPATH, '//*[@id="num"]')
    search.send_keys(car)
    time.sleep(0.5)
    btn1 = driver.find_element(By.XPATH, '//*[@id="searchByGosNumberButton"]').click()
    time.sleep(9)
    soup = BeautifulSoup(driver.page_source, 'lxml')
    block = soup.find('select', class_='form-control')
    vin1 = block.find('option').text




    print(block)
    print(vin1)

    # btn2 = driver.find_element(By.XPATH, '//*[@id="getCheckButton"]').click()
    # time.sleep(4)
    #

    #
    # rows = soup.find("tbody").find_all("td")
    #
    # info = []
    # for item in rows:
    #     info.append(item.text)
    #
    # mark_info = []
    # name = soup.find("tbody").find_all("th")
    # for item in name:
    #     mark_info.append(item.text)
    #
    # # year_info = info[4] + ' ' + info[5]
    # # volume_info = info[6] + ' ' + info[7]
    # # power_info = info[10] + ' ' + info[11]
    # # name_info = mark_info[0] + ' ' + mark_info[1]
    # # vin_info = info[14] + ' ' + info[15]
    # # body_info = info[16] + ' ' + info[17]
    # # owners_number = info[18] + ' ' + info[19]
    # year_info =info[5]
    # volume_info = info[7]
    # power_info = info[11]
    # name_info = mark_info[1]
    # vin_info = info[15]
    # # body_info = info[17]
    # #owners_number - серия и номер ПТС
    # owners_number = info[19]
    #
    #
    # all_info = []
    # all_info.append(name_info)
    # all_info.append(year_info)
    # all_info.append(volume_info)
    # all_info.append(power_info)
    # all_info.append(vin_info)
    # all_info.append(owners_number)
    #
    # # print(all_info)
    # # time.sleep(5)
    # return all_info

except Exception as ex:
    print(ex)
    # return None
finally:
    driver.close()
    driver.quit()
    # return all_info


# if __name__ == '__main__':
#
#     car1 = 'У932НР116'
#     # car1 = input('input car number: ')
#     print(basic_vin01_info(car1))