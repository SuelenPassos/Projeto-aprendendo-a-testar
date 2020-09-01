#-- coding: utf-8 --
from selenium import webdriver
from time import sleep
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains

#Cenário 4: Verificar inclusão dos dados na tabela usuarios

#Abrindo a página
driver = webdriver.Firefox ()
driver.maximize_window() 
driver.get('http://www.aprendendotestar.com.br/treinar-automacao.php')

driver.save_screenshot('/home/suelen/Documentos/Aprendendo a testar/evidencias_aprendendotestar/cenário4/1_Tela inicial.png')


#preencher o campo usuário
usuario = driver.find_element_by_xpath('/html/body/section/section[2]/div/form/table/tbody/tr[2]/td/input')
usuario.send_keys('SXP')

#preencher o campo senha
senha = driver.find_element_by_xpath('/html/body/section/section[2]/div/form/table/tbody/tr[4]/td/input')
senha.send_keys('123456')


#preencher o campo nome
nome = driver.find_element_by_xpath('/html/body/section/section[2]/div/form/table/tbody/tr[6]/td/input')
nome.send_keys('Suelen Passos')


driver.save_screenshot('/home/suelen/Documentos/Aprendendo a testar/evidencias_aprendendotestar/cenário4/2_Preenchimento de dados.png')

sleep (5)

#clicar no botao enviar 
clicar = driver.find_element_by_xpath('/html/body/section/section[2]/div/form/table/tbody/tr[7]/td/input') 
actions = ActionChains(driver)
actions.click(clicar).perform()

sleep (5)


#verificar usuario
try:
    usuario = driver.find_element_by_xpath('//*[contains(text(),"SXP")]')
    print('Teste passou')
except:
    print('Teste não passou')
    
#verificar senha
try:
    senha = driver.find_element_by_xpath('//*[contains(text(),"123456")]')
    print('Teste passou')
except:
    print('Teste não passou')

#verificar nome
try:
    nome = driver.find_element_by_xpath('//*[contains(text(),"Suelen Passos")]')
    print('Teste passou')
except:
    print('Teste não passou')


sleep(5)
driver.save_screenshot('/home/suelen/Documentos/Aprendendo a testar/evidencias_aprendendotestar/cenário4/3_Inclusão de dados.png')
sleep(5)


driver.quit()
