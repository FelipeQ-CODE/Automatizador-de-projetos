#permite fazer as automaçoes
from selenium import webdriver


#permite uso de teclado
from selenium.webdriver.common.keys import Keys

#permite encontrar elementos
from selenium.webdriver.common.by import By

#permite trabalhar com dropDown
from selenium.webdriver.support.select import Select

from time import sleep 

numero_oab = 133864

driver = webdriver.Chrome()

#Entrar no site da 
driver.get('https://pje1g.trf3.jus.br/pje/ConsultaPublica/listView.seam')
sleep(15)

#Digitar o Numero do OAB 
campo_oab = driver.find_element(By.XPATH,"//input[@id='fPP:Decoration:numeroOAB']")
#digitando dentro do campo desejado.
campo_oab.send_keys(numero_oab)

#Selecionar o estado 
dropdown_estados = driver.find_element(By.XPATH,"//select[@id='fPP:Decoration:estadoComboOAB']") 
opcoes_estados = Select(dropdown_estados)

#Abre a aba e ja digita SP
opcoes_estados.select_by_visible_text('SP')

#Clicar em pesquisar
botao_pesquisar = driver.find_element(By.XPATH,"//input[@id='fPP:searchProcessos']")
botao_pesquisar.click()
sleep(10)

#Fim do projeto o site da PJE nao da mais acesso a automação!
