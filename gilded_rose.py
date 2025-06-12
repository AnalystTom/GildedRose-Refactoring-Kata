# -*- coding: utf-8 -*-

QualityCap = 50

## NAMES
AGED_BRIE = "Aged Brie"
SULFURUS = "Sulfuras, Hand of Ragnaros"
BACKSTAGE = "Backstage passes to a TAFKAL80ETC concert"


class GildedRose(object):

    def __init__(self, items):
        self.items = items

    def update_quality(self):
        for item in self.items:
            if item.name != AGED_BRIE and item.name != BACKSTAGE:
                if item.quality > 0:
                    if item.name != SULFURUS:
                        item.quality = item.quality - 1
            else:
                if item.quality < QualityCap:
                    item.quality = item.quality + 1
                    if item.name == BACKSTAGE:
                        if item.sell_in < 11:
                            if item.quality < QualityCap:
                                item.quality = item.quality + 1
                        if item.sell_in < 6:
                            if item.quality < QualityCap:
                                item.quality = item.quality + 1
            if item.name != SULFURUS:
                item.sell_in = item.sell_in - 1
            if item.sell_in < 0:
                if item.name != AGED_BRIE:
                    if item.name != BACKSTAGE:
                        if item.quality > 0:
                            if item.name != SULFURUS:
                                item.quality = item.quality - 1
                    else:
                        item.quality = item.quality - item.quality
                else:
                    if item.quality < QualityCap:
                        item.quality = item.quality + 1


class Item:
    def __init__(self, name, sell_in, quality):
        self.name = name
        self.sell_in = sell_in
        self.quality = quality

    def __repr__(self):
        return "%s, %s, %s" % (self.name, self.sell_in, self.quality)
