
from selenium import webdriver 
from selenium.webdriver.common.keys import Keys # works as keyboard keys, like enter or arrow keys
chromedriverpath = "L:/selenium chrome driver/chromedriver.exe"
driver = webdriver.Chrome(executable_path=chromedriverpath)


driver.get("http://secure-retreat-92358.herokuapp.com/")
# " https:// " this part is very important 
# =============================================================================
# we can use css select
#
##driver.find_element_by_xpath('//*[@id="articlecount"]/a[1]')
#
############### Clicking ################
# =============================================================================
# 
# number = driver.find_element_by_css_selector("#articlecount a") 
# #print(number.text)
# number.click()
# =============================================================================

# =============================================================================
# #click on url y just the text in the page
# 
# all_portals = driver.find_element_by_link_text("All portals")
# 
# all_portals.click()
# =============================================================================
############ enter key##########
# =============================================================================
# search = driver.find_element_by_name("search")
# search.send_keys("Python")
# search.send_keys(Keys.ENTER)
# =============================================================================

# =============================================================================
# 
# #try to fill the form in this link 
# #http://secure-retreat-92358.herokuapp.com/
# =============================================================================
###filling up the for####
first_name = driver.find_element_by_name("fName")
first_name.send_keys("testing")

last_name = driver.find_element_by_name("lName")
last_name.send_keys("Bin Sulaiman")

email = driver.find_element_by_name("email")
email.send_keys("Riwnasdgad@yahoo.com")

submit = driver.find_element_by_css_selector("button")
submit.click()





#driver.quit()
