from gilded_rose import GildedRose, Item

BACKSTAGE = "Backstage passes to a TAFKAL80ETC concert"

def test_backstage_quality_increases():
    items = [Item(BACKSTAGE, 11, 0)]
    gilded_rose = GildedRose(items)
    gilded_rose.update_quality()
    assert items[0].quality == 1
    
    
def test_backstage_quality_increases_by_2_when_sell_in_is_less_than_10():
    items = [Item(BACKSTAGE, 9, 10)]
    gilded_rose = GildedRose(items)
    gilded_rose.update_quality()
    assert items[0].quality == 12
    
    
def test_backstage_quality_increases_by_3_when_sell_in_is_less_than_5():
    items = [Item(BACKSTAGE, 4, 10)]
    gilded_rose = GildedRose(items)
    gilded_rose.update_quality()
    assert items[0].quality == 13
    
    
def test_backstage_quality_drops_to_0_after_concert():
    items = [Item(BACKSTAGE, 0, 10)]
    gilded_rose = GildedRose(items)
    gilded_rose.update_quality()
    assert items[0].quality == 0
    