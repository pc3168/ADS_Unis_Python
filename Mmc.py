from tkinter import *

from setuptools.command.saveopts import saveopts


def calcular():
    print("Nome: %s"% np.get())
    print("Endereço: %s" % end.get())
    print("Altura: %s" % alt.get())
    print("peso: %s" % pe.get())
    print("IMC: %s" % (float(pe.get()) / (float(alt.get())** 2)))

def reiniciar():
    np.delete(0,END)
    end.delete(0, END)
    alt.delete(0, END)
    pe.delete(0, END)


def sair():
    app.destroy()

app=Tk()
app.title("MMC")
app.geometry("400x250")
app.configure(background="#dde")

Label(app, text="Nome:", anchor=W).place(x=10,y=10,width=100,height=20)
Label(app, text="Endereço:", anchor=W).place(x=10,y=35,width=100,height=20)
Label(app, text="Altura:", anchor=W).place(x=10,y=60,width=100,height=20)
Label(app, text="Peso:", anchor=W).place(x=10,y=85,width=100,height=20)

np=Entry(app)
end=Entry(app)
alt=Entry(app)
pe=Entry(app)

np.place (x=110,y=10,width=250,height=20)
end.place(x=110,y=35,width=250,height=20)
alt.place(x=110,y=60,width=100,height=20)
pe.place (x=110,y=85,width=100,height=20)

resultado=Text(app)
resultado.place (x=220,y=60,width=140,height=100)

Button(app, text="Calcular", command=calcular).place (x=10,y=180,width=100,height=30)
Button(app, text="Reiniciar", command=reiniciar).place (x=110,y=180,width=100,height=30)
Button(app, text="Sair", command=sair).place (x=260,y=180,width=100,height=30)

app.mainloop()