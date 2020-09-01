#-- coding: utf-8 --
from selenium import webdriver
from time import sleep
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains

#Cenário 5: Verificar ordenação da tabela usuarios

#Abrindo a página
driver = webdriver.Firefox ()
driver.maximize_window() 
driver.get('http://www.aprendendotestar.com.br/treinar-automacao.php')

driver.save_screenshot('/home/suelen/Documentos/Aprendendo a testar/evidencias_aprendendotestar/cenário5/1_Tela inicial.png')


#inclusão de registro 1
#preencher o campo usuário
usuario = driver.find_element_by_xpath('/html/body/section/section[2]/div/form/table/tbody/tr[2]/td/input')
usuario.send_keys('SXP')
#preencher o campo senha
usuario = driver.find_element_by_xpath('/html/body/section/section[2]/div/form/table/tbody/tr[4]/td/input')
usuario.send_keys('abc@12')
#preencher o campo nome
usuario = driver.find_element_by_xpath('/html/body/section/section[2]/div/form/table/tbody/tr[6]/td/input')
usuario.send_keys('Suelen Passos')
#clicar no botao enviar 
clicar = driver.find_element_by_xpath('/html/body/section/section[2]/div/form/table/tbody/tr[7]/td/input') 
actions = ActionChains(driver)
actions.click(clicar).perform()

driver.save_screenshot('/home/suelen/Documentos/Aprendendo a testar/evidencias_aprendendotestar/cenário5/2_Inclusão de dados1.png')


sleep (3)

#inclusão de registro 2
#preencher o campo usuário
usuario = driver.find_element_by_xpath('/html/body/section/section[2]/div/form/table/tbody/tr[2]/td/input')
usuario.send_keys('JP')
#preencher o campo senha
usuario = driver.find_element_by_xpath('/html/body/section/section[2]/div/form/table/tbody/tr[4]/td/input')
usuario.send_keys('12091988')
#preencher o campo nome
usuario = driver.find_element_by_xpath('/html/body/section/section[2]/div/form/table/tbody/tr[6]/td/input')
usuario.send_keys('Joao Paulo')
#clicar no botao enviar 
clicar = driver.find_element_by_xpath('/html/body/section/section[2]/div/form/table/tbody/tr[7]/td/input') 
actions = ActionChains(driver)
actions.click(clicar).perform()

driver.save_screenshot('/home/suelen/Documentos/Aprendendo a testar/evidencias_aprendendotestar/cenário5/3_Inclusão de dados2.png')

sleep (5)

driver.save_screenshot('/home/suelen/Documentos/Aprendendo a testar/evidencias_aprendendotestar/cenário5/4_Lista ordenada.png')



try:
    nomes = driver.find_elements_by_xpath("//tbody[tr(@td)]")
    
    print('Teste passou') 
except:
    print('Teste não passou')
    



driver.quit()

