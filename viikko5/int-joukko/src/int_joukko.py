KAPASITEETTI = 5
OLETUSKASVATUS = 5


class IntJoukko:
    def _luo_lista(self, koko):
        return [0] * koko

    def __init__(self, kapasiteetti=KAPASITEETTI, kasvatuskoko=OLETUSKASVATUS):
        if not isinstance(kapasiteetti, int) or kapasiteetti < 0:
            raise Exception("Väärä kapasiteetti")
        if not isinstance(kasvatuskoko, int) or kasvatuskoko < 0:
            raise Exception("Väärä kasvatuskoko")

        self.kapasiteetti = kapasiteetti
        self.kasvatuskoko = kasvatuskoko

        self.lukujono = self._luo_lista(self.kapasiteetti)

        self.alkioiden_maara = 0

    def kuuluu(self, luku):
        osumat = 0

        for i in range(0, self.alkioiden_maara):
            if luku == self.lukujono[i]:
                osumat += 1

        return osumat > 0

    def lisaa(self, luku):
        if not self.kuuluu(luku):
            if self.alkioiden_maara == len(self.lukujono):
                self.lukujono = self.lukujono + self._luo_lista(self.kasvatuskoko)

            self.lukujono[self.alkioiden_maara] = luku
            self.alkioiden_maara += 1
            return True

        return False

    def poista(self, luku):
        try:
            indeksi = self.lukujono.index(luku, 0, self.alkioiden_maara)
            self.lukujono.pop(indeksi)
            self.alkioiden_maara -= 1
            return True
        except ValueError:
            return False

    def mahtavuus(self):
        return self.alkioiden_maara

    def to_int_list(self):
        return self.lukujono[:self.alkioiden_maara]

    @staticmethod
    def yhdiste(joukko_a, joukko_b):
        yhdiste_joukko = IntJoukko()
        for luku in joukko_a.to_int_list():
            yhdiste_joukko.lisaa(luku)
        for luku in joukko_b.to_int_list():
            yhdiste_joukko.lisaa(luku)
        return yhdiste_joukko

    @staticmethod
    def leikkaus(joukko_a, joukko_b):
        leikkaus_joukko = IntJoukko()
        a_lista = joukko_a.to_int_list()
        b_lista = joukko_b.to_int_list()
        for luku in a_lista:
            if luku in b_lista:
                leikkaus_joukko.lisaa(luku)
        return leikkaus_joukko

    @staticmethod
    def erotus(joukko_a, joukko_b):
        erotus_joukko = IntJoukko()
        for luku in joukko_a.to_int_list():
            erotus_joukko.lisaa(luku)
        for luku in joukko_b.to_int_list():
            erotus_joukko.poista(luku)
        return erotus_joukko

    def __str__(self):
        if self.alkioiden_maara == 0:
            return "{}"
        if self.alkioiden_maara == 1:
            return "{" + str(self.lukujono[0]) + "}"

        esitys = "{"
        for i in range(0, self.alkioiden_maara - 1):
            esitys = esitys + str(self.lukujono[i])
            esitys = esitys + ", "
        esitys = esitys + str(self.lukujono[self.alkioiden_maara - 1])
        esitys = esitys + "}"
        return esitys
