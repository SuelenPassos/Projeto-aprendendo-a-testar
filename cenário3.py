#-- coding: utf-8 --
from selenium import webdriver
from time import sleep
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains

#Cenário 3: Verificar a obrigatoriedade do campo nome

#Abrindo a página
driver = webdriver.Firefox ()
driver.maximize_window() 
driver.get('http://www.aprendendotestar.com.br/treinar-automacao.php')

driver.save_screenshot('/home/suelen/Documentos/Aprendendo a testar/evidencias_aprendendotestar/cenário3/1_Tela inicial.png')

#preencher o campo usuário
usuario = driver.find_element_by_xpath('/html/body/section/section[2]/div/form/table/tbody/tr[2]/td/input')
usuario.send_keys('SXP')

#preencher o campo senha
senha = driver.find_element_by_xpath('/html/body/section/section[2]/div/form/table/tbody/tr[4]/td/input')
senha.send_keys('123456')

#verificar o campo nome
nome = driver.find_element_by_xpath('/html/body/section/section[2]/div/form/table/tbody/tr[6]/td/input')

sleep (3)

#clicar no botao enviar 
clicar = driver.find_element_by_xpath('/html/body/section/section[2]/div/form/table/tbody/tr[7]/td/input') 
actions = ActionChains(driver)
actions.click(clicar).perform()

sleep(5)

try:
    texto = driver.find_element_by_xpath('//*[contains(text(),"Existem campos em branco.")]')
    print('Teste passou')
except:
    print('Teste não passou')


driver.save_screenshot('/home/suelen/Documentos/Aprendendo a testar/evidencias_aprendendotestar/cenário3/2_Mensagem de crítica.png')
sleep(5)

driver.quit()
