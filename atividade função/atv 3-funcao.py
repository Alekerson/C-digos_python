vet = []

def somaPar():
    calc = 0
    for contador in range(1,11):
        vet.append(contador)
        if contador % 2 == 0:
            calc += 1
    return calc
    
print(f"{somaPar()}")