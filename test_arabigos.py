import unittest


class RomanoTest(unittest.TestCase):
    def test_Descomponer(self):
        self.assertEqual(descomponer(1987), [1,9,8,7])
    
    def test_descomponer_solo_enteros(self):
        self.assertRaises(SyntaxError, descomponer, 1987.0)
        
    def test_convertir_987(self):
         self.assertEqual(convertir(1987), [1,9,8,7], "CMLXXXVII")
    
    def test_entero_a_romano(self):
        self.assertEqual(entero_a_Romano(1987), "MCMLXXXVII")
        self.assertRaises(OverflowError)
    