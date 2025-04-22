import os
import shutil
import psutil

print("Iniciando a Otimização")

#Limpando os dados temporários
temp_dir = os.getenv('TEMP')
if os.path.exists(temp_dir):
    shutil.rmtree(temp_dir, ignore_errors=True)
    print("Pasta Temp limpa com sucesso!")
else:
    print("Pasta Temp não encontrada.")

#Reiniciando drivers gráficos
def reiniciar_drivers_graficos():
    for proc in psutil.process_iter(['pid', 'name']):
        if proc.info['name'] == 'dwm.exe':
            os.system("powershell -Command \"Start-Process -FilePath powershell -ArgumentList 'Stop-Process -Name dwm -Force' -Verb RunAs\"")
            os.system("timeout /t 1")
            os.system("powershell -Command \"Start-Process -FilePath C:\\Windows\\System32\\dwm.exe\"")
            break
reiniciar_drivers_graficos()
print("Drivers reiniciados")

print("Otimização concluida!")