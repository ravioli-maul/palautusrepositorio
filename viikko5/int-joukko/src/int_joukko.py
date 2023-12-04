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

        for indeksi in range(0, self.alkioiden_maara):
            if luku == self.lukujono[indeksi]:
                osumat += 1

        return osumat > 0

    def lisaa(self, luku):
        if self.alkioiden_maara == 0:
            self.lukujono[0] = luku
            self.alkioiden_maara += 1
            return True

        if not self.kuuluu(luku):
            self.lukujono[self.alkioiden_maara] = luku
            self.alkioiden_maara += 1

            if self.alkioiden_maara % len(self.lukujono) == 0:
                taysi_lukujono = self.lukujono
                self.kopioi_lista(self.lukujono, taysi_lukujono)
                self.lukujono = self._luo_lista(self.alkioiden_maara + self.kasvatuskoko)
                self.kopioi_lista(taysi_lukujono, self.lukujono)

            return True

        return False

    def poista(self, luku):
        kohta = -1
        apu = 0

        for indeksi in range(0, self.alkioiden_maara):
            if luku == self.lukujono[indeksi]:
                kohta = indeksi  # siis luku löytyy tuosta kohdasta :D
                self.lukujono[kohta] = 0
                break

        if kohta != -1:
            for j in range(kohta, self.alkioiden_maara - 1):
                apu = self.lukujono[j]
                self.lukujono[j] = self.lukujono[j + 1]
                self.lukujono[j + 1] = apu

            self.alkioiden_maara = self.alkioiden_maara - 1
            return True

        return False

    def kopioi_lista(self, a, b):
        for i in range(0, len(a)):
            b[i] = a[i]

    def mahtavuus(self):
        return self.alkioiden_maara

    def to_int_list(self):
        taulu = self._luo_lista(self.alkioiden_maara)

        for i in range(0, len(taulu)):
            taulu[i] = self.lukujono[i]

        return taulu

    @staticmethod
    def yhdiste(a, b):
        x = IntJoukko()
        a_taulu = a.to_int_list()
        b_taulu = b.to_int_list()

        for i in range(0, len(a_taulu)):
            x.lisaa(a_taulu[i])

        for i in range(0, len(b_taulu)):
            x.lisaa(b_taulu[i])

        return x

    @staticmethod
    def leikkaus(a, b):
        y = IntJoukko()
        a_taulu = a.to_int_list()
        b_taulu = b.to_int_list()

        for i in range(0, len(a_taulu)):
            for j in range(0, len(b_taulu)):
                if a_taulu[i] == b_taulu[j]:
                    y.lisaa(b_taulu[j])

        return y

    @staticmethod
    def erotus(a, b):
        z = IntJoukko()
        a_taulu = a.to_int_list()
        b_taulu = b.to_int_list()

        for i in range(0, len(a_taulu)):
            z.lisaa(a_taulu[i])

        for i in range(0, len(b_taulu)):
            z.poista(b_taulu[i])

        return z

    def __str__(self):
        if self.alkioiden_maara == 0:
            return "{}"
        elif self.alkioiden_maara == 1:
            return "{" + str(self.lukujono[0]) + "}"
        else:
            tuotos = "{"
            for i in range(0, self.alkioiden_maara - 1):
                tuotos = tuotos + str(self.lukujono[i])
                tuotos = tuotos + ", "
            tuotos = tuotos + str(self.lukujono[self.alkioiden_maara - 1])
            tuotos = tuotos + "}"
            return tuotos
