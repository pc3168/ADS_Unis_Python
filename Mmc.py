from tkinter import *

from setuptools.command.saveopts import saveopts
def calcula(imc):
    if  imc < 17:
        valor = "Muito abaixo do peso"
    elif imc < 18.49:
        valor = "Abaixo do peso"
    elif imc < 24.99:
        valor = "Peso normal"
    elif imc < 29.99:
        valor = "Acima do peso"
    elif imc < 34.99:
        valor = "Obesidade I"
    elif imc < 39.99:
        valor = "Obesidade II (severa)"
    else:
        valor = "Obesidade III (mórbida)"
    return valor

def calcular():
    resultado.insert(INSERT, "Nome: %s"% np.get())
    resultado.insert(INSERT, "\nEndereço: %s" % end.get())
    resultado.insert(INSERT, "\nAltura: %s" % alt.get())
    resultado.insert(INSERT, " e Peso: %s" % pe.get())
    resultado.insert(END, "\nIMC: %s" % calcula((float(pe.get()) / (float(alt.get())** 2))))

def reiniciar():
    np.delete(0,END)
    end.delete(0, END)
    alt.delete(0, END)
    pe.delete(0, END)


def sair():
    app.destroy()

app=Tk()
app.title("Tabela de IMC")
app.geometry("500x250")
app.configure(background="#dde")

Label(app, text="Nome:", anchor=W).place(x=10,y=10,width=100,height=20)
Label(app, text="Endereço:", anchor=W).place(x=10,y=35,width=100,height=20)
Label(app, text="Altura:", anchor=W).place(x=10,y=60,width=100,height=20)
Label(app, text="Peso:", anchor=W).place(x=10,y=85,width=100,height=20)

np=Entry(app)
end=Entry(app)
alt=Entry(app)
pe=Entry(app)

np.place (x=110,y=10,width=300,height=20)
end.place(x=110,y=35,width=300,height=20)
alt.place(x=110,y=60,width=100,height=20)
pe.place (x=110,y=85,width=100,height=20)

resultado=Text(app)
resultado.place (x=220,y=60,width=190,height=100)

Button(app, text="Calcular", command=calcular).place (x=10,y=180,width=100,height=30)
Button(app, text="Reiniciar", command=reiniciar).place (x=110,y=180,width=100,height=30)
Button(app, text="Sair", command=sair).place (x=310,y=180,width=100,height=30)

app.mainloop()