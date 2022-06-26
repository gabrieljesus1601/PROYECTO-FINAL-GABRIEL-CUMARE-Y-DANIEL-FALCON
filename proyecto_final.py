import os
import archivo
import encriptar

def agregar_material():
    global inventario
    id_material = ""

    if os.path.exists('datatable.txt'):
        id_material = archivo.buscar_id()
    else:
        archivo.crear_archivo()
        id_material = 1

    print("----- Agregar Articulos al inventario-----\n")

    print("ID Material:", id_material)
    des_material = input("Ingrese la descripción del material: ")
    cantidad = input("ingrese la cantidad del material: ")
    verificacion = input("Se verificó el material antes de ser usado? escriba [si] o [no]: ")

    id_material = encriptar.encriptador(str(id_material))
    des_material = encriptar.encriptador(des_material.lower())
    cantidad = encriptar.encriptador(cantidad.lower())
    verificacion = encriptar.encriptador(verificacion.lower())
    
    # añade los valores a  la tabla
    inventario.append((id_material, des_material, cantidad, verificacion)) 
    archivo.agregar_inventario(inventario)

    inventario = []

def eliminar_material():

    print("----- Eliminar Articulos del inventario-----\n")
    id_material = int(input("Ingrese el ID del material: "))
    archivo.eliminar_inventario(id_material)

def actualizar_material():
    global inventario

    print("----- Actualizar Articulos del inventario-----\n")
    id_material = int(input("Ingrese el ID del material: "))
    archivo.actualizar_inventario(id_material)
    
def listar_inventario():
    archivo.reporte_inventario()

inventario = []
while True:
    print("----- Bienvenido al inventario secreto de asuntos de la CIA ------\n")
    print("1. ----- Agregar Inventario ------")
    print("2. ----- Eliminar Inventario ------")
    print("3. ----- Actualizar Inventario ------")
    print("4. ----- Listar Inventario ------")
    print("5. ----- Salir ------")

    opcion = int(input("\nSeleccione una opción: "))

    if opcion == 1:
        agregar_material()
    elif opcion == 2:
        eliminar_material()
    elif opcion == 3:
        actualizar_material()
    elif opcion == 4:
        listar_inventario()
    elif opcion == 5:
        print("Vuelva pronto....")
        exit(0)
    else:
        print("Ingrese una opción valida")
