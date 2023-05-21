pokemon = input("Dame el nombre de un pokemon ") 
election = int(input("Selecciona un numero del 1 al 4 "))
style = None

dict = {
    1 : "Fuego", 
    2 : "Agua", 
    3 : "Veneno", 
    4 : "Tierra", 
    5 : "Hielo", 
    6 : "Electrico"
}

if election in dict:
    valor = dict[election]



print(f"Tu pokemon se llama {pokemon} y su tipo es {valor}")