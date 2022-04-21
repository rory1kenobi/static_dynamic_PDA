import unittest
from src.card import Card
from src.card_game import CardGame

class TestCardGame(unittest.TestCase):

    def setUp(self):
        self.card_1 = Card('Spade', 1)
        self.card_2 = Card('Heart', 7)
        self.cards = [self.card_1, self.card_2]

    def test_card_is_ace(self):
        self.assertEqual(True, CardGame.check_for_ace(self, self.card_1))

    def test_highest_card(self):
        self.assertEqual(self.card_2, CardGame.highest_card(self, self.card_1, self.card_2))

    def test_cards_total(self):
        self.assertEqual("You have a total of 8", CardGame.cards_total(self, self.cards))