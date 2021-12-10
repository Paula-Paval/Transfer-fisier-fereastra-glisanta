import json
import math


class Serializare:

    def __init__(self, fileName):
        self.fileName=fileName
    def serializare(self):
        list = []
        with open(self.fileName) as f:
            text = f.read()
            nrofchar = len(text)
            print(nrofchar)
            nr_pachete = math.ceil(nrofchar / 3)
            print(nr_pachete)
            nr = 0
            data = ""
            num_pachet = 1
            for caracter in text:
                if (nr % 3 == 0 and nr != 0):
                    dic = {"nr_pachet": num_pachet, "data": data, "numar_pachete": nr_pachete}
                    num_pachet = num_pachet + 1
                    list.append(dic)
                    data = caracter
                else:
                    data = data + caracter
                nr = nr + 1
            dic = {"nr_pachet": num_pachet, "data": data, "numar_pachete": nr_pachete}
            list.append(dic)

        return list

        # out_file = open("test2.json", "w")
        # json.dump(list, out_file, indent=4)
        # out_file.close()