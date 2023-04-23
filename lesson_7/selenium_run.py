from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC



def run():
    start_urls = "http://quotes.toscrape.com/login"

    driver = webdriver.Firefox(executable_path="/snap/bin/geckodriver")
    driver.get(url=start_urls)
   
    WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.ID, "username")))

    login = driver.find_element(By.ID, "username")
    password = driver.find_element(By.ID, "password")

    login.send_keys("admin")
    password.send_keys("admin")
    login_btn = driver.find_element(By.XPATH, "//input[@value='Login']")
    
    login_btn.click()

    WebDriverWait(driver, 120).until(EC.presence_of_element_located((By.CLASS_NAME, "quote")))

    html = driver.page_source
    quotes = driver.find_elements(By.CLASS_NAME, "quote")

    print(html)
    print(f"Количество цитат равно {len(quotes)}")

    driver.quit()

if __name__ == "__main__":
    run()