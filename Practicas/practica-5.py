
traductor = {"amor":"love", "abrazo":"hug"}

palabra = ""
while palabra != "0":
    palabra = input("Ingrese la palabra que quiere traducir: ")
    if palabra in traductor:
        print(f"(esp): {palabra}  (en): {traductor[palabra]}")
    elif palabra != "0":
        print("No se encuentra la palabra en el diccionario ")
        resp = input("¿Deseas agregarlo? S/N: ")
        if resp == "S":
            
            traduccion = input("Ingrese la traduccion de la palabra que quieres agregar: ")
            traductor[palabra] = traduccion
            print(traductor)
    elif palabra == "0":
        print("---El Diccionario se ha cerrado---")
