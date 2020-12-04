# -*- coding: utf-8 -*-
from items import NonLegendaryItem, ConjuredItem, CheeseItem, BackstageItem, LegendaryItem


SUBCLASS_MAPPING = {
    "Aged Brie": CheeseItem,
    "Backstage passes to a TAFKAL80ETC concert": BackstageItem,
    "Sulfuras, Hand of Ragnaros": LegendaryItem,
    "Conjured Mana Cake": ConjuredItem,
}


class GildedRose(object):
    def __init__(self, items):
        self.inventory = [self._get_item_category(i) for i in items]

    def __repr__(self):
        return "\n".join(str(i) + " " + str(type(i)) for i in self.inventory)

    def _get_item_category(self, item):
        # Take the right subclass of every item
        subclass = SUBCLASS_MAPPING.get(item.name, NonLegendaryItem)
        return subclass(item.name, item.sell_in, item.quality)

    def update_quality(self):
        for item in self.inventory:
            item.update()