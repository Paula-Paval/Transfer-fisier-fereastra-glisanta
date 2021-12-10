

class Deserealizare:
    def deserealizare(self, lista_pachete):
        lista = []
        #data = json.load(lista_pachete)

        nr = lista_pachete[0]['numar_pachete']
        print(nr)

        text = ""
        for i in range(0, nr):
            text = text + lista_pachete[i]['data']
            dictionar = {'nr_pachet': lista_pachete[i]['nr_pachet']}
            lista.append(dictionar)

        return text
