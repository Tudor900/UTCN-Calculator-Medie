import chromedriver_autoinstaller
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options





chrome_options = Options()
chrome_options.add_argument("--headless")  # Run Chrome in headless mode
chrome_options.add_argument("--disable-gpu")  # Disabling GPU acceleration

def launch_selenium(username, password):
    chromedriver_autoinstaller.install()

    driver = webdriver.Chrome(options=chrome_options)

    driver.get("https://websinu.utcluj.ro/note/default.asp")

    username_field = driver.find_element(By.NAME, "username")
    password_field = driver.find_element(By.NAME, "password")

    username_field.send_keys(username)
    password_field.send_keys(password)

    submit_button = driver.find_element(By.NAME, "submit")
    submit_button.click()

    # WebDriverWait(driver, 10).until(EC.url_changes("https://websinu.utcluj.ro/note/default.asp"))

    link_element = driver.find_element(By.XPATH, '//a[@href="javascript: NoteSesiuneaCurenta(\'Facultatea de Electronica,Telecomunicatii si Tehnologia Informatiei\', \'Inginerie Electronica,Telecomunicatii  si Tehn.Inform.(engleza)-lic\')"]')
    link_element.click()

    marks_file = open("marks.txt", "w")

    rows = driver.find_elements(By.XPATH, '//table[@class="table"]/tbody/tr[td[contains(text(), "Nota")]]')

    for row in rows:
        marks_file.write(row.text + "\n")

    marks_file.close()
    driver.quit()