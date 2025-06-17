from typing import Iterable, Protocol

from item import Item


def decrease_item_quality(item: Item, amount: int = 1) -> None:
    item.quality = max(item.quality - amount, 0)


def increase_item_quality(item: Item, amount: int = 1, max_quality: int = 50) -> None:
    item.quality = min(item.quality + amount, max_quality)


# Item types
AGED_BRIE = "Aged Brie"
BACKSTAGE_PASSES = "Backstage passes to a TAFKAL80ETC concert"
SULFURAS = "Sulfuras, Hand of Ragnaros"
CONJURED = "Conjured Mana Cake"


class ItemUpdater(Protocol):
    def update_sell_in(self, item: Item) -> None: 
        ...

    def update_quality(self, item: Item) -> None: 
        ...

# Base item updater
class BaseItemUpdater:
    def update_sell_in(self, item: Item) -> None:
        item.sell_in = item.sell_in - 1

    def update_quality(self, item: Item) -> None:
        decrease_item_quality(item)
        if item.sell_in < 0:
            decrease_item_quality(item)


# Aged Brie item updater
class BrieItemUpdater(BaseItemUpdater):
    def update_quality(self, item: Item) -> None:
        increase_item_quality(item)
        if item.sell_in < 0:
            increase_item_quality(item)

# Backstage passes item updater
class PassItemUpdater(BaseItemUpdater):
    def update_quality(self, item: Item) -> None:
        increase_item_quality(item)
        if item.sell_in < 10:
            increase_item_quality(item)
        if item.sell_in < 5:
            increase_item_quality(item)
        if item.sell_in < 0:
            item.quality = 0

# Sulfuras item updater
class SulfurasItemUpdater(BaseItemUpdater):
    def update_sell_in(self, item: Item) -> None:
        pass

    def update_quality(self, item: Item) -> None:
        pass

# Conjured item updater
class ConjuredItemUpdater(BaseItemUpdater):
    def update_quality(self, item: Item) -> None:
        decrease_item_quality(item, 2)
        if item.sell_in < 0:
            decrease_item_quality(item, 2)

# Dictionary of item types and their updaters
ITEM_UPDATERS_DICT = {
    AGED_BRIE: BrieItemUpdater(),
    BACKSTAGE_PASSES: PassItemUpdater(),
    SULFURAS: SulfurasItemUpdater(),
    CONJURED: ConjuredItemUpdater(),
}

# Keeping these as before, goes through each item and updates the quality
def update_quality(items: Iterable[Item]) -> None:
    for item in items:
        update_quality_single(item)

# We retrieve the necessary updater for the item
def update_quality_single(item: Item):
    item_updater = ITEM_UPDATERS_DICT.get(item.name, BaseItemUpdater())

    # update the sell in value
    item_updater.update_sell_in(item)

    # update the quality
    item_updater.update_quality(item)