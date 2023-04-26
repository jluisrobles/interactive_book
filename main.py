#practicing

# BOOK (NOCGE EN UNA CUEVA)
pages=[
        "Page 0) Todo estaba apareciendo al final de eltune \n quizas alguien me buscara \n Que vas hacer? \n 1) EScuchar el viento \n 3) saltar a otro nivel",
        "Page 1) El viento se escuchaba y el frio se sentia \n algo de luz al final del tunel \n 1) Viento \n 2) Salir \n 3) Escuchar",
        "Page 2) Quice salir pero tenia miedo \n oscurecio y tenia hambre \n La historia llego a su... \n FIN.",
        "Page 3) Se escuchaban aullidos y gritos \n supongo que habia algien buscandome \n 0) Inicio \n 4) Murnullos \n 5) Correr ",
        "Page 4) Los murmullos en mi mente seguian \n solo era el estres de estar solo toda la noche",
        "Page 5) Queria correr pero no tenia fuerzas \n No se veia nada por la socuridad de la noche"
]
def showPage(pageNumber):
         text = pages[pageNumber]
         print (text)
         responce = input()
         showPage (int(responce))

showPage(0)