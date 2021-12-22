import unittest
from math import pi

from kreis import kreis_flaeche
# from app.kreis import kreis_flaeche


class Kreistest(unittest.TestCase):

    def test_kreis_flaeche(self):
        # Tests bei Radius >= 0
        self.assertAlmostEqual(kreis_flaeche(1), pi)
        self.assertAlmostEqual(kreis_flaeche(0), 0)
        self.assertAlmostEqual(kreis_flaeche(3.1), pi * 3.1**2)

    def test_werte(self):
        # gebe Fehler aus, wenn Werte ungültig sind
        self.assertRaises(ValueError, kreis_flaeche, -2)   