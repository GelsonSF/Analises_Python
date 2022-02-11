import pandas as pd
import pyautogui
import pyperclip
import time

pyautogui.PAUSE = 1

pyautogui.hotkey('ctrl', 't')
pyperclip.copy('https://drive.google.com/drive/folders/149xknr9JvrlEnhNWO49zPcw0PW5icxga?usp=sharing')
pyautogui.hotkey('ctrl', 'v')
pyautogui.press('enter')

time.sleep(5)

pyautogui.click(x=1140, y=274, clicks=2)
time.sleep(2)

pyautogui.click(x=1076, y=274)

time.sleep(10)

tabela = pd.read_excel(r'D:\! - Downloads\Downloads GoogleChrome\!Intensivão Python\Dia 1\Vendas - Dez.xlsx')
display(tabela)

faturamento = tabela['Valor Final'].sum()
qtde_produtos = tabela['Quantidade'].sum()

link = 'https://mail.google.com/mail/u/0/'
texto = (f"""Bom dia, tudo bem? 

O faturamento foi de {faturamento:,.2f}
A quantidade vendida foi de {qtde_produtos:,.2f}

Desde já agradeço a atenção!""")


pyautogui.press('win')
pyautogui.write('chrome')
pyautogui.press('enter')

pyperclip.copy(link)
pyautogui.hotkey('ctrl', 'v')
pyautogui.press('enter')

time.sleep(5)

pyautogui.click(x=87, y=192)

pyautogui.write('aaaaaazz.154@gmail.com')
pyautogui.press('tab')
pyautogui.press('tab')

pyautogui.write('E-mail de faturamento')
pyautogui.press('tab')

pyperclip.copy(texto)
pyautogui.hotkey('ctrl', 'v')
pyautogui.hotkey('ctrl', 'enter')

time.sleep(5)
