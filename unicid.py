#permite fazer as automaçoes
from selenium import webdriver

#permite uso de teclado
from selenium.webdriver.common.keys import Keys

#permite encontrar elementos
from selenium.webdriver.common.by import By

#permite trabalhar com dropDown
from selenium.webdriver.support.select import Select

from time import sleep 

#Burlar o repCaptcha
import pyautogui

numero_rgm = 35717424
senha_aluno = 46706

#Abrir o navegador
driver = webdriver.Chrome()

#Digitar o site da unicid
driver.get('https://www.unicid.edu.br/')
driver.maximize_window()
sleep(10)

#Entrar na Central do aluno
botao_central_aluno = driver.find_element(By.XPATH,"//a[@id='btnTOPBAR-SouAluno']")
botao_central_aluno.click()
sleep(10)

#Area do aluno
driver.get('https://novoportal.cruzeirodosul.edu.br/?empresa=unicid&blackboard=false')
driver.maximize_window()
sleep(10)


#Entrar na area do aluno

aluno_acesso = driver.find_element(By.XPATH,"//input[@id='txt-rgmcpf']")
aluno_acesso.click()
sleep(10)

#Digitar RGM
digita_rgm = driver.find_element(By.XPATH, "//input[@id='txt-rgmcpf']")

#Digita o rgm automatico devido a declaração no inicio do codigo.
digita_rgm.send_keys(numero_rgm)
sleep(15)

#Digitar a senha
digita_senha = driver.find_element(By.XPATH,"//input[@id='txt-senha']")

#Digita a senha declarada no inicio 
digita_senha.send_keys(senha_aluno)
sleep(10)
