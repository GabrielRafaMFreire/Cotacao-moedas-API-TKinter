import requests
import json
from tkinter import *

def pegar_cotacoes():
    cotacoes = requests.get("https://economia.awesomeapi.com.br/last/USD-BRL,EUR-BRL,BTC-BRL")
    cotacoes = cotacoes.json()
    cotacao_dolar = cotacoes['USDBRL']['bid']
    cotacao_euro = cotacoes['EURBRL']['bid']
    cotacao_bitcoin = cotacoes['BTCBRL']['bid']

    texto = f''' 
    Dolar = {cotacao_dolar}
    Euro = {cotacao_euro}
    Bitcoin = {cotacao_bitcoin}'''


    texto_cotacoes["text"] = texto
    

#parte gráfica 

window = Tk()
window.title("Cotações")
window.geometry("330x200")

#texto
text_orientation = Label(window, text = "Aperte o botão abaixo para ver a cotação do Dolar, Euro e Bitcoin", wraplength=310)
text_orientation.grid(column=0, row = 0, padx= 10, pady=10)

#botao
bt = Button(window, text = "Clique aqui", command = pegar_cotacoes)
bt.grid(column=0, row=1, padx= 10, pady=10)


#print texto

texto_cotacoes = Label(window, text="")
texto_cotacoes.grid(column=0, row=2, padx= 10, pady=10)


window.mainloop()

#Rafáaa