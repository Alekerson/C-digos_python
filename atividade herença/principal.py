from personagem import Personagem, Jogador

raca = input("Escolha um tipo de raça: ")

a = Personagem("Alex")
b = Jogador("Alekerson", raca)

a.atacar()

b.usarHabilidade("Invocação de chamas infernais")