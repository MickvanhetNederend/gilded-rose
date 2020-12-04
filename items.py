# -*- coding: utf-8 -*-
class Item:
    def __init__(self, name, sell_in, quality):
        self.name = name
        self.sell_in = sell_in
        self.quality = quality

    def __repr__(self):
        return "%s, %s, %s" % (self.name, self.sell_in, self.quality)


class GeneralItem(Item):
    def __init__(self, name, sell_in, quality):
        super().__init__(name, sell_in, quality)
        self.min_quality = 0
        self.max_quality = 50

    def update(self):
        decrement = 1 if self.sell_in > 0 else 2
        self.quality = _confine(
            self.quality - decrement, self.min_quality, self.max_quality
        )
        self.sell_in = self.sell_in - 1


class CheeseItem(Item):
    def __init__(self, name, sell_in, quality):
        super().__init__(name, sell_in, quality)
        self.min_quality = 0
        self.max_quality = 50

    def update(self):
        increment = 1 if self.sell_in > 0 else 2
        self.quality = _confine(
            self.quality + increment, self.min_quality, self.max_quality
        )
        self.sell_in = self.sell_in - 1


class BackstageItem(Item):
    def __init__(self, name, sell_in, quality):
        super().__init__(name, sell_in, quality)
        self.min_quality = 0
        self.max_quality = 50

    def update(self):
        # If, after updating, the concert will be in the past
        if self.sell_in - 1 < 0:
            self.quality = 0
        else:
            # Tickets get more valuable the closer to the concert date
            increment = 1 if self.sell_in > 10 else 2 if self.sell_in > 5 else 3
            self.quality = _confine(
                self.quality + increment, self.min_quality, self.max_quality
            )
        self.sell_in = self.sell_in - 1


class LegendaryItem(Item):
    def __init__(self, name, sell_in, quality):
        super().__init__(name, sell_in, quality)

    def update(self):
        pass


def _confine(value, lower_bound, upper_bound):
    # takes lower bound if value is too low,
    # takes upper bound if value is too high
    return min(max(value, lower_bound), upper_bound)