#-- coding: utf-8 --
from selenium import webdriver
from time import sleep
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains

#Cenário 2: Verificar a obrigatoriedade do campo senha

#Abrindo a página
driver = webdriver.Firefox ()
driver.maximize_window() 
driver.get('http://www.aprendendotestar.com.br/treinar-automacao.php')

driver.save_screenshot('/home/suelen/Documentos/Aprendendo a testar/evidencias_aprendendotestar/cenário2/1_Tela inicial.png')

#preencher o campo usuário
usuario = driver.find_element_by_xpath('/html/body/section/section[2]/div/form/table/tbody/tr[2]/td/input')
usuario.send_keys('SXP')

#verificar se o campo senha está vazio
senha = driver.find_element_by_xpath('/html/body/section/section[2]/div/form/table/tbody/tr[4]/td/input')
if senha.get_attribute('required'): 
    if senha.text == '':
        print('Teste passou')
else:
    print ('Teste não passou')

#clicar no botao enviar 
clicar = driver.find_element_by_xpath('/html/body/section/section[2]/div/form/table/tbody/tr[7]/td/input') 
actions = ActionChains(driver)
actions.click(clicar).perform()

sleep(5)
driver.save_screenshot('/home/suelen/Documentos/Aprendendo a testar/evidencias_aprendendotestar/cenário2/2_Mensagem de crítica.png')
sleep(5)

driver.quit()
