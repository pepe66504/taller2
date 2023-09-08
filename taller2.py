contactos ={"nombre":"juan","numero":3235901594,"direccion":"calle 91#92 a.31"}


print(contactos)


configurar = 1


nombre = contactos.get("nombre")

while configurar == 1:
    configurar = int(input("desea configurar sus datos\n1.si \n2.no:"))
    if configurar ==1:
        
        opciones = int(input(f"\neliga opcion(\n1.eliminar dato \n2.actualizar dato\n3.consular dato \n4.agregar dato): "))
        if opciones == 1:
            opcion_eliminar = int(input("\neliga dato a eliminar \n1.nombre \n2.numero \n3.direccion:"))
            if opcion_eliminar == 1:
                eliminao=contactos.pop("nombre")
                print(f"\n",contactos)
            elif opcion_eliminar == 2:
                 eliminao=contactos.pop("numero")
                 print(f"\n",contactos)
            elif opcion_eliminar == 3:
                eliminao=contactos.pop("direccion")
                print(f"\n",contactos)
        elif opciones == 2:
            opcion_editar = int(input("\neliga dato a editar \n1.nombre \n2.numero \n3.direccion:"))
            if opcion_editar == 1:
                actualizacion_nombre = input("ingrese nuevo nombre: ")               
                contactos["nombre"] = actualizacion_nombre
                print(f"\n",contactos)
            elif opcion_editar == 2:
                 actualizacion_numero = int(input("ingrese nuevo numero: "))               
                 contactos["numero"] = actualizacion_numero
                 print(f"\n",contactos)
            elif opcion_editar == 3:
                actualizacion_direccion = input("ingrese nueva direccion: ")               
                contactos["direccion"] = actualizacion_direccion
                print(f"\n",contactos)
        elif opciones ==3:
            opcion_consultar = int(input("\neliga dato a consultar \n1.nombre \n2.numero \n3.direccion:"))
            if opcion_consultar == 1:
                nombre = contactos.get("nombre")
                print(f"\n",nombre)
            elif opcion_consultar == 2:
                 numero = contactos.get("numero")
                 print(f"\n",numero)
            elif opcion_consultar == 3:
                direccion = contactos.get("diereccion")
                print(f"\n",direccion)
        elif opciones == 4:
            nuevodato = input("\ningrese nuevo indice de dato:")
            dato = input("\ningrese dato:")
            contactos[nuevodato] = dato
            print(f"\n",contactos)
    elif configurar ==2:
        print(f"\n el concato con las modificaciones: ", contactos)