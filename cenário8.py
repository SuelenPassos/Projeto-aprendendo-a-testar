#-- coding: utf-8 --
from selenium import webdriver
from time import sleep
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains

#Cenário 8: Verificar atualização da pagina

#Abrindo a página
driver = webdriver.Firefox ()
driver.maximize_window()

driver.get('http://www.aprendendotestar.com.br/treinar-automacao.php')

driver.save_screenshot('/home/suelen/Documentos/Aprendendo a testar/evidencias_aprendendotestar/cenário8/1_Antes da atualização.png')


pagina = driver.page_source

#clicar no botao clique aqui para atualizar 
clicar = driver.find_element_by_xpath('/html/body/section/section[2]/div/p[3]/a') 
clicar.click()


paginaatualizada = driver.page_source 

if pagina == paginaatualizada:
    #Atualizada sem alteração
    print ("Teste passou")
else:
    #Atualizada com alteração
    print ("Teste não passou")
sleep(5)
driver.save_screenshot('/home/suelen/Documentos/Aprendendo a testar/evidencias_aprendendotestar/cenário8/2_Após atualização.png')
sleep(5)

# driver.quit()


