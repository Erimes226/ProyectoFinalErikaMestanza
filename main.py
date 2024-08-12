from accessData.conexionOrm import Database, DATABASE_URL
from accessData.entities.model import BaseDeDatos
from dominio.entities.modelsOrm.dto import VeterinariaDTO, MascotaDTO
from servicios.service import VeterinariaService


def mostrar_veterinaria(veterinaria):
    for vete in veterinaria:
        print(f"Veterinaria: id={vete.id_veterinaria}, nombre={vete.nombre}")


def main():

    servicio = VeterinariaService(db)

    while True:
        
        print("\n--- MENU ---")
        print("1. Gestion veterinaria")
        print("2. Gestion Mascotas")
        print("3. Salir")
        opcion= input("selecione una opción")

        if opcion == "1":
            while True:
                print("\n--- Menú veterinaria ---")
                print("1. Crear Veterinaria")
                print("2. Mostrar todas las veterinarias")
                print("3. buscar veterinaria")
                print("4. Actualizar veterinaria")
                print("5. Eliminar veterinaria")
                print("6. volver a Menu")

                opcion = input("Seleccione una opción: ")

                if opcion == "1":
                    nombre = input("Ingrese el nombre de la veterinaria: ")
                    
                    vete = VeterinariaDTO(None, nombre)
                    servicio.crear_veterinaria(vete)
                    print(f"Veterinaria creada: id={vete.id_veterinaria}, nombre={vete.nombre}")


                elif opcion == "2":
                    veterinaria = servicio.ver_veterinarias()
                    mostrar_veterinaria(veterinaria)

                elif opcion == "3":
                    estudianteId = int(input("Ingrese el ID de la veterinaria a consultar: "))
                    veterinaria = servicio.buscar_veterinaria(estudianteId)
                    if veterinaria:
                        print(f"Veterinaria: id={veterinaria.id_veterinaria}, nombre={veterinaria.nombre}")
                    else:
                        print("Veterinaria no encontrada.")


                elif opcion == "4":
                    id_vete = int(input("Ingrese el ID de la veterinaria que desea actualizar: "))
                    veterinaria = servicio.buscar_veterinaria(id_vete)
                    if veterinaria:
                        nuevo_nombre = input(f"Ingrese el nuevo nombre (nombre actual: {veterinaria.nombre}")
                    
                        veterinaria_actualizada = VeterinariaDTO(id_vete, nuevo_nombre)
                        servicio.actualizar_veterinaria(veterinaria_actualizada)

                        print("Veterinaria actualizada")
                    else:
                        print("Veterinaria no encontrada.")

                elif opcion == "5":
                    veterinariaId = int(input("Ingrese el ID de la veterinaria que desea eliminar: "))
                    veterinaria = servicio.buscar_veterinaria(veterinariaId)

                    if veterinaria:
                        servicio.borrar_veterinaria(veterinariaId)
                        print("Veterinaria eliminada exitosamente.")
                    else:
                        print("Veterinaria no encontrada.")

                elif opcion == "6":
                    servicio.cerrarConexion()
                    break

                else:
                    print("Opción inválida. Por favor, seleccione una opción válida.")
        if opcion == "2":
            while True:
                print("\n--- Menú Mascota ---")
                print("1. Crear Mascota")
                print("2. Mostrar todas las Mascotas")
                print("3. buscar Mascota")
                print("4. Actualizar Mascota")
                print("5. Eliminar Mascota")
                print("6. volver a Menu")


                opcion= input("selecione una opción")

                if opcion == "1":
                    
                    nombre = input("Ingrese el nombre de la mascota: ")
                    tipo = input("Ingrese el tipo de mascota (perro, gato, etc.): ")
                    edad = int(input("Ingrese la edad de la mascota: "))

                    # Obtener y mostrar las veterinarias disponibles
                    veterinarias = servicio.ver_veterinarias()
                    print("Veterinarias disponibles:")
                    for vete in veterinarias:
                        print(f"ID: {vete.id_veterinaria}, Nombre: {vete.nombre}")

                    id_veterinaria = int(input("Ingrese el ID de la veterinaria en la que se encuentra la mascota: "))

                    mascota_dto = MascotaDTO(nombre=nombre, tipo=tipo, edad=edad, id_veterinaria=id_veterinaria)

                    # Crear la mascota en la base de datos
                    mascota = servicio.crear_mascota(mascota_dto)
                    print(f"Mascota creada: {mascota.nombre}, ID: {mascota.id_mascota}, Tipo: {mascota.tipo}, Edad: {mascota.edad} ")

                elif opcion == "2":
                    mascotas = servicio.ver_mascotas()
                    if mascotas:
                        for mascota in mascotas:
                            veterinaria = servicio.buscar_veterinaria(mascota.id_veterinaria)
                            print(f"ID: {mascota.id_mascota}, Mascota: {mascota.nombre}, Tipo: {mascota.tipo}, Edad: {mascota.edad}, Veterinaria: {veterinaria.nombre if veterinaria else 'No asignada'}")
                    else:
                        print("No hay mascotas registradas.")

                elif opcion == "3":
                    mascota_id = int(input("Ingrese el ID de la mascota: "))
                    mascota, veterinaria = servicio.buscar_mascota(mascota_id)
                    if mascota:
                        print(f"Mascota: {mascota.nombre}, Tipo: {mascota.tipo}, Edad: {mascota.edad}")
                        if veterinaria:
                            print(f"se encuentra en la veterinaria: {veterinaria.nombre}")
                        else:
                            print("Esta mascota no está asignada a ninguna veterinaria.")
                    else:
                        print("No se encontró una mascota con ese ID.")  

                elif opcion == "4":
                    mascota_id = int(input("Ingrese el ID de la mascota a actualizar: "))
                    mascota, veterinaria = servicio.buscar_mascota(mascota_id)
                    
                    if mascota:
                       
                        nombre = input(f"Ingrese el nuevo nombre de la mascota (actual: {mascota.nombre}): ") or mascota.nombre
                        tipo = input(f"Ingrese el nuevo tipo de la mascota (actual: {mascota.tipo}): ") or mascota.tipo
                        edad = input(f"Ingrese la nueva edad de la mascota (actual: {mascota.edad}): ")
                        edad = int(edad) if edad else mascota.edad

                        veterinarias = servicio.ver_veterinarias()
                        for vete in veterinarias:
                            print(f"ID: {vete.id_veterinaria}, Nombre: {vete.nombre}")
                        id_veterinaria = input(f"Ingrese el nuevo ID de la veterinaria (actual: {mascota.id_veterinaria}): ")
                        id_veterinaria = int(id_veterinaria) if id_veterinaria else mascota.id_veterinaria

                       
                        mascota_dto = MascotaDTO(
                            id_mascota=mascota_id,
                            nombre=nombre,
                            tipo=tipo,
                            edad=edad,
                            id_veterinaria=id_veterinaria
                        )

                        
                        mascota_actualizada = servicio.actualizar_mascota(mascota_dto)
                        print(f"Mascota actualizada: {mascota_actualizada.nombre}, ID: {mascota_actualizada.id_mascota}")
                    else:
                        print("Mascota no encontrada.")

                        if opcion == "3":
                            servicio.cerrarConexion()
                            print("¡Hasta luego!")
                            break
                            
                elif opcion == "5":
                    mascotaId = int(input("Ingrese el ID de la mascota que desea eliminar: "))
                    mascota = servicio.buscar_mascota(mascotaId)

                    if mascota:
                        servicio.borrar_mascota(mascotaId)
                        print("Mascota eliminada exitosamente.")
                    else:
                        print("Mascota no encontrada.")

                elif opcion == "6":
                    servicio.cerrarConexion()
                    break


if __name__ == "__main__":
    db = Database(DATABASE_URL)
    engine = db.engine
    BaseDeDatos.metadata.create_all(bind=engine)
    main()