import os
import shutil
import psutil 
from tkinter import *
import tkinter as tk

root = Tk()

#Limpando os dados temporários
def limpar_pasta_temp():
    temp_dir = os.getenv('TEMP')
    if os.path.exists(temp_dir):
        shutil.rmtree(temp_dir, ignore_errors=True)
    
        label_stt.config(text="Pasta temp limpa com sucesso!")
    else:
        label_stt.config(text="Pasta temp não encontrada!")
    pass


#Reiniciando drivers gráficos
def reiniciar_drivers_graficos():  
    for proc in psutil.process_iter(['pid', 'name']):
        if proc.info['name'] == 'dwm.exe':
            os.system("powershell -Command \"Start-Process -FilePath powershell -ArgumentList 'Stop-Process -Name dwm -Force' -Verb RunAs\"")
            os.system("timeout /t 1")
            os.system("powershell -Command \"Start-Process -FilePath C:\\Windows\\System32\\dwm.exe\"")
            
            label_stt.config(text="Drivers reiniciados com sucesso!")

            break
    pass

# Configurações da janela principal
root.title("Optimiza Python GUI")
root.geometry("400x300")
root.configure(bg="#17389c")

label = Label(root, text="Optimza Python GUI")

#botão para limpar pasta TEMP
label.temp = Button(root, text="Limpar pasta TEMP", font=("Verdana", 10, "italic", "bold"),command=limpar_pasta_temp, width=35, height=2)
label.temp.configure(bg="#2949ab", fg="white")
label.temp["text"]= "Limpar pasta TEMP"
label.temp.pack(pady=10)  

#Botão para reiniciar drivers gráficos
label.drivers = Button(root, text="Reiniciando Drivers", font=("Verdana", 10, "italic", "bold"),command=reiniciar_drivers_graficos, width=35, height=2)
label.drivers.configure(bg="#2949ab", fg="white")
label.drivers["text"]= "Reiniciando Drivers Gráficos"
label.drivers.pack(pady=10)  

#Texto de status/retorno
label_stt = Label(root, text="", font=("Verdana", 10, "italic", "bold"))
label_stt.configure(bg="#17389c")
label_stt.pack(pady=30)

#Botão Sair
label.sair = Button(root, text="Exit", font=("Verdana", 10, "italic", "bold"), command=root.quit)
label.sair.configure(bg="#2949ab", fg="white")
label.sair["text"]= "Sair"
label.sair.pack(side=BOTTOM, pady=10)  

root.mainloop()




