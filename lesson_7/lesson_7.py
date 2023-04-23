from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC



def run():
    start_urls = "https://www.scrapethissite.com/login/"

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

    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//input[@id='email']")))

    login = driver.find_element(By.XPATH, "//input[@id='email']")
    password = driver.find_element(By.XPATH, "//input[@id='password']")

    login.send_keys("admin@admin.com")
    password.send_keys("admin")
    login_btn = driver.find_element(By.XPATH, "//input[@value='Login →']")
    
    login_btn.click()

    WebDriverWait(driver, 120).until(EC.presence_of_element_located((By.XPATH, "//h4[@class='ui-pnotify-title']")))

    message = driver.find_element(By.XPATH, "//h4[@class='ui-pnotify-title']")

    print(message)

    driver.quit()

if __name__ == "__main__":
    run()
    