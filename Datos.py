print(" \n Clase v2 Renata Ronquillo Lopez ♥1307♥ \n")
# zona de clase
class datos:
    # El constructor funcion multiplos
    def __init__(self, estatura,peso):
        self.estatura=estatura
        self.peso=peso
    def mostrar_datos1307(self):
            print(f" Estatura: {self.estatura} mts. Peso {self.peso}kg. \n")
    
    def lista1307(self):
        Favsong=["New Woman"," Bombayah","Dame \n"]
        print(Favsong)
    
        for canciones in Favsong:
            print(canciones)

        
    # Tuplas
    def tupla1307(self):
        FavMakeup=(" Doyuin "," Natural "," Coquette ")
        print(FavMakeup)
        for Makeu in FavMakeup:
            print(Makeu)


    # Conjuntos
    def conjunto1307(self):
        Misktraumas=(" 25 - 21 "," Escalera al cielo "," Hola y Adios mamá ")
        print(Misktraumas)
        
        for Mks in Misktraumas:
            print(Mks)
    #diccionario
    def Diccionario1307(self):
        Labiales= {
    " 1:": "Gloss Italia Deluxe", 
    " 2:": "Labial Cafe de Jafra",
    " 3:": "Labial de My Melody \n "
    }
        print(Labiales)
        for R, L in Labiales.items():
            print(R,L)
            
# Creacion de objeto info.datos
info=datos(1.70, 54 )

# Utilizando el objeto 
print(" Altura y Peso ")
info.mostrar_datos1307()
print(" Lista de mis 3 canciones favoritas: ")
info.lista1307()
print(" Tuplas de mis maquillajes favoritos: ")
info.tupla1307()
print(" \n Conjunto de mis Ktraumas (Series coreanas que me traumaron) ")
info.conjunto1307()
print(" \n Diccionario, Labiales Fav: ")
info.Diccionario1307()