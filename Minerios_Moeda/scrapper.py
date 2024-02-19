import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
# from selenium.webdriver.common.action_chains import ActionChains

options = Options()
options.add_argument("--headless")

# Parece que com o selenium mais recente, nao precisa usar mais o webdriver.
driver = webdriver.Chrome(
    options = options
    )


# navigate to the Google homepage
driver.get("https://br.investing.com/commodities/copper-historical-data?cid=959211")

dropdown_menu = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[1]/div[2]/div[2]/div[2]/div[1]/div[2]/div[2]/div[1]/div[2]")))
dropdown_menu.click()

# Wait for the options to be visible and click the desired option
option = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, "/html/body/div[1]/div[2]/div[2]/div[2]/div[1]/div[2]/div[2]/div[1]/div[2]/div/div[3]")))
option.click()

table = driver.find_element(By.XPATH, "/html/body/div[1]/div[2]/div[2]/div[2]/div[1]/div[2]/div[3]/table")

rows = table.find_elements(By.TAG_NAME, "tr")

for row in rows:
    cells = row.find_elements(By.TAG_NAME, "td")
    
    # Iterate over the cells
    for cell in cells:
        # Print the cell text
        print(cell.text)


# driver.delete_all_cookies()

# # get the Google name
# google_name = driver.title

# # print the Google name
# print('Google name:', google_name)

# //*[@id="ctl00_ContentPlaceHolder1_txtChaveAcessoResumo"]

# ActionChains(driver) \
#     .click(clickable) \
#     .perform()
# select = Select(select_element)



# option_list = select.options

# print(option_list)

time.sleep(2)

# close the browser window
driver.quit()
