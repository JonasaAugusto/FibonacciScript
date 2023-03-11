
import tkinter as tk
import math

root = tk.Tk()

fonte = ('Helvetica', 14)

entrada = tk.Text(root, height=3, width=34)
entrada.pack()
resposta = tk.Label(root, text="", font=('Helvetica',12))
resposta.pack()

# Função que verifica se um número é um quadrado perfeito
def Raiz(n):
    s = int(math.sqrt(n))
    return s*s == n

# Função que verifica se um número pertence à sequência de Fibonacci
def Fibonacci(n):
    return Raiz(5*n*n + 4) or Raiz(5*n*n - 4)

# Função que é chamada quando o botão "Verificar" é clicado
def verificar():
    num = int(entrada.get("1.0", "end-1c"))

    if Fibonacci(int(num)):
        resposta.config(text=f"{num} pertence à sequência de Fibonacci.")
    else:
        resposta.config(text=f"{num} não pertence à sequência de Fibonacci.")

# Cria um botão para verificar o número
botao = tk.Button(root, text="Resposta", command=verificar, padx=8, pady=7, bg="#f0f0f0")
botao.pack()

root.mainloop()