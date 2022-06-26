import encriptar #encriptador
import msvcrt

def tecla_esperar():
    print("\nPresione una tecla para continuar...")
    msvcrt.getch()

def establecer_archivo(ruta, permiso):
    archivo = open(ruta, permiso)

    return archivo

def leer_archivo(archivo):
    contenido = archivo.read()

    return contenido

def escribir_archivo(archivo, texto):
    archivo.write('\n' + texto)

# Buscando el Id del Material
def buscar_id():
    archivo = establecer_archivo('datatable.txt', 'r')
    
    indice = []
    for line in archivo:
        if (line[:1] != "-"):
            leer = line.strip()
            leer = leer.strip("\t")
            arreglo = leer.split(sep='|')
            
            for i in range(len(arreglo)):
                if i == 1 and arreglo[i].strip() != "ID": 
                    indice.append(int(encriptar.desencriptar(arreglo[i].strip())))
                    break
     
    archivo.close()

    id = max(indice) + 1
    return id

# funcion para crear un tabla y los valores queden centrados en el recuadro
def wordfill(word, size):
    if len(word) % 2 == 0:
        result = ' ' * int((size - len(word))/2) + word + ' ' * int((size - len(word))/2)
    else:
        result = ' ' * int((size - len(word))/2) + word + ' ' * int((size - len(word))/2) + ' '

    return result 

def agregar_inventario(inventario):
    archivo = establecer_archivo('datatable.txt', 'a')

	# añade los materiales que escribio el usuario que estan en la lista inventario
    for row in inventario:
        str_4 = wordfill(str(row[0]), 20)
        str_5 = wordfill(row[1], 20)
        str_6 = wordfill(row[2], 20)
        str_7 = wordfill(row[3], 20)

        archivo.write('\n|{}|\t{}|\t{}|\t{}|\t'.format(str_4, str_5, str_6, str_7))
        archivo.write('\n' + '-'*93 )
    
    archivo.close()

# escribe en el archivo txt la tabla los elementos de la lista encabezado
def crear_archivo():
    encabezado = [("ID","MATERIAL","CANTIDAD","VERIFICACION")]
    archivo = establecer_archivo('datatable.txt', 'w')
        
    for i in encabezado:
        str_0 = wordfill(i[0], 20)
        str_1 = wordfill(i[1], 20)
        str_2 = wordfill(i[2], 20)
        str_3 = wordfill(i[3], 20)
        
        archivo.write('-'*93) 
        archivo.write('|{}|\t{}|\t{}|\t{}|\t\n'.format(str_0, str_1, str_2, str_3))
        # añade lineas en la tabla para separar el encabezado de los elementos introducidos
        archivo.write('-'*93) 

    archivo.close()

def eliminar_inventario(id):
    archivo = establecer_archivo('datatable.txt', 'r')
    numero_linea = 0

    for line in archivo:
        cadena = line[:20]
        numero_linea = numero_linea + 1
        id_material = encriptar.encriptador(str(id))
        opcion = "0"

        posicion_texto = cadena.find(id_material)
        if posicion_texto >= 0:

            leer = line.strip()
            leer = leer.strip("\t")
            # Hago un split de cadena para crear un arreglo del registro
            arreglo = leer.split(sep='|')

            # Desencriptando la informacion
            id_material = encriptar.desencriptar(arreglo[1].strip())
            des_material = encriptar.desencriptar(arreglo[2].strip())
            cantidad = encriptar.desencriptar(arreglo[3].strip())
            verificado = encriptar.desencriptar(arreglo[4].strip())

            opcion = "1"
            while opcion != "2":
                print("\nEliminar material")
                print("\nID Material:", id_material)

                if (opcion := input(f"Desea eliminar \n\tEl material: \t {id_material} \n\tMaterial: \t{des_material}\n\tCantidad: \t{cantidad}\n\tVerificado: \t{verificado}\n1) si \n2) no\n")) == "1":
                    break
                elif opcion == "2":
                    break
            break

    archivo.close()

    if posicion_texto < 0:
        print("\nNo existe el material ", id)
        tecla_esperar()
    else:
        if opcion == "1":
            archivo = establecer_archivo('datatable.txt', 'r')
            lineas = archivo.readlines()
            archivo.close()

            archivo = establecer_archivo('datatable.txt', 'w')
            
            posicion = 1
            print("linea: ", numero_linea-2, numero_linea-1)
            for linea in lineas:
                if (posicion != (numero_linea) and posicion != (numero_linea+1)):
                    print("linea: ", linea, posicion, numero_linea-1, numero_linea-2)
                    archivo.write(linea)
                posicion += 1
            archivo.close()

            print("\nSe elimino el material", id)
            tecla_esperar()

