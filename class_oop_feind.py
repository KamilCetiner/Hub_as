class Feind():
    Leben = 4
    def Attacke(self):
        print("Looooosssss")
        self.Leben -= 1

    def Lebende(self):
        if (self.Leben <=0):
            print("Tot")
        else:
            print(str(self.Leben) + " " + "noch ich habe")

Feind1 = Feind()
Feind2 = Feind()


Feind1.Attacke()
Feind1.Attacke()
Feind1.Attacke()
Feind2.Attacke()

Feind1.Lebende()
Feind2.Lebende()
