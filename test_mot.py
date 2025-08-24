import unittest

class TestMot(unittest.TestCase):
    def test_mettrep_maj(self):
        mot = "hello"
        resultat_attendu = "Hello"
        self.assertEqual(mot.capitalize(), resultat_attendu)

    def test_convertir_maj(self):
        mot = "hello"
        resultat_attendu = "HELLO"
        self.assertEqual(mot.upper(), resultat_attendu)

if __name__ == "__main__":
    unittest.main()