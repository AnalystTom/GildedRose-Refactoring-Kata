from gilded_rose import GildedRose, Item

SULFURUS = "Sulfuras, Hand of Ragnaros"

def test_sulfuras_quality_never_changes():
    items = [Item(SULFURUS, 10, 10)]
    gilded_rose = GildedRose(items)
    gilded_rose.update_quality()
    assert items[0].quality == 10
    assert items[0].sell_in == 10