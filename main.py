from time import sleep
import os
import json
import requests

# importações para web
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.firefox.service import Service


os.system('cls') or None

print('INICIANDO NAVEGADOR...')
s = Service('geckodriver.exe')
navegador= webdriver.Firefox(service=s)
navegador.get("https://blaze.com/pt/games/double")

wait = WebDriverWait(navegador, 10)

user= "laizaalmeida1221@gmail.com"
password= "Ciciebeto8812"

sleep(3)
text = navegador.find_element(By.XPATH, '/html/body/div[1]/main/div[1]/div[2]/div/div[2]/div/div[2]/div/div/div[1]')
text.click()
sleep(2)
elemento = navegador.find_element(By.XPATH,'/html/body/div[1]/main/div[3]/div/div[2]/div/form/div[1]/div/input') 
elemento.send_keys(user)
elemento = navegador.find_element(By.XPATH,'/html/body/div[1]/main/div[3]/div/div[2]/div/form/div[2]/div/input') 
elemento.send_keys(password)
sleep(2)
elemento = navegador.find_element(By.XPATH,'/html/body/div[1]/main/div[3]/div/div[2]/div/form/div[4]/button') 
elemento.click()

sleep(25)

# saldo
WebDriverWait(navegador, 15).until(
                EC.element_to_be_clickable((By.XPATH ,'//*[@id="header"]/div[2]/div/div[2]/div/div[3]/div/a/div/div/div[1]'))
                )
saldo_inicial = navegador.find_element(By.XPATH, '//*[@id="header"]/div[2]/div/div[2]/div/div[3]/div/a/div/div/div[1]').text

print(f'SALDO INICIAL ---- {float(saldo_inicial.split("$")[1])}')

##############################################################################
#APOSTAS 
def aposta_vermelho(valor):
    print("APOSTANDO VERMELHO")
    sleep(2)
    WebDriverWait(navegador, 5).until(
                EC.element_to_be_clickable((By.XPATH ,'/html/body/div[1]/main/div[1]/div[4]/div/div[1]/div/div/div[1]/div[1]/div[1]/div[2]/div[1]/div/div[1]/input'))
                )
    input =  navegador.find_element(By.XPATH, '/html/body/div[1]/main/div[1]/div[4]/div/div[1]/div/div/div[1]/div[1]/div[1]/div[2]/div[1]/div/div[1]/input')
    input.send_keys(str(valor))
    sleep(1)

    elemento = navegador.find_element(By.CSS_SELECTOR, '.input-wrapper > div:nth-child(1)') 
    navegador.execute_script("arguments[0].click();", elemento)
    
#--
    while True:
        try:
            resultado = navegador.find_element(By.XPATH, '//*[@id="roulette-timer"]/div[1]').text
            sleep(1)
            split_r = resultado.split(' ')
            # print(f'{split_r}')
            if split_r[0]=='Blaze':
                print(resultado)
                break
        
            if split_r[1]=='Em':
                print(resultado)
                break
        except:
            pass

    WebDriverWait(navegador, 10).until(
                EC.element_to_be_clickable((By.XPATH ,'/html/body/div[1]/main/div[1]/div[4]/div/div[1]/div/div/div[1]/div[1]/div[1]/div[3]/button'))
                )
    aposta= navegador.find_element(By.XPATH, '/html/body/div[1]/main/div[1]/div[4]/div/div[1]/div/div/div[1]/div[1]/div[1]/div[3]/button')   
    aposta.click()
    print("FEITO")

def aposta_preto(valor):
    print("APOSTANDO PRETO")
    sleep(2)
    WebDriverWait(navegador, 10).until(
                EC.element_to_be_clickable((By.XPATH ,'/html/body/div[1]/main/div[1]/div[4]/div/div[1]/div/div/div[1]/div[1]/div[1]/div[2]/div[1]/div/div[1]/input'))
                )
    input =  navegador.find_element(By.XPATH, '/html/body/div[1]/main/div[1]/div[4]/div/div[1]/div/div/div[1]/div[1]/div[1]/div[2]/div[1]/div/div[1]/input')
    input.send_keys(str(valor))
    sleep(1)
    elemento = navegador.find_element(By.CSS_SELECTOR, 'div.black:nth-child(3)') 
    elemento.click()

#--
    while True:
        try:
            resultado = navegador.find_element(By.XPATH, '//*[@id="roulette-timer"]/div[1]').text
            sleep(1)
            split_r = resultado.split(' ')
            # print(f'{split_r}')
            if split_r[0]=='Blaze':
                print(resultado)
                break
            if split_r[1]=='Em':
                print(resultado)
                break
        except:
            pass

    WebDriverWait(navegador, 5).until(
                EC.element_to_be_clickable((By.XPATH ,'/html/body/div[1]/main/div[1]/div[4]/div/div[1]/div/div/div[1]/div[1]/div[1]/div[3]/button'))
                )
    aposta= navegador.find_element(By.XPATH, '/html/body/div[1]/main/div[1]/div[4]/div/div[1]/div/div/div[1]/div[1]/div[1]/div[3]/button')
    aposta.click()
    print("FEITO")

def aposta_branco(valor):
    
    print("APOSTANDO BRANCO")    
    input =  navegador.find_element(By.XPATH, '/html/body/div[1]/main/div[1]/div[4]/div/div[1]/div/div/div[1]/div[1]/div[1]/div[2]/div[1]/div/div[1]/input')
    input.clear()
    input.send_keys(str(valor))
    sleep(2)

    elemento = navegador.find_element(By.CSS_SELECTOR, 'div.white:nth-child(2) > div:nth-child(1)') 

    navegador.execute_script("arguments[0].click();", elemento)
    
    WebDriverWait(navegador, 5).until(
                EC.element_to_be_clickable((By.XPATH ,'/html/body/div[1]/main/div[1]/div[4]/div/div[1]/div/div/div[1]/div[1]/div[1]/div[3]/button'))
                )
    aposta= navegador.find_element(By.XPATH, '/html/body/div[1]/main/div[1]/div[4]/div/div[1]/div/div/div[1]/div[1]/div[1]/div[3]/button')
    aposta.click()
    print("BOTAO CLICADO")


def resultados():
    # Defina a URL da API e os parâmetros de consulta (se houver)
    url = "https://blaze.com/api/roulette_games/history"
    params = {"param1": "value1", "param2": "value2"}

    # Faça uma solicitação GET à API e obtenha a resposta
    response = requests.get(url)
    # response = requests.get(url, params=params)

    # Verifique se a resposta foi bem-sucedida
    if response.status_code == 200:
        # Exiba o conteúdo da resposta
        data = response.json()
        print(data)
    else:
        # Exiba o código de status da resposta e a mensagem de erro (se houver)
        print("Erro ao consumir API:", response.status_code, response.reason)


def main():
    with open("cfg.json") as estrategias:
        dados = json.load(estrategias)
    print(dados)    

    while True:
        
 
        pass

main()    
navegador.quit()



