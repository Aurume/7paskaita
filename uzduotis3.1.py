# Perdaryti 1 užduotį taip, kad jei kuriant objektą, nepaduodamas joks tekstas,
# veiksmai turi būti atliekami su „Zen of Python“ tekstu.

# Parašyti klasę Sakinys, kuri turi savybę tekstas ir metodus, kurie:

class Sakinys:
    def __init__(self, mano_tekstas="Zen of Python"):
        self.mano_tekstas = mano_tekstas

# 1.1 Gražinti tekstą atbulai

    def atvirksciai(self):
        return self.mano_tekstas[::-1]

# 1.2 Gražina tekstą didžiosiomis raidėmis

    def didz_r(self):
        return self.mano_tekstas.upper()

#1.3 Gražina tekstą mažosiomis raidėmis
    def maz_r(self):
        return self.mano_tekstas.lower()

# 1.4 Gražina žodį pagal nurodytą eilės numerį
    def kelinta_spausdinu(self):
        po_zodi = self.mano_tekstas.split()
        return po_zodi[3]

# 1.5 Gražina, kiek tekste yra nurodytų simbolių arba žodžių
    def kiek_tekste_yra_kazko(self):
       return self.mano_tekstas.count("e")

# 1.6 Gražina tekstą su pakeistu nurodytu žodžiu arba simboliu
    def pervadinti(self, is_tokio, i_kitoki ):
        return self.mano_tekstas.replace(is_tokio, i_kitoki)

# 1.7 Atspausdina, kiek sakinyje yra žodžių, skaičių, didžiųjų ir mažųjų raidžių
    def zodziai_raides_sk(self):
        kiek_zodziu = len(self.mano_tekstas.split())
        kiek_didziuju = sum(x.isupper() for x in self.mano_tekstas)
        kiek_mazuju = sum(x.islower() for x in self.mano_tekstas)
        kiek_skaiciu = sum(x.isnumeric() for x in self.mano_tekstas)
        print(f"1.7. Žodžiai: {kiek_zodziu}, \n     Didžiosios raidės: {kiek_didziuju}, \n     Mažosios raidės: {kiek_mazuju}, \n     Skaičių yra: {kiek_skaiciu}.")

# 1.8 Susikurti kelis klasės objektus ir išbandyti visus metodus

mano_tekstas = Sakinys()

print(f"1.1. {mano_tekstas.atvirksciai()}")
print(f"1.2. {mano_tekstas.didz_r()}")
print(f"1.3. {mano_tekstas.maz_r()}")
#print(f"1.4. {mano_tekstas.kelinta_spausdinu()}")
#print(f"1.5. {mano_tekstas.kiek_tekste_yra_kazko()}")
print(f"1.6. {mano_tekstas.pervadinti('su', 'KAIP')}")  #daryt skirtingas kabutes, skliaustuose ir uz ju, nes kitaip klaida
mano_tekstas.zodziai_raides_sk()

