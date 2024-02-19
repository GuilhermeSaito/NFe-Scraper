import time
from selenium import webdriver

# Parece que com o selenium mais recente, nao precisa usar mais o webdriver.
driver = webdriver.Chrome()


# navigate to the Google homepage
driver.get("https://www.nfe.fazenda.gov.br/portal/consultaRecaptcha.aspx?tipoConsulta=resumo")

driver.delete_all_cookies()

# get the Google name
google_name = driver.title

# print the Google name
print('Google name:', google_name)

# //*[@id="ctl00_ContentPlaceHolder1_txtChaveAcessoResumo"]

time.sleep(2)

# close the browser window
driver.quit()
