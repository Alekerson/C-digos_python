def h():
    num =[]
    for cont in range(1, 4):
        num.append(int(input(f"Digite o {cont}° número: ")))
    num.sort()
    print(num)
    num.sort(reverse=True)
    print(num)


h()