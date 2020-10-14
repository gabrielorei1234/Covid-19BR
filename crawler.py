import requests
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
import re

#Declaração de variáveis
url             = "https://www.melhorcambio.com/dolar-hoje"
option          = Options()
option.headless = True
Path            = "C:\\Users\\gabri\\miniconda3\\Lib\\site-packages\\geckodriver\\geckodriver.exe"
#1 pegar o conteudo html a partir da url

driver      = webdriver.Firefox(executable_path=Path)
driver.get(url)
element     = driver.find_element_by_id("comercial")
HtmlContent = element.get_attribute('outerHTML')
SplitString         =  re.split("value=", HtmlContent)
Aux                 =  re.split(" class=",SplitString[1])
print("O Dólar hoje está custando R$ " + Aux[0])

driver.quit()