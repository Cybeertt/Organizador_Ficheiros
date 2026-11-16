from pathlib import Path

pasta = Path.cwd()
print("ORGANIZADOR DE FICHEIROS")
print("-----------------------")
for ficheiro in pasta.iterdir():
    if ficheiro.is_file():
        print("Nome:", ficheiro.name)
        print("Extensão:", ficheiro.suffix)
        print("-----------------------")
        