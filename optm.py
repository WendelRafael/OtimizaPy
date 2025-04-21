import os
import shutil

# Defina o caminho da pasta Temp
temp_dir = os.getenv('TEMP')

# Verifique se a pasta Temp existe
if os.path.exists(temp_dir):
    # Apague todo o conteúdo da pasta Temp
    shutil.rmtree(temp_dir, ignore_errors=True)

    print("Pasta Temp limpa com sucesso!")
else:
    print("Pasta Temp não encontrada.")