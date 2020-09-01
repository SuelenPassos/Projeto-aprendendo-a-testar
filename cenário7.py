#-- coding: utf-8 --
from selenium import webdriver
from time import sleep
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains

#Cenário 7: Verificar atualização de dados

#Abrindo a página
driver = webdriver.Firefox ()
driver.maximize_window() 
driver.get('http://www.aprendendotestar.com.br/treinar-automacao.php')

driver.save_screenshot('/home/suelen/Documentos/Aprendendo a testar/evidencias_aprendendotestar/cenário7/1_Tela inicial.png')

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

sleep (3)

driver.save_screenshot('/home/suelen/Documentos/Aprendendo a testar/evidencias_aprendendotestar/cenário7/2_Inclusão dos registros.png')


try:
    usuario = driver.find_element_by_xpath('//*[contains(text(),"SXP")]')
    tr = usuario.find_element_by_xpath('..')
    senha = tr.find_element_by_xpath('//*[contains(text(),"abc@12")]')
    nome = tr.find_element_by_xpath('//*[contains(text(),"Suelen Passos")]')

    print('Dados atuais ' + senha.text + ' ' + nome.text) 
except:
    print('Teste não passou')


#atualização de registro 1
#preencher o campo usuário
usuario = driver.find_element_by_xpath('/html/body/section/section[2]/div/form/table/tbody/tr[2]/td/input')
usuario.send_keys('SXP')
#preencher o campo senha
usuario = driver.find_element_by_xpath('/html/body/section/section[2]/div/form/table/tbody/tr[4]/td/input')
usuario.send_keys('novasenha')
#preencher o campo nome
usuario = driver.find_element_by_xpath('/html/body/section/section[2]/div/form/table/tbody/tr[6]/td/input')
usuario.send_keys('Novo Nome')
#clicar no botao enviar 
clicar = driver.find_element_by_xpath('/html/body/section/section[2]/div/form/table/tbody/tr[7]/td/input') 
actions = ActionChains(driver)
actions.click(clicar).perform()

sleep (5)

try:
    usuario = driver.find_element_by_xpath('//*[contains(text(),"SXP")]')
    tr = usuario.find_element_by_xpath('..')
    senha = tr.find_element_by_xpath('//*[contains(text(),"novasenha")]')
    nome = tr.find_element_by_xpath('//*[contains(text(),"Novo Nome")]')

    print('Dados atuais ' + senha.text + ' ' + nome.text) 
    print('Teste passou') 

except:
    print('Teste não passou')

driver.save_screenshot('/home/suelen/Documentos/Aprendendo a testar/evidencias_aprendendotestar/cenário7/3_Atualização do usuario SXP.png')


sleep(10)

driver.quit()
