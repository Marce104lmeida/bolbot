from selenium import webdriver, common
import time
from selenium.webdriver.common.by import By

from selenium.webdriver.common.keys import Keys
# Autor: Marcelo Oliveira Almeida
# Email: marcelo.almeida1989@bol.com.br
# este bot funcionou com o email da bol
# futuramente será adicionado para funcionar com mais provedores
driver = webdriver.Chrome('C:\\Users\MARCELO\\anaconda3\\chromedriver.exe')
driver.get('https://conta.uol.com.br/login?t=bol&env=visitante&dest=https://bmail.uol.com.br/login/check_session')
driver.maximize_window()
# email onde esta os email a serem encaminhados!
EMAIL_ADRESS =''
#senha do email!
EMAIL_PASSWORD = ''
# email para onde será encaminhado os emails
enc_para = ''

time.sleep(2)
user_field = driver.find_element(By.ID, 'user')
time.sleep(1)
user_senha = driver.find_element(By.ID, 'pass')
btn_entrar = driver.find_element(By.ID, 'button-submit')
user_senha.send_keys(EMAIL_PASSWORD)
user_field.send_keys(EMAIL_ADRESS)
time.sleep(1)
btn_entrar.click()
time.sleep(20)

# Criada a função encaminhar
def encaminhar():
    total_envio = 0
    try:
        selected_email = driver.find_element(By.XPATH,
                                             '/html/body/div[3]/div/section[2]/div/div[2]/div/div[2]/section[1]/div/div[5]/ul/li[1]/a/div/div[3]/span')
        time.sleep(2)
        selected_email.click()
    except common.exceptions.NoSuchElementException:
        print("Falha no Login ou / nenhum email nesta pasta")
    else:
        print('')
    time.sleep(5)
    for email in range(101):
        try:
            encaminhar = driver.find_element(By.XPATH,
                                             '/html/body/div[3]/div/section[2]/div/div[2]/div/div[2]/section[2]/div/div[1]/div[1]/menu[3]/span[2]')
            encaminhar.click()
            time.sleep(3)
            destino = driver.find_element(By.ID, 'fake_input__field-to')
            destino.send_keys(enc_para)
            time.sleep(5)
            btn_enviar = driver.find_element(By.XPATH,
                                             '/html/body/div[3]/div/div[1]/div[1]/form/div[4]/menu[1]/span[2]')
            btn_enviar.click()
            time.sleep(2)
            btn_apagar = driver.find_element(By.XPATH,
                                             '/html/body/div[3]/div/section[2]/div/div[2]/div/div[1]/div[1]/span/ul/li[2]/span/span')
            btn_apagar.click()
            time.sleep(3)
            total_envio += 1
        except common.exceptions.NoSuchElementException:
            back_entrada = driver.find_element(By.XPATH,
                                               "//*[@id='fc-collapsable-sidebar']/div[3]/div[2]/div/div[1]/ul/li[1]")
            back_entrada.click()
            break
        else:
            print('')

        print(f'Foram enviados um total de: {total_envio} email(s)')


def lixeira():
    lixeira = driver.find_element(By.XPATH, "//*[@id='fc-collapsable-sidebar']/div[3]/div[2]/div/div[1]/ul/li[4]")
    lixeira.click()
    time.sleep(3)
    for i in range(1000):
        try:
            chkbox = driver.find_element(By.XPATH, "/html/body/div[3]/div/section[2]/div/div[2]/div/div[2]/section[1]/div/div[1]/label")
            time.sleep(3)
            chkbox.click()
            time.sleep(1)
            btn_apagar = driver.find_element(By.XPATH, "/html/body/div[3]/div/section[2]/div/div[2]/div/div[1]/div[1]/span/ul/li[2]/span")
            time.sleep(1)
            btn_apagar.click()
            time.sleep(1)
            confirma = driver.find_element(By.XPATH, "/html/body/div[3]/div/div[2]/div/div/span[1]")
            time.sleep(1)
            confirma.click()
            time.sleep(2)
        except:
         break
        else:
           print("")

encaminhar()
time.sleep(1)
lixeira()

