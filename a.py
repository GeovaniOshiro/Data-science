import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import tkinter as tk
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg


def plot_data():
    data = pd.read_csv('b.csv')
    
    anos = data['ano']
    vendas = data['vendas']

    fig, grafico = plt.subplots()
    grafico.plot(anos, vendas, marker='o', linestyle='-', color='b')

    grafico.set_xlabel('Ano')
    grafico.set_ylabel('Vendas')
    grafico.set_title('Vendas Anuais')

    canvas = FigureCanvasTkAgg(fig, master=janela)
    canvas.draw()
    canvas.get_tk_widget().pack(side=tk.RIGHT, fill=tk.BOTH, expand=True)

janela = tk.Tk()
janela.title('Gráfico de Vendas')

botao = tk.Button(janela, text='Exibir Gráfico', command=plot_data)
botao.pack(pady=20)

janela.mainloop()






