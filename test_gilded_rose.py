# -*- coding: utf-8 -*-
import unittest

from gilded_rose import GildedRose
from items import Item


class GildedRoseTest(unittest.TestCase):
    def test_general_item(self):
        items_input = [
            Item(name="+5 Dexterity Vest", sell_in=10, quality=10),
            Item(name="+5 Dexterity Vest", sell_in=1, quality=10),
            Item(name="+5 Dexterity Vest", sell_in=0, quality=10),
            Item(name="+5 Dexterity Vest", sell_in=10, quality=0),
            Item(name="+5 Dexterity Vest", sell_in=-10, quality=1),
        ]

        items_expected = [
            Item(name="+5 Dexterity Vest", sell_in=9, quality=9),
            Item(name="+5 Dexterity Vest", sell_in=0, quality=9),
            Item(name="+5 Dexterity Vest", sell_in=-1, quality=8),
            Item(name="+5 Dexterity Vest", sell_in=9, quality=0),
            Item(name="+5 Dexterity Vest", sell_in=-11, quality=0),
        ]

        gilded_rose = GildedRose(items_input)
        gilded_rose.update_quality()
        self._assert_item_lists_equality(gilded_rose.inventory, items_expected)

    def test_cheese_item(self):
        items_input = [
            Item(name="Aged Brie", sell_in=10, quality=0),
            Item(name="Aged Brie", sell_in=0, quality=0),
            Item(name="Aged Brie", sell_in=-10, quality=0),
            Item(name="Aged Brie", sell_in=10, quality=49),
            Item(name="Aged Brie", sell_in=10, quality=50),
        ]

        items_expected = [
            Item(name="Aged Brie", sell_in=9, quality=1),
            Item(name="Aged Brie", sell_in=-1, quality=2),
            Item(name="Aged Brie", sell_in=-11, quality=2),
            Item(name="Aged Brie", sell_in=9, quality=50),
            Item(name="Aged Brie", sell_in=9, quality=50),
        ]

        gilded_rose = GildedRose(items_input)
        gilded_rose.update_quality()
        self._assert_item_lists_equality(gilded_rose.inventory, items_expected)

    def test_backstage_item(self):
        items_input = [
            Item(
                name="Backstage passes to a TAFKAL80ETC concert", sell_in=20, quality=10
            ),
            Item(
                name="Backstage passes to a TAFKAL80ETC concert", sell_in=10, quality=10
            ),
            Item(
                name="Backstage passes to a TAFKAL80ETC concert", sell_in=5, quality=10
            ),
            Item(
                name="Backstage passes to a TAFKAL80ETC concert", sell_in=2, quality=10
            ),
            Item(
                name="Backstage passes to a TAFKAL80ETC concert", sell_in=0, quality=10
            ),
        ]

        items_expected = [
            Item(
                name="Backstage passes to a TAFKAL80ETC concert", sell_in=19, quality=11
            ),
            Item(
                name="Backstage passes to a TAFKAL80ETC concert", sell_in=9, quality=12
            ),
            Item(
                name="Backstage passes to a TAFKAL80ETC concert", sell_in=4, quality=13
            ),
            Item(
                name="Backstage passes to a TAFKAL80ETC concert", sell_in=1, quality=13
            ),
            Item(
                name="Backstage passes to a TAFKAL80ETC concert", sell_in=-1, quality=0
            ),
        ]

        gilded_rose = GildedRose(items_input)
        gilded_rose.update_quality()
        self._assert_item_lists_equality(gilded_rose.inventory, items_expected)

    def test_legendary_item(self):
        items_input = [
            Item(name="Sulfuras, Hand of Ragnaros", sell_in=10, quality=80),
            Item(name="Sulfuras, Hand of Ragnaros", sell_in=-10, quality=80),
        ]

        items_expected = [
            Item(name="Sulfuras, Hand of Ragnaros", sell_in=10, quality=80),
            Item(name="Sulfuras, Hand of Ragnaros", sell_in=-10, quality=80),
        ]

        gilded_rose = GildedRose(items_input)
        gilded_rose.update_quality()
        self._assert_item_lists_equality(gilded_rose.inventory, items_expected)

    def _assert_item_lists_equality(self, list1, list2):
        [
            self._assert_items_equality(item, list2[ind])
            for ind, item in enumerate(list1)
        ]

    def _assert_items_equality(self, item1, item2):
        try:
            self.assertEqual(item1.name, item2.name)
            self.assertEqual(item1.sell_in, item2.sell_in)
            self.assertEqual(item1.quality, item2.quality)
        except AssertionError:
            raise AssertionError("{} does not equal {}".format(item1, item2))


if __name__ == "__main__":
    unittest.main()
