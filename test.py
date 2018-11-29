import unittest
from vocab_builder import CharVocab, WordVocab


class VocabUnitTest(unittest.TestCase):
    def test_char_vocab_build(self):
        v = CharVocab(["안녕", "내 이름은", "뽀로로야"])
        self.assertEqual(15, len(v.itos))

    def test_word_vocab_build(self):
        v = WordVocab(["안녕", "내 이름은", "뽀로로야"])
        self.assertEqual(9, len(v.itos))
