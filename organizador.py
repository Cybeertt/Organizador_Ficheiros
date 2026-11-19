from pathlib import Path

pasta = Path.cwd()
print("ORGANIZADOR DE FICHEIROS")
print("---")

ficheiros = [ficheiro for ficheiro in pasta.iterdir() if ficheiro.is_file()]

total_ficheiros = len(ficheiros)

if total_ficheiros == 0:
    print("A pasta atual não contém ficheiros.")
else:
    print(f"A pasta atual contém {total_ficheiros} ficheiro(s):")
    print("---")
    for ficheiro in ficheiros:
        print("Nome:", ficheiro.name)
        print("Extensão:", ficheiro.suffix)
        if ficheiro.suffix in [".py", ".txt", ".csv"]:
            print("Tipo: Ficheiro relevante")
        else:
            print("Tipo: outro")
        ficheuro_tamanho = ficheiro.stat().st_size
        print("Tamanho:", ficheuro_tamanho, "bytes")
        print("---")
        