

def menu():
    print("menu")
    print("1-Mantenedor Usuarios")
    print("2-Reporte")
    print("3-Salida")

int(input("seleccione una opcion: "))
def opcion_Mantenedor():
    print("Has elegido la opcion Mantenedor de usuarios")


def opcion_reporte():
    print("Has elegido la opcion de Reporte")

def opcion_salir():
    print("Has elegido la opcion de Salir")

def main():
    while true:
        menu()
        opcion= int(input("seleccione una opcion (1,2,3): "))
        if opcion == "1":
            opcion_Mantenedor()
        elif opcion == "2":
            opcion_reporte()   
        elif opcion == "3":
            salir()
            break
        else:
            print("seleccione una opcion valida")     


