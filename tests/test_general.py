from gilded_rose import GildedRose, Item

def test_general():
    items = [Item("foo", 0, 0)]
    gilded_rose = GildedRose(items)
    gilded_rose.update_quality()
    assert items[0].name == "foo"
    
def test_item_sell_in_decreases():
    items = [Item("foo", 10, 10)]
    gilded_rose = GildedRose(items)
    gilded_rose.update_quality()
    assert items[0].sell_in == 9
    
def test_item_quality_decreases():
    items = [Item("foo", 10, 10)]
    gilded_rose = GildedRose(items)
    gilded_rose.update_quality()
    assert items[0].quality == 9
    
    