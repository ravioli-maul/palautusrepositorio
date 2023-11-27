import unittest
from unittest.mock import Mock, ANY
from kauppa import Kauppa
from viitegeneraattori import Viitegeneraattori
from varasto import Varasto
from tuote import Tuote

class TestKauppa(unittest.TestCase):
    def setUp(self):
    # Testien yhteinen alustus 
        self.pankki_mock = Mock()
        self.viitegeneraattori_mock = Mock(wraps=Viitegeneraattori())
        self.varasto_mock = Mock()

        # palautetaan aina arvo 42
        # Ei enää...
        #self.viitegeneraattori_mock.uusi.return_value = 42

        # tehdään toteutus saldo-metodille
        def varasto_saldo(tuote_id):
            if tuote_id == 1:
                return 10
            if tuote_id == 2:
                return 50
            if tuote_id == 3:
                return 0

        # tehdään toteutus hae_tuote-metodille
        def varasto_hae_tuote(tuote_id):
            if tuote_id == 1:
                return Tuote(1, "maito", 5)
            if tuote_id == 2:
                return Tuote(1, "leipä", 4)
            if tuote_id == 3:
                return Tuote(1, "voi", 8)

        # otetaan toteutukset käyttöön
        self.varasto_mock.saldo.side_effect = varasto_saldo
        self.varasto_mock.hae_tuote.side_effect = varasto_hae_tuote

        # alustetaan kauppa
        self.kauppa = Kauppa(self.varasto_mock, self.pankki_mock, self.viitegeneraattori_mock)

    def test_ostoksen_paatyttya_pankin_metodia_tilisiirto_kutsutaan(self):
        # tehdään ostokset
        self.kauppa.aloita_asiointi()
        self.kauppa.lisaa_koriin(1)
        self.kauppa.tilimaksu("pekka", "12345")

        # varmistetaan, että metodia tilisiirto on kutsuttu
        self.pankki_mock.tilisiirto.assert_called()
        # toistaiseksi ei välitetä kutsuun liittyvistä argumenteista

    def test_ostoksen_paatyttya_pankin_metodia_tilisiirto_kutsutaan_oikeilla_argumenteilla(self):
        # tehdään ostokset
        self.kauppa.aloita_asiointi()
        self.kauppa.lisaa_koriin(1)
        self.kauppa.tilimaksu("pekka", "12345")

        # Testi argumenteilla
        self.pankki_mock.tilisiirto.assert_called_with(
            "pekka", ANY, "12345", ANY, 5
        )

    def test_ostetaan_kaksi_samaa_tuotetta_pankin_metodia_tilisiirto_kutsutaan_oikeilla_argumenteilla(self):
        # tehdään ostokset
        self.kauppa.aloita_asiointi()
        self.kauppa.lisaa_koriin(1)
        self.kauppa.lisaa_koriin(1)
        self.kauppa.tilimaksu("pekka", "12345")

        # Testi argumenteilla
        self.pankki_mock.tilisiirto.assert_called_with(
            "pekka", ANY, "12345", ANY, 10
        )

    def test_ostetaan_kaksi_eri_tuotetta_pankin_metodia_tilisiirto_kutsutaan_oikeilla_argumenteilla(self):
        # tehdään ostokset
        self.kauppa.aloita_asiointi()
        self.kauppa.lisaa_koriin(1)
        self.kauppa.lisaa_koriin(2)
        self.kauppa.tilimaksu("pekka", "12345")

        # Testi argumenteilla
        self.pankki_mock.tilisiirto.assert_called_with(
            "pekka", ANY, "12345", ANY, 5 + 4
        )

    def test_ostetaan_kaksi_eri_tuotetta_toinen_loppu_pankin_metodia_tilisiirto_kutsutaan_oikeilla_argumenteilla(self):
        # tehdään ostokset
        self.kauppa.aloita_asiointi()
        self.kauppa.lisaa_koriin(1)
        self.kauppa.lisaa_koriin(3)
        self.kauppa.tilimaksu("pekka", "12345")

        # Testi argumenteilla
        self.pankki_mock.tilisiirto.assert_called_with(
            "pekka", ANY, "12345", ANY, 5
        )

    def test_aloita_asionti_nollaa_edellisen_ostoksen(self):
        # tehdään ensimmäiset ostokset
        self.kauppa.aloita_asiointi()
        self.kauppa.lisaa_koriin(1)
        self.kauppa.tilimaksu("pekka", "12345")

        # Resetoidaan pankki_mock
        #self.pankki_mock.reset_mock()

        # tehdään toiset ostokset
        self.kauppa.aloita_asiointi()
        self.kauppa.lisaa_koriin(2)
        self.kauppa.tilimaksu("pekka", "12345")
        
        # Tarkastetaan että oikea hinta tilisiirrossa
        self.pankki_mock.tilisiirto.assert_called_with(
            "pekka", ANY, "12345", ANY, 4
        )

    def test_uusi_viitenumero_jokaiselle_maksutapahtumalle(self):
        # tehdään ostokset ja maksetaan
        self.kauppa.aloita_asiointi()
        self.kauppa.lisaa_koriin(1)
        self.kauppa.tilimaksu("pekka", "12345")

        # Tarkastetaan että viitegeneraattoria on kutsuttu kerran testin aikana
        self.assertEqual(self.viitegeneraattori_mock.uusi.call_count, 1)

        # tehdään toiset ostokset ja maksetaan
        self.kauppa.aloita_asiointi()
        self.kauppa.lisaa_koriin(2)
        self.kauppa.tilimaksu("pekka", "12345")

        # Tarkastetaan että viitegeneraattoria on kutsuttu kahdesti testin aikana
        self.assertEqual(self.viitegeneraattori_mock.uusi.call_count, 2)

        # tehdään vielä kolmannnet ostokset ja maksetaan
        self.kauppa.aloita_asiointi()
        self.kauppa.lisaa_koriin(1)
        self.kauppa.tilimaksu("pekka", "12345")

        # Tarkastetaan että viitegeneraattoria on kutsuttu kolmesti testin aikana
        self.assertEqual(self.viitegeneraattori_mock.uusi.call_count, 3)

    def test_poista_korista_poistaa_tuotteen_korista(self):
        # Lisätään ja poistetaan korista, maksun tulee olla nolla.
        self.kauppa.aloita_asiointi()
        self.kauppa.lisaa_koriin(1)
        self.kauppa.poista_korista(1)
        self.kauppa.tilimaksu("pekka", "12345")

        self.pankki_mock.tilisiirto.assert_called_with(
        "pekka", ANY, "12345", ANY, 0
    )


