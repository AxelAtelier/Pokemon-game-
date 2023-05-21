pokemon = input("Dame el nombre de un pokemon ") 
election = int(input("Selecciona un numero del 1 al 4 "))
style = None

dict = {
    1 : "Fuego", 
    2 : "Agua", 
    3 : "Veneno", 
    4 : "Tierra", 
    5 : "Hielo"
}


if election == 1:
    style = str("fuego")
elif election == 2:
    style = str("tierra")
elif election == 3:
    style = str("veneno")
else:
    style = str("agua")


print(f"Tu pokemon se llama {pokemon} y su tipo es {style}")