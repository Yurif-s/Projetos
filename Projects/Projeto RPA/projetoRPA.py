# Script do Projeto

# Bibliptecas do Projeto
import yfinance as yf
import pyautogui as gui
import pyperclip as clip
import webbrowser
from time import sleep

# Saber qual ação retiraremos os dados
codigo = input('Digite o código: ')
data = input('Digite a data final: [Ano-Mês-Dia] ')
# Pegar os dados dessa ação
dados = yf.Ticker(codigo).history(start='2024-01-01', end=f'{data}')
# Pegar apenas o fechamento desses dados
fechamento = dados.Close

# Criar as ações solicitadas
maxima = round(fechamento.max(), 2)
minima = round(fechamento.min(), 2)
valor_medio = round(fechamento.mean(), 2)

# Definindo os textos que irão ser utilizados para o envio do e-mail
destinatario = 'yurifs9118@gmail.com'
assunto = 'Análises do Projeto 2023'
mensagem = f'''
Prezado Eu,

Seguem as análises solicitadas da ação {codigo}:

Cotação máxima: R${maxima}
Cotação mínima: R${minima}
Valor médio: R${valor_medio}

Qualquer dúvida, estou a disposição!

Atte.
'''

# Definindo o intervalo de execução dos código do PyAutoGUI
gui.PAUSE = 4

# Abrir o Chrome no Gmail.com
webbrowser.open('www.gmail.com')
sleep(4)
# Clicar no botão Escrever
gui.click(x=79, y=178)
# Copiar e colar o texto do destinatário
clip.copy(destinatario)
gui.hotkey('ctrl', 'v')
# Ir para o próximo campo
gui.hotkey('tab')
# Copiar e colar o texto do assunto
clip.copy(assunto)
gui.hotkey('ctrl', 'v')
# Ir para o próximo campo
gui.hotkey('tab')
# Copiar e colar o texto da mensagem
clip.copy(mensagem)
gui.hotkey('ctrl', 'v')
# Clicar no botão Enviar
gui.click(x=849, y=697)

# Fechar a aba do Chrome
gui.hotkey('ctrl', 'w')


gui.hotkey('alt', 'tab')
print('Programa finalizado')