import os.path


from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

WAIT_TIME = 10
userEmail='sulaemanr46@gmail.com'
userPassword='123456'
driver = webdriver.Chrome(executable_path=os.path.abspath("chromedriver"))
driver.get("https://dev-plaundry.herokuapp.com/login")
driver.find_element_by_id("formBasicEmail").send_keys(userEmail)
driver.find_element_by_id("formBasicPassword").send_keys(userPassword)
driver.find_element_by_class_name("btn.btn-primary.btn-block").click()



try:
    element = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, ".fnavbar"))
    )

    driver.get("https://dev-plaundry.herokuapp.com/order")

    element = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "formName"))
    )
    element.send_keys("ucok")
    driver.find_element_by_id("formAddress").send_keys("JL Kopo sayti 8 RT 05/07")
    driver.find_element_by_id("formno_telp").send_keys("6786687")


    select = Select(driver.find_element_by_id('type_cucian'))

    select.select_by_visible_text('Satuan')

    select = Select(driver.find_element_by_id('jenis_layanan'))
    select.select_by_visible_text('Reguler')

    select = Select(driver.find_element_by_id('layanan_kurir'))
    select.select_by_visible_text('Antar Saja')

    element = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.NAME, "nama"))
    )
    btn = driver.find_element_by_class_name("btn.btn-primary.btn-block")
    btn.click()
    # driver.find_elements_by_css_selector("btn.btn-primary.btn-block")[0].click()
    button = driver.find_element_by_link_text("Logout")
    button.click()
finally:
    # pass
    driver.quit()
