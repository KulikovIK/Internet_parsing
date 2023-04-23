import time
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains

def run():
    start_urls = "https://quotes.toscrape.com/scroll"

    profile = webdriver.FirefoxProfile()
    profile.set_preference("permissions.default.image", 2)
    profile.set_preference("dom.ipc.plugins.enabled.libflashplayer.so", "false")

    options = Options()
    options.add_argument("--headless")

    driver = webdriver.Firefox(
        firefox_profile=profile,
        options=options,
        executable_path="/snap/bin/geckodriver")
    
    driver.get(url=start_urls)

    WebDriverWait(driver, 120).until(EC.presence_of_element_located((By.CLASS_NAME, "quotes")))
    body_height = driver.execute_script("return document.body.scrollHeight")

    pause_time = 0.5

    # Получение данных методом прокрутки страницы "скролом" до конца
    # while True:
    #     driver.execute_script(f"window.scrollTo(0, {body_height});")
    #     new_height = driver.execute_script("return document.body.scrollHeight")
    #     time.sleep(pause_time)
    #     if new_height == body_height:
    #         break
    #     body_height = new_height
    
    actions = ActionChains(driver)

    # Получение данных методом прокрутки страницы клавишей "пробел" до конца
    while True:
        for _ in range(3):
            actions.send_keys(Keys.SPACE).perform()
            time.sleep(pause_time)
        new_height = driver.execute_script("return document.body.scrollHeight")
        
        if new_height == body_height:
            break
        body_height = new_height

    quotes = driver.find_elements(By.CLASS_NAME, "quote")
    print(f"Количество цитат равно {len(quotes)}")
    time.sleep(pause_time)
    driver.quit()

if __name__ == "__main__":
    run()