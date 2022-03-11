from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import random
import time
from fake_useragent import UserAgent
from bs4 import BeautifulSoup

# Поиск фото авто
def nomerogram_images(car):

    url = 'https://www.nomerogram.ru/'

    useragent = UserAgent()
    options = webdriver.ChromeOptions()
    options.add_argument(f"user-agent={useragent.random}")
    # options.add_argument('headless')

    #set proxy
    #options.add_argument("--proxy-server=138.128.91.65:8888")

    driver = webdriver.Chrome(options=options)

    try:
        first_litter = car[0]
        three_numbers = car[1] + car[2] + car[3]
        other_litters = car[4] + car[5]
        if len(car) == 9:
            region = car[6] + car[7] + car[8]
        else:
            region = car[6] + car[7]

        number_lst = []

        number_lst.append(first_litter)
        number_lst.append(three_numbers)
        number_lst.append(other_litters)
        number_lst.append(region)

        driver.get(url=url)
        time.sleep(5)
        srch1 = driver.find_element(By.XPATH, '/html/body/div/main/form/div[2]/div[1]/div[1]/input[1]')
        srch2 = driver.find_element(By.XPATH, '/html/body/div/main/form/div[2]/div[1]/div[1]/input[2]')
        srch3 = driver.find_element(By.XPATH, '/html/body/div/main/form/div[2]/div[1]/div[1]/input[3]')
        srch4 = driver.find_element(By.XPATH, '/html/body/div/main/form/div[2]/div[1]/div[2]/input')
        srch1.send_keys(first_litter)
        srch2.send_keys(three_numbers)
        time.sleep(1)
        srch3.send_keys(other_litters)
        srch4.send_keys(region)
        time.sleep(2)

        btn = driver.find_element(By.XPATH, '/html/body/div/main/form/div[3]/button').click()
        time.sleep(8)
        soup = BeautifulSoup(driver.page_source, 'lxml')
        src_sorted = []
        all_img = []
        block = soup.find('div', class_='ng-list ng-list_theme_extended-info-card')
        all_img = block.find_all('img')
        src = []
        for item in all_img:
            src.append(item['src'])
        for i in range(len(src)):
            if src[i][0] == 'h':
                src_sorted.append(src[i])
        return src_sorted
    except Exception as ex:
        print(ex)
    finally:
        driver.close()
        driver.quit()


def basic_vin01_info(car):

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
        driver.get(url=url)
        time.sleep(2)
        search = driver.find_element(By.XPATH, '//*[@id="num"]')
        search.send_keys(car)
        time.sleep(0.5)
        btn1 = driver.find_element(By.XPATH, '//*[@id="searchByGosNumberButton"]').click()
        time.sleep(9)
        btn2 = driver.find_element(By.XPATH, '//*[@id="getCheckButton"]').click()
        time.sleep(4)

        soup = BeautifulSoup(driver.page_source, 'lxml')

        rows = soup.find("tbody").find_all("td")

        info = []
        for item in rows:
            info.append(item.text)

        mark_info = []
        name = soup.find("tbody").find_all("th")
        for item in name:
            mark_info.append(item.text)

        year_info = info[4] + ' ' + info[5]
        volume_info = info[6] + ' ' + info[7]
        power_info = info[10] + ' ' + info[11]
        name_info = mark_info[0] + ' ' + mark_info[1]
        vin_info = info[14] + ' ' + info[15]
        body_info = info[16] + ' ' + info[17]
        owners_number = info[18] + ' ' + info[19]
        vin = info[15]

        all_info = []
        all_info.append(name_info)
        all_info.append(year_info)
        all_info.append(volume_info)
        all_info.append(power_info)
        all_info.append(vin_info)
        all_info.append(owners_number)

        return all_info

    except Exception as ex:
        print(ex)
        return None
    finally:
        driver.close()
        driver.quit()


def basic_avtokod_info(car):

    url = 'https://avtocod.ru/'

    useragent = UserAgent()
    options = webdriver.ChromeOptions()
    options.add_argument(f"user-agent={useragent.random}")
    # options.add_argument('headless')

    # set proxy
    # options.add_argument("--proxy-server=138.128.91.65:8888")

    driver = webdriver.Chrome(options=options)

    try:
        driver.get(url=url)
        time.sleep(5)
        search = driver.find_element(By.XPATH, '//*[@id="check-head"]/div/div[2]/div/div/input')

        search.send_keys(car)
        time.sleep(1)
        search.send_keys(Keys.ENTER)
        time.sleep(5)
        name_info = driver.find_element(By.XPATH, '//*[@id="identifiers"]/div[1]/ul[1]/li[1]/div/div/div[2]/span')
        year_info = driver.find_element(By.XPATH, '//*[@id="names"]/div/div/div/div[2]/div[2]/div[1]/div/div[2]/h1/span')
        volume_info = driver.find_element(By.XPATH, '//*[@id="identifiers"]/div[1]/ul[2]/li[5]/div/div/div[2]/span')
        power_info = driver.find_element(By.XPATH, '//*[@id="identifiers"]/div[1]/ul[2]/li[6]/div/div/div[2]/span')

        car_info = []
        car_info.append(name_info.text)
        car_info.append(year_info.text)
        car_info.append(volume_info.text)
        car_info.append(power_info.text)

        return car_info

    except Exception as ex:
        print(ex)
        return None
    finally:
        driver.close()
        driver.quit()


if __name__ == '__main__':
    car = 'В625Ре116'
    print(nomerogram_images(car))
    print(basic_vin01_info(car))
    print(basic_avtokod_info(car))


