from Kerri import Kerri

class KerriElektrik(Kerri):
    def __init__(self,name,vitiProdhimit,dyert,ngjyra,bateria):
        super().__init__(name,vitiProdhimit,dyert,ngjyra)
        self.bateria=bateria

        def mbusheBaterin(self):
            print("bateria eshte duke mbushur")