def actualizar_inventario(id):
    archivo = establecer_archivo('datatable.txt', 'r')
    numero_linea = 0
    inventario = []

    for line in archivo:
        cadena = line[:20]
        numero_linea = numero_linea + 1
        id_material = encriptar.encriptador(str(id))
        cambios = ""

        posicion_texto = cadena.find(id_material)
        if posicion_texto >= 0:

            leer = line.strip()
            leer = leer.strip("\t")
            # Hago un split de cadena para crear un arreglo del registro
            arreglo = leer.split(sep='|')

            # Desencriptando la informacion
            id_material = encriptar.desencriptar(arreglo[1].strip())
            des_material = encriptar.desencriptar(arreglo[2].strip())
            cantidad = encriptar.desencriptar(arreglo[3].strip())
            verificado = encriptar.desencriptar(arreglo[4].strip())

            opcion = "1"
            while opcion != "4":
                print("\nActualizar material")
                print("\nID Material:", id_material)

                if (opcion := input(f"Que dato desea modificar, selecione una opción:\n1) Material: \t{des_material}\n2) Cantidad: \t{cantidad}\n3) Verificado: \t{verificado}\n4) Salir y Actualizar\n")) == "1":
                    des_material = input("\tIngrese la descripción del material: ").lower()
                elif opcion == "2":
                    cantidad = input("\tingrese la cantidad del material: ").lower()
                elif opcion == "3":
                    verificado = input("\tSe verificó el material antes de ser usado? escriba [si] o [no]: ").lower()
                elif opcion == "4":
                    break

            id_material = encriptar.encriptador(str(id_material))
            des_material = encriptar.encriptador(des_material.lower())
            cantidad = encriptar.encriptador(cantidad.lower())
            verificado = encriptar.encriptador(verificado.lower())
            
            # añade los valores al arreglo
            inventario.append((id_material, des_material, cantidad, verificado))

            for row in inventario:
                str_1 = wordfill(str(row[0]), 20)
                str_2 = wordfill(row[1], 20)
                str_3 = wordfill(row[2], 20)
                str_4 = wordfill(row[3], 20)
                cambios = ('|{}|\t{}|\t{}|\t{}|\t\n'.format(str_1, str_2, str_3, str_4))

            break

    archivo.close()

    if posicion_texto < 0:
        print("\nNo existe el material ", id)
        tecla_esperar()
    else:
        archivo = establecer_archivo('datatable.txt', 'r+')
        texto = archivo.readlines()

        # Modificamos la línea que queramos a partir del índice
        texto[numero_linea-1] = cambios

        # Volvemos a ponter el puntero al inicio y reescribimos
        archivo.seek(0)
        archivo.writelines(texto)
        archivo.close()

        print("\nSe actualizo el material", id)
        tecla_esperar()

def reporte_inventario():
    archivo = establecer_archivo('datatable.txt', 'r')

    for line in archivo:
        if (line[:1] == "-"):
            print(line)
        else:
            leer = line.strip()
            leer = leer.strip("\t")
            arreglo = leer.split(sep='|')
            if arreglo[1].strip() == "ID":
                print(line)
            else:
                id_material = wordfill(encriptar.desencriptar(arreglo[1].strip()), 20)
                des_material = wordfill(encriptar.desencriptar(arreglo[2].strip()), 20)
                cantidad = wordfill(encriptar.desencriptar(arreglo[3].strip()), 20)
                verificado = wordfill(encriptar.desencriptar(arreglo[4].strip()), 20)

                print('|{}|\t{}|\t{}|\t{}|\t\n'.format(id_material, des_material, cantidad, verificado))

    archivo.close()
    tecla_esperar()
