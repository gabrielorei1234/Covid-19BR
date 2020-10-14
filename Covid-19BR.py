import requests
import selenium
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
import time
import re
#Declaração de variáveis
url = "https://covid.saude.gov.br"
option          = Options()
option.headless = True
Path            = "C:\\Users\\gabri\\miniconda3\\Lib\\site-packages\\geckodriver\\geckodriver.exe"
driver = webdriver.Firefox(options=option,executable_path=Path)
#1 pegar o conteudo html a partir da url
driver.get(url)
time.sleep(1)

#Pegar os Casos Totais
TotalCases = driver.find_element_by_xpath("/html/body/app-root/ion-app/ion-router-outlet/app-home/ion-content/painel-geral-component/div/card-totalizadores-component/div/div[2]/div[2]/div[1]").text
SplitString         =  re.split("\nAcumulado", TotalCases)
TotalCases = SplitString[0]

#Casos Novos
NewCases = driver.find_element_by_xpath("/html/body/app-root/ion-app/ion-router-outlet/app-home/ion-content/painel-geral-component/div/card-totalizadores-component/div/div[2]/div[2]/div[2]").text
SplitString         =  re.split("\nCasos novos", NewCases)
NewCases = SplitString[0]

#Incidência
Incidencia = driver.find_element_by_xpath("/html/body/app-root/ion-app/ion-router-outlet/app-home/ion-content/painel-geral-component/div/card-totalizadores-component/div/div[2]/div[3]/div").text
SplitString         =  re.split("\nIncidência*", Incidencia)
Incidencia = SplitString[0]

#Óbitos acumulados
deaths = driver.find_element_by_xpath("/html/body/app-root/ion-app/ion-router-outlet/app-home/ion-content/painel-geral-component/div/card-totalizadores-component/div/div[3]/div[2]/div[1]").text
SplitString         =  re.split("\nÓbitos acumulados", deaths)
deaths = SplitString[0]

#Casos confirmados na morte
deathscases = driver.find_element_by_xpath("/html/body/app-root/ion-app/ion-router-outlet/app-home/ion-content/painel-geral-component/div/card-totalizadores-component/div/div[3]/div[2]/div[2]").text
SplitString         =  re.split("\nCasos novos", deathscases)
deathscases = SplitString[0]

#letalidade
letalidade = driver.find_element_by_xpath("/html/body/app-root/ion-app/ion-router-outlet/app-home/ion-content/painel-geral-component/div/card-totalizadores-component/div/div[3]/div[3]/div[1]").text
SplitString         =  re.split("\nLetalidade", letalidade)
letalidade = SplitString[0]

#Mortalidade
mortalidade = driver.find_element_by_xpath("/html/body/app-root/ion-app/ion-router-outlet/app-home/ion-content/painel-geral-component/div/card-totalizadores-component/div/div[3]/div[3]/div[2]").text
SplitString         =  re.split("\nMortalidade*", mortalidade)
mortalidade = SplitString[0]

#Casos Curados
curados = driver.find_element_by_xpath("/html/body/app-root/ion-app/ion-router-outlet/app-home/ion-content/painel-geral-component/div/card-totalizadores-component/div/div[1]/div[1]").text
SplitString         =  re.split("Casos recuperados\n", curados)
curados = SplitString[1]

#Acompanhamento
andamento = driver.find_element_by_xpath("/html/body/app-root/ion-app/ion-router-outlet/app-home/ion-content/painel-geral-component/div/card-totalizadores-component/div/div[1]/div[2]").text
SplitString         =  re.split("Em acompanhamento\n", andamento)
andamento = SplitString[0]


print("Casos totais: " + TotalCases + " registrados.")
print("Novos casos: " + NewCases + " registrados.")
print("Incidência: " + Incidencia + " registrada.")
print("Casos totais: " + deaths + " registrados.")
print("Total de Óbitos: " + deathscases + " registrados.")
print("Letalidade: " + letalidade + " registrada.")
print("Mortalidade: " + mortalidade + " registrada.")
print("Casos Curados: " + curados + " registrados.")
print("Em acompanhamento: " + andamento + " registrados.")

print("Informações retiradas de: " + url)



driver.quit()
