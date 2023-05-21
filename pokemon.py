pokemon = input("Dame el nombre de un pokemon ") 
election = int(input("Selecciona un numero del 1 al 3 "))
style = None


if election == 1:
    style = str("fuego")
elif election == 2:
    style = str("tierra")
else:
    style = str("agua")


print(f"Tu pokemon se llama {pokemon} y su tipo es {style}")