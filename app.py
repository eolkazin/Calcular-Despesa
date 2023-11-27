import tkinter as tk

#Lista de Opções:
OptionList = [
"Mensal",
"Trimestral",
"Semastral",
"Anual"
]

#Configuração da Janela:
janela = tk.Tk()
janela.geometry('500x300')
janela.title("Calcular Despesa")
janela.resizable(False,False)

#Entrada de Despesas:
despesatext = tk.Label(text="Despesas:",font=('Helvetica', 12))
despesatext.place(relx=0.15,rely=0.05)
despesa = tk.DoubleVar()
despesa_Entry = tk.Entry(textvariable=despesa,justify='center',font=('Helvetica', 12))
despesa_Entry.place(relx=0.45,rely=0.05)

#Menu de Opções:
variable = tk.StringVar(janela)
variable.set(OptionList[0])
opt = tk.OptionMenu(janela, variable, *OptionList)
opt.config(width=45, font=('Helvetica', 12),fg="blue",bg='yellow')
opt.place(relx=0.05,rely=0.25)

#Rótulo para Resultados:
labelTest = tk.Label(text="", font=('Helvetica', 12), fg='red')
labelTest.place(relx=0.35,rely=0.55)

#Função de Callback:
def callback(*args):
    a = variable.get()
    r = despesa.get()
    if a == "Anual":
        f = r
    elif a == "Semastral":
        f = r*2
    elif a == "Trimestral":
        f = r * 4
    else:
        f = r*12
    labelTest.configure(text="A sua despesa anual é de {}.".format(f))
variable.trace("w", callback)
janela.mainloop()