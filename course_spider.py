import scrapy 

class CourseSpider(scrapy.Spider):
  name = "courseInfo"
  start_urls = ['https://www.nursingce.com/ceu-courses']

  def parse(self,response):
    for card in response.css('div.card-body'):
      yield{
        'title': card.css('h4::text').get(),
        'cost' : card.css('p.text-success.fw-900::text').get(),
        'description' : card.css('p::text')[0].get(),
        'contact hours' : card.css('p.hours::text')[0].get()
      }


# For contact hours: response.css('div.card-body p.hours::text').get()

#for title of text: response.css('div.card-body h4::text').get()

# for cost: response.css('div.card-body p.text-success.fw-900::text').get()

# for description: response.css('div.card-body p::text').get()

