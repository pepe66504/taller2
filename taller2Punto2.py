contactos =[]
print(contactos)
configurar = 1
while configurar == 1:
    configurar = int(input("desea configurar sus datos\n1.si \n2.no:"))
    if configurar ==1:       
        opciones = int(input(f"\neliga opcion(\n1.eliminar dato \n2.actualizar dato\n3.consular dato \n4.agregar dato): "))
        if opciones == 1:
            opcion_eliminar = (input("que contacto vas a eliminar"))
            contactos.remove(opcion_eliminar)
            print(f"\n",contactos)
        elif opciones == 2:
            opcion_editar = (input("que dato desea editar"))
            actualizacion_nombre = input("ingrese nuevo nombre: ")               
            posicion=contactos.index(opcion_editar)
            contactos[posicion]=actualizacion_nombre
            print(f"\n",contactos)
        elif opciones ==3:
            opcion_consultar = (input("que nombre quiere consultar"))
            posicion=contactos.index(opcion_consultar)
            print(contactos[posicion])
        elif opciones == 4:
            dato = input("\ningrese dato:")
            contactos.append(dato)
            print(f"\n",contactos)