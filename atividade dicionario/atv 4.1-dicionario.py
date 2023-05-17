playlist  =[]
musica = {}

for contador in range(1):
    nome = input("Qual o nome da música? ")
    artista = input("Qual o nome do artista? ")
    tempo = float(input("Qual a duração da música? "))

    musica[nome] = {"artista": artista, "duracao": tempo}

    playlist.append(musica.copy())
    musica.clear

for linha in playlist:
    for chave, valor in linha.items():
        print(f"{valor} = {valor['artista']} = {valor['duracao']}")