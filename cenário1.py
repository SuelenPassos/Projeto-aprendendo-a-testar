#-- coding: utf-8 --
from selenium import webdriver
from time import sleep
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains

#Cenário 1 - Verificar a obrigatoriedade do campo usuario

#Abrindo a página
driver = webdriver.Firefox ()
driver.maximize_window() 
driver.get('http://www.aprendendotestar.com.br/treinar-automacao.php')

driver.save_screenshot('/home/suelen/Documentos/Aprendendo a testar/evidencias_aprendendotestar/cenário1/1_Tela inicial.png')

#verificar se o campo usuário está vazio
usuario = driver.find_element_by_xpath('/html/body/section/section[2]/div/form/table/tbody/tr[2]/td/input')

if usuario.get_attribute('required'): 
    if usuario.text == '':
        print('Teste passou')
    else:
        print('Campo preenchido')
else:
    print ('Teste não passou')

#clicar no botao enviar 
clicar = driver.find_element_by_xpath('/html/body/section/section[2]/div/form/table/tbody/tr[7]/td/input') 
actions = ActionChains(driver)
actions.click(clicar).perform()

sleep(5)
driver.save_screenshot('/home/suelen/Documentos/Aprendendo a testar/evidencias_aprendendotestar/cenário1/2_Mensagem de crítica.png')
sleep(5)

driver.quit()


