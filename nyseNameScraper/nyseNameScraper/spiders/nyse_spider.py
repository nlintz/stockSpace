from scrapy.spider import BaseSpider
from scrapy.selector import HtmlXPathSelector
from nyseNameScraper.items import nyseItem

class nyseSpider(BaseSpider):
  name = 'nyse'
  allowed_domains = ['eoddata.com']
  start_urls = [
    'http://eoddata.com/stocklist/NYSE/A.htm'
  ]

  def parse(self, response):
    hxs = HtmlXPathSelector(response)
    # TODO fix html selectors
    sites = hxs.select('//ul/li')
    items = []
    for site in sites:
      item = nyseItem()
      # TODO fix the ticker selector
      item['ticker'] = site.select('a/text()').extract()
      items.append(item)
    return items
