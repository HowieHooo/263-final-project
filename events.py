from lxml import html
import mechanize
import pprint

all_events = []
br = mechanize.Browser()

base_url = 'https://events.ucsc.edu'
page_url = 'https://events.ucsc.edu/all'

while (page_url):
	response=br.open(page_url)

	page = html.document_fromstring(response.read())

	event_list = page.xpath('//*[@id="block-system-main"]/div/div/div[1]/div/ul/*')
	for i in range(len(event_list)):
	 	event_element = {}
	 	title_xpath = '//*[@id="block-system-main"]/div/div/div[1]/div/ul/li['+str(i+1)+']/div/div[1]/div[1]/div/div/h3/a'
	 	date_xpath = '//*[@id="block-system-main"]/div/div/div[1]/div/ul/li['+str(i+1)+']/div/div[1]/div[2]/div/div/strong'   
		content_xpath = '//*[@id="block-system-main"]/div/div/div[1]/div/ul/li['+str(i+1)+']/div/div[1]/div[3]/div/div/p'   
		image_xpath = '//*[@id="block-system-main"]/div/div/div[1]/div/ul/li['+str(i+1)+']/div/div[2]/div/div/div/a/img/@src'


		event_title = page.xpath(title_xpath)[0].text_content()
		event_date = page.xpath(date_xpath)[0].text_content()
		if page.xpath(content_xpath):
			event_content = page.xpath(content_xpath)[0].text_content()
		else:
			event_content = 'null'

		try:
			event_image = page.xpath(image_xpath)[0]
		except:
			event_image = 'null'
		
		event_element['title'] = event_title
		event_element['date'] = event_date
		event_element['content'] = event_content
		event_element['image'] = event_image
		all_events.append(event_element)

	if page.xpath('//*[@id="block-system-main"]/div/div/div[2]/ul/li[5]/a/@href'):
		page_url =base_url+page.xpath('//*[@id="block-system-main"]/div/div/div[2]/ul/li[5]/a/@href')[0]
	else:
		page_url = ''

pprint.pprint(all_events)





