# -*- coding: utf-8 -*-

from item import Item

max_quality = 50

## NAMES
AGED_BRIE = "Aged Brie"
SULFURUS = "Sulfuras, Hand of Ragnaros"
BACKSTAGE = "Backstage passes to a TAFKAL80ETC concert"

def decrease_item_quality(item: Item, amount: int = 1) -> None:
    item.quality = max(0, item.quality - amount)

def increase_item_quality(item: Item, amount: int = 1) -> None:
    item.quality = min(max_quality, item.quality + amount)



class GildedRose(object):

    def __init__(self, items):
        self.items = items

    def update_quality(self):
        for item in self.items:
            self.update_quality_single(item)

    def update_quality_single(self, item):
        if item.name == SULFURUS:
            pass
        else: 
            item.sell_in = item.sell_in - 1
        
        if item.name != AGED_BRIE and item.name != BACKSTAGE:
            if item.name != SULFURUS:
                decrease_item_quality(item)
        else:
            increase_item_quality(item)
            if item.name == BACKSTAGE:
                if item.sell_in < 10:
                    increase_item_quality(item)
                if item.sell_in < 5:
                    increase_item_quality(item)
                    
                    
                    
        if item.sell_in < 0:
            if item.name == AGED_BRIE:
                increase_item_quality(item)
            else:
                if item.name == BACKSTAGE:
                    item.quality = 0
                else:
                    if item.name == SULFURUS:
                        pass
                    else:
                        decrease_item_quality(item)          
                

