def basic_avtokod_info(car):
        import time
        from selenium import webdriver
        from selenium.webdriver.common.keys import Keys
        from selenium.webdriver.common.by import By
        import random
        from fake_useragent import UserAgent

        url = 'https://avtocod.ru/'
        # car = 'А087ЕО116'

        useragent = UserAgent()
        options = webdriver.ChromeOptions()
        options.add_argument(f"user-agent={useragent.random}")
        # options.add_argument('headless')
        #set proxy
        #options.add_argument("--proxy-server=138.128.91.65:8888")

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
        car1 = 'У940РС197'
        # car1 = input('input car number: ')9
        print(basic_avtokod_info(car1))

