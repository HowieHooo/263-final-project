import scrapy
from event_scrapy.items import EventScrapyItem

class EventSpider(scrapy.Spider):
	name = "event"
	allowed_domains = ['events.ucsc.edu']
	start_urls = [
		'https://events.ucsc.edu/all'
	]

	def parse(self, response):
		#get all the h3 titles from the web
		items = []
		for event in response.css('div.ds-2col node node-event node-teaser view-mode-teaser event-list clearfix'):
			item = EventScrapyItem()
			item['title'] = event.css('div.group-left a::text').extract()
			item['time'] = event.css('div.field-item even strong::text').extract()
			item['describtion'] = event.css('div.field-item even p::text').extract()
			items.append(item)

		return items


