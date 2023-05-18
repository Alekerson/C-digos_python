esporte = input("Qual esporte você prática? ").lower()

def funcao(esporte):

    if esporte == "natação":
        ginasio = "Ginásio 1"
    elif esporte == "vôlei":
        ginasio = "Ginásio 1"
    elif esporte == "dança":
        ginasio = "Ginásio 2"
    elif esporte == "futebol":
        ginasio = "Ginásio 2"
    elif esporte == "corrida":
        ginasio = "Ginásio 3"
    elif esporte == "ballet":
        ginasio = "Ginásio 3"
    return ginasio

print(f"{funcao(esporte)}")