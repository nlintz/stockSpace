# An object to store stock ticker names from the NYSE
from scrapy.item import Item, Field

class nyseItem(Item):
  ticker = Field()
