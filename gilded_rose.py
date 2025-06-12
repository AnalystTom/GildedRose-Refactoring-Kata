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

def decrease_sell_in(item: Item, amount: int = 1) -> None:
    item.sell_in = item.sell_in - amount
    
def increase_sell_in(item: Item, amount: int = 1) -> None:
    item.sell_in = item.sell_in + amount

def update_backstage(item: Item) -> None:
    increase_item_quality(item)
    if item.sell_in < 10:
        increase_item_quality(item)
    if item.sell_in < 5:
        increase_item_quality(item)

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
            decrease_sell_in(item)
        
        if item.name == SULFURUS:
            pass
        elif item.name == AGED_BRIE:
            if item.sell_in < 0:
                increase_item_quality(item)
            else:
                increase_item_quality(item)
        elif item.name == BACKSTAGE:
            if item.sell_in < 0:
                item.quality = 0
            else:
                update_backstage(item)
        else:
            decrease_item_quality(item)
            if item.sell_in < 0:
                decrease_item_quality(item)
            
        
        
            

