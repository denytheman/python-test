from unittest import TestCase

from models.item import ItemModel


class ItemTest(TestCase):
    def setUp(self):
        self.item = ItemModel('test', 19.99)

    def test_create_item(self):
        self.assertEqual(self.item.name, 'test',
                         "The name of the item after creation does not equal the constructor argument")
        self.assertEqual(self.item.price, 19.99,
                         "The price of the item after creation does not equal the constructor argument")

    def test_item_json(self):
        expected = {
            'name': 'test',
            'price': 19.99
        }

        self.assertEqual(self.item.json(),
                         expected,
                         "The JSON export of the item is incorrect. Received {}, expected {}".format(self.item.json(),
                                                                                                     expected))
