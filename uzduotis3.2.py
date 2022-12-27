import datetime
import calendar

# Sukurti klasę Sukaktis, kuri turėtų savybę data (galima atskirai įvesti metus, mėnesius ir kt.) ir metodus
# kurie gražina, kiek nuo įvestos sukakties praėjo metų, savaičių, dienų, valandų, minučių, sekundžių

class Sukaktis:
    def __init__(self, metai, menuo, diena, valandos, minutes, sekundes):
        self.metai = metai
        self.menuo = menuo
        self.diena = diena
        self.valandos = valandos
        self.minutes = minutes
        self.sekundes = sekundes
        self.data = datetime.datetime(metai, menuo, diena, valandos, minutes, sekundes)

    def praejo_laiko(self):
        kiek_dienu = datetime.datetime.today() - self.data
        print("Praėjo metų: ", kiek_dienu.days // 365)
        print("Praėjo mėnesių: ", kiek_dienu.days // 365 * 12)
        print("Praėjo dienų: ", kiek_dienu.days)
        print("Praėjo valandų: ", round(kiek_dienu.total_seconds() // 3600))
        print("Praėjo minučių: ", round(kiek_dienu.total_seconds() / 60))
        print("Praėjo sekundžių: ", round(kiek_dienu.total_seconds()))

# Gražina, ar nurodytos sukakties metai buvo keliamieji.

    def tikrinam_ar_keliamieji(self):
        if calendar.isleap(self.metai):
            print("Metai yra keliamieji")

# Atima iš nurodytos datos nurodytą kiekį dienų ir gražina naują datą.

    def atimti(self, dienos):
        return self.data - datetime.timedelta(days=dienos)

# Prideda prie nurodytos datos nurodytą kiekį dienų ir gražina naują datą

    def prideti(self, dienos):
        return self.data + datetime.timedelta(days=dienos)





ivesta_sukaktis1 = Sukaktis(2000, 2, 2, 1, 1, 1)
ivesta_sukaktis1.praejo_laiko()

ivesta_sukaktis1.tikrinam_ar_keliamieji()
print(ivesta_sukaktis1.atimti(23))
print(ivesta_sukaktis1.prideti(18))