# -*- coding: utf-8 -*-
class Item:
    def __init__(self, name, sell_in, quality):
        self.name = name
        self.sell_in = sell_in
        self.quality = quality

    def __repr__(self):
        return "%s, %s, %s" % (self.name, self.sell_in, self.quality)


class NonLegendaryItem(Item):
    def __init__(
        self,
        name,
        sell_in,
        quality,
        min_quality=0,
        max_quality=50,
        delta_fresh=-1,
        rot_factor=2,
    ):
        super().__init__(name, sell_in, quality)
        self.min_quality = min_quality
        self.max_quality = max_quality
        self.delta_fresh = delta_fresh
        self.rot_factor = rot_factor

    def update(self):
        # The delta is multiplied by the "rot_factor" when the sell_in moment has expired
        delta = self.delta_fresh if self.sell_in > 0 else self.delta_fresh * self.rot_factor
        quality = self.quality + delta
        self.quality = _confine(quality, self.min_quality, self.max_quality)
        self.sell_in = self.sell_in - 1


class ConjuredItem(NonLegendaryItem):
    def __init__(self, name, sell_in, quality):
        super().__init__(name, sell_in, quality, delta_fresh=-2)


class CheeseItem(NonLegendaryItem):
    def __init__(self, name, sell_in, quality):
        super().__init__(name, sell_in, quality, delta_fresh=+1)


class BackstageItem(NonLegendaryItem):
    def __init__(self, name, sell_in, quality):
        super().__init__(name, sell_in, quality)

    def update(self):
        # If, after updating, the concert will be in the past
        if self.sell_in - 1 < 0:
            self.quality = 0
        else:
            # Tickets get more valuable the closer to the concert date
            delta = 1 if self.sell_in > 10 else 2 if self.sell_in > 5 else 3
            quality = self.quality + delta
            self.quality = _confine(quality, self.min_quality, self.max_quality)
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