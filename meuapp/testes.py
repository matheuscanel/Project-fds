from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from time import sleep
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
servico = Service(ChromeDriverManager().install())
navegador = webdriver.Chrome(service=servico)

navegador.get('http://127.0.0.1:8000/')
navegador.find_element('xpath', '/html/body/header/a[2]/button').click()
sleep(2)
navegador.find_element('xpath', '/html/body/form/input[2]').send_keys("Ricardinho")
sleep(2)
navegador.find_element('xpath', '/html/body/form/input[3]').send_keys("rac2@cesar.school")
sleep(2)
navegador.find_element('xpath', '/html/body/form/input[4]').send_keys("camisasnaNota10")
sleep(2)
navegador.find_element('xpath','/html/body/form/label[4]').click()
sleep(5)
navegador.find_element('xpath', '/html/body/form/input[5]').click()
sleep(2)
navegador.find_element('xpath','//*[@id="id_team_0"]').click()
sleep(5)
navegador.find_element('xpath','/html/body/form/button').click()
sleep(5)
navegador.find_element('xpath','/html/body/a/button').click()
sleep(5)
navegador.find_element('xpath', '/html/body/header/a[1]/button').click()
sleep(3)
navegador.find_element('xpath', '/html/body/form/input[2]').send_keys("Ricardinho")
sleep(3)
navegador.find_element('xpath', '/html/body/form/input[3]').send_keys("camisasnaNota10")
sleep(3)
navegador.find_element('xpath', '/html/body/form/input[4]').click()
sleep(3)
navegador.find_element('xpath', '/html/body/header/a[3]/button').click()
sleep(2)
navegador.find_element('xpath','//*[@id="id_comentario"]').send_keys("otima loja")
sleep(5)
navegador.find_element('xpath','/html/body/form/button[1]').click()
sleep(5)
navegador.find_element('xpath','//*[@id="id_comentario"]').clear()
sleep(5)
navegador.find_element('xpath', '/html/body/form/button[2]').click()
sleep(5)
navegador.find_element('xpath', '/html/body/footer/a[2]/button').click()
sleep(5)
navegador.find_element('xpath','/html/body/div[2]/a/button').click()
sleep(5)
navegador.find_element('xpath','/html/body/footer/a[2]/button').click()
sleep(5)
navegador.find_element('xpath','/html/body/div[2]/button').click()
sleep(5)
navegador.find_element('xpath','//*[@id="nome"]').send_keys("Ricardo")
sleep(5)
navegador.find_element('xpath','//*[@id="numero"]').send_keys("1234764209864398")
sleep(5)
navegador.find_element('xpath','//*[@id="expiracao_mes"]').send_keys("11")
sleep(5)
navegador.find_element('xpath','//*[@id="expiracao_ano"]').send_keys("2030")
sleep(5)
navegador.find_element('xpath','//*[@id="cvv"]').send_keys("387")
sleep(5)
navegador.find_element('xpath','//*[@id="payment-form"]/button').click()
sleep(5)