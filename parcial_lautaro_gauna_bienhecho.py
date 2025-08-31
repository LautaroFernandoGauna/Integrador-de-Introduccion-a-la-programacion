import array as arr
import random
#vector_global.append(nro_aleatorio)

array_creado=False
array_lleno=False

def llenado(var):
    cantidad=random.randint(1,9)
    for _ in range(cantidad):
        var.append(1)
        
    return var


while True:
    opcion=int(input("Menu principal \n1. Crear array\n2. Llenar vector\n3. Mostrar array\n4. Modificar\n5. Salir\nOpcion: "))
    if opcion==1 and array_creado==False:
        
        vector_global= arr.array('i',[])
            
        print(vector_global)
        llenar=input(("""---------------Crear---------------
Array Creado
Presione ENTER para volver al Menú"""))
        array_creado=True
        

            
    elif opcion==2 and array_creado==True and array_lleno==False:
        
        vector_global=llenado(vector_global)
        print(f"Array lleno con {len(vector_global)} elementos.")
        array_lleno=True
        print(f"Array lleno con {len(vector_global)} elementos.")
        
        llenar=input((f'''---------------Llenar---------------
----array lleno, tiene, {len(vector_global)},elementos----
Presione ENTER para volver al Menú'''))
    elif opcion==3 and array_lleno==True:
        for indice, i in enumerate(vector_global):
            print(f"{indice}---{i}")

        llenar=input(("""Presione ENTER para volver al Menú"""))
        
    elif opcion==4 and array_lleno==True:
        eleccion=int(input(f"Ingrese una posición entre 0 y {len(vector_global)}: "))
        if eleccion < 0 or eleccion >len(vector_global):
            print("La posicion no existe")
        
        else:
            eleccion2=int(input("Ingrese un nuevo valor: "))
            vector_global[eleccion]=eleccion2
            print(vector_global)
            
        Menú=input("Presione ENTER para volver al Menú")
    elif opcion==4 and array_lleno==False:
        print("Array vacío")
        Menú=input("Presione ENTER para volver al Menú")
    elif opcion==5:
        break
    else:
        incorrecto=input(("""---------------Ingrese una opcion correcta---------------
Presione ENTER para volver al Menú"""))
        
print("Fin del programa")