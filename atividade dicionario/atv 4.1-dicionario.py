playlist  =[]
musica = {}

for contador in range(2):
    nome = input("Qual o nome da música? ")
    artista = input("Qual o nome do artista? ")
    tempo = float(input("Qual a duração da música? "))

    musica[nome] = {"Artista": artista, "Duracao":tempo}

    playlist.append(musica.copy())
    musica.clear

for linha in playlist:
    for chave, valor in linha.items():
        print(f"{chave} = {valor[artista]} = {valor[tempo]}")