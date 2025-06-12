from gilded_rose import GildedRose, Item

def test_aged_brie_quality_increases():
    items = [Item("Aged Brie", 10, 10)]
    gilded_rose = GildedRose(items)
    gilded_rose.update_quality()
    assert items[0].quality == 11
    
    