from selenium import webdriver


driver = webdriver.Chrome(executable_path='c:\\Users\\szwagiers\\SeleniumDrivers\\chromedriver.exe')
# each time wait 2s, to load element
driver.implicitly_wait(2)
# open weather forecast search engine
driver.get('http://www.meteo.pl/um/php/gpp/search.php')
# input city name
driver.find_element_by_name('name').send_keys('Gdynia')
# click search
driver.find_element_by_xpath('/html/body/table/tbody/tr[5]/td[2]/table/tbody/tr/td[2]/input').click()
# find weather forecast for cities
driver.find_element_by_link_text('Gdynia').click()
# return all handle values of opened browser windows
handles = driver.window_handles

# for each site print handle and title
for h in handles:
    driver.switch_to.window(h)
    print(h)
    print(driver.title)
    # for the site with diagram accept privacy policy and screenshot the diagram
    if driver.title == 'Meteorogramy - meteorograms':
        driver.find_element_by_xpath('//*[@id="qc-cmp2-ui"]/div[2]/div/button[2]').click()
        driver.save_screenshot("weather.png")

# quit session
driver.quit()





