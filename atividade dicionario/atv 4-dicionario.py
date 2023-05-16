from os import system
playlist = []
musica = {}

system("cls")
for contador in range(0, 2):
    nome = (input("Informe o nome da música: "))
    musica[nome] = input(f"Informe o nome do artista da musica {nome}: ")

    playlist.append(musica.copy())
    musica.clear()

for linha in playlist:
    for linha, coluna in linha.items():
        print(f"{linha} = {coluna}") 