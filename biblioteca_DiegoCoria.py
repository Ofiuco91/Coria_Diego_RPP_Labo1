import json

def menu(): #genero el menu de opciones
    opcion = input("""------ Menu de opciones -----------
                1) Cargar archivo
                2) Imprimir lista
                3) Asignar totales
                4) Filtrar por tipo
                5) Mostrar servicios
                6) Guardar servicios
                7) Salir.
                   Opcion...""")
    return opcion

def cargar_archivo(archivo):
    #cargo el archivo ingresando el nombre por parametro
    try:
        with open(archivo, "r") as archivo: #selecciono para que se abra en formato "read"
            servicios = json.load(archivo) #lo cargo
        return servicios
    except FileNotFoundError:
        print("El archivo no existe.")
        return None
    
def guardar_archivo(nombre_archivo, servicios):
    # recibe un nombre y una lista y las guarda en un archivo json

    with open(nombre_archivo, 'w') as archivo:
        json.dump(servicios, archivo, indent=4)

def imprimir_lista(lista):
    #genero un for para que recorra las listas y las vaya imprimiendo en orden
    print("id_servicio //descripcion      // tipo        //precio unitario      //      cantidad    //total servicio")
    for i in lista:
        print(f"{i["id_servicio"]}            {i["descripcion"]}   {i["tipo"]}     {i["precioUnitario"]}             {i["cantidad"]}    {i["totalServicio"]}")

def asignar_totales(servicios):
    #recibe una lista y le asigna el resultado de multiplicar precio unitario por cantidad de cada uno
    for servicio in servicios:
        servicio["totalServicio"] = (lambda p, c: p * c)(float(servicio["precioUnitario"]), float(servicio["cantidad"]))
    return servicios



def filtar_por_tipo(servicios, tipo):
    #Recibe una lista y un string, los clasifica por tipo y retorna la lista
    filtrados = []
    for servicio in servicios:
        if servicio["tipo"] == (tipo.capitalize()):#hago que la primera letra siempre se ponga en mayuscula
            filtrados.append(servicio)

    return filtrados

def ordenar_servicios_ascendente(servicios):
    #Recibe una lista y ordena los servicios
    return sorted(servicios, key=lambda x: x["descripcion"])

