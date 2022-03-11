# Поиск фото авто
def nomerogram_images(car):

    from selenium import webdriver
    from selenium.webdriver.common.keys import Keys
    from selenium.webdriver.common.by import By
    import random
    import time
    from fake_useragent import UserAgent
    from bs4 import BeautifulSoup

    url = 'https://www.nomerogram.ru/'
    # car = 'А087ЕО116'

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
        # print(number_lst)
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

if __name__ == '__main__':
    car = 'В625Ре116'
    print(nomerogram_images(car))


