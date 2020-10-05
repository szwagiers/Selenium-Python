from selenium import webdriver
import urllib


driver = webdriver.Chrome(executable_path='c:\\Users\\szwagiers\\SeleniumDrivers\\chromedriver.exe')

driver.implicitly_wait(2)

driver.get('http://www.meteo.pl/um/php/gpp/search.php')

driver.find_element_by_name('name').send_keys('Gdynia')


driver.find_element_by_xpath('/html/body/table/tbody/tr[5]/td[2]/table/tbody/tr/td[2]/input').click()

driver.find_element_by_link_text('Gdynia').click()

handles = driver.window_handles()
driver.switch_to_window(handles[1])

driver.find_element_by_link_text('ZGADZAM SIĘ').click()


# driver.save_screenshot("weather.png")

