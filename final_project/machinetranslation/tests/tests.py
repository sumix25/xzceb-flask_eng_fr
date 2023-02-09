import unittest
from translator import *

class TestTranslateText(unittest.TestCase):
    def test_translate_textfr(self):
        text = "Hello"
        translated_text = englishToFrench(text)
        self.assertEqual(translated_text, "Bonjour")


    def test_translate_texten(self):
        text = "Bonjour"
        translated_text = frenchToEnglish(text)
        self.assertEqual(translated_text, "Hello")

if __name__ == '__main__':
    unittest.main()