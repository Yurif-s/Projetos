# Script do Projeto
import yfinance as yf
import pyautogui as gui
import pyperclip as clip
import webbrowser
from time import sleep

codigo = input('Digite o código: ')
dados = yf.Ticker(codigo).history(start='2023-01-01', end='2023-12-31')
fechamento = dados.Close

maxima = round(fechamento.max(), 2)
minima = round(fechamento.min(), 2)
valor_medio = round(fechamento.mean(), 2)

destinatario = 'yurifs9118@gmail.com'
assunto = 'Análises do Projeto 2023'
mensagem = f'''
Prezado gestor,

Seguem as análises solicitadas da ação {codigo}:

Cotação máxima: R${maxima}
Cotação mínima: R${minima}
Valor médio: R${valor_medio}

Qualquer dúvida, estou a disposição!

Atte.
'''

gui.PAUSE = 3

webbrowser.open('www.gmail.com')
sleep(4)

gui.click(x=79, y=178)
clip.copy(destinatario)
gui.hotkey('ctrl', 'v')
gui.hotkey('tab')
clip.copy(assunto)
gui.hotkey('ctrl', 'v')
gui.hotkey('tab')
clip.copy(mensagem)
gui.hotkey('ctrl', 'v')
gui.click(x=849, y=697)