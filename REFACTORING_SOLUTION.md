# My Approach


## Steps taken

1. Simplified Folder Structure
2. Replaced strings and ints with variables
3. Created Tests for Generic tests, sulfurus, backstage and brie. 
4. Moved Item Class into separate file 
5. Created helper functions (increase and decrease quality value)
6. Flipped some of the != into == for easier interpretability 
7. Converted teh testtext into pytest to test 2 day simulation
8. Created conjured test

Now I have a couple of options available: 
1. I can either use a Factory Design, where each item is a class
2. Or create a item_update class 
I decided to implement the item_update class to keep the Item as a pure data model
* Also we can unit test each updater in isolation
* Makes creating the conjured logic easy

9. I decided to take the update_quality and update_quality_single functions out of the Guilded Rose class and disolve the class. 
10. Instead I have created ItemUpdater Protocol (a protocol specifies the methods and attributes that a class must implement to be considered a given type.)
11. Aso I created the BaseItemUpdate class which has function update_sell_in and update_quality which update the respective values 
12. Then I have created an updater for each item "type" (eg. sulphuras, brie, conjured, etc) which inheartits from the BaseItemUpdater and handles all of the busienss logic separately. (getting rid of the if else statements)
13. I have created the ITEM_UPDATERS_DICT which allows us to update the item passed into quality_update_single according to the Updater function that matches the item.name 
14. All of the tests pass succesfully and the objective of implemeneintg the conjured items is complete 