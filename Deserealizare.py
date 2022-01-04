import json

class Deserealizare:

    def deserealizare(self, lista_pachete):
        lista = []
        data = lista_pachete

        nr = data[0]['numar_pachete']
        print(nr)

        text = ""
        for i in range(0, nr):
            text = text + data[i]['data']
            dictionar = {'nr_pachet': data[i]['nr_pachet']}
            lista.append(dictionar)

        print(text)
        return text
