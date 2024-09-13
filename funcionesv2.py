print("funciones version 2")
print("alexis jimenez")
#zona de funciones conjuntos tuplas y deccionarios
celulares=["samsung a52","Iphone 11","chafa"]
tipos={"chihuahua","labrador","pomerania","cruzado","husky"}
Tprocesador=("Ryzen 9","Ryzen 7","Intel i5","intel i3")
Micoche={
    "marca ":"ford",
    "dia comprado ":"2036",
    "seguro ":"si"
}
#zona de funciones
def verlista(telefono):
    for uncelular in telefono:
        print(uncelular)

def perros(raza):
    for x in raza:
        print(x)

def procesadores(marca):
    for y in marca:
        print(y)
    
def carrito(Dcarro):
    for z in Dcarro:
        print(z,Micoche[z])    
        
#llamadas a funciones
print("-imprime celulares")
verlista(celulares)     
print("-imprime perros")
perros(tipos)
print("-imprime procesadores")
procesadores(Tprocesador)
print("-imprime datos de mi carro")
carrito(Micoche)