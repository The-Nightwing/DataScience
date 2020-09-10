import scrapy


class QuotesSpider(scrapy.Spider):
    name = "quotes"

    def start_requests(self):
        urls = [
            'http://quotes.toscrape.com/page/1/',
            'http://quotes.toscrape.com/page/2/',
        ]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        page = response.url.split("/")[-2]
        #filename = 'quotes-%s.html' % page

        for q in response.css("div.quote"):
            text=q.css("span.text::text").get()
            text=text.replace("\u201c","")
            text=text.replace("\u201d","")
            author= q.css("small.author::text").get()
            tags=q.css("a.tag::text").getall()

            yield{

                'text': text,
                'author': author,
                'tags': tags
            }

        next_page=response.css('li.next a::attr(href)').get() #next button se /page2/ aisa mila jayega
        if next_page is not None:
            next_page=response.urljoin(next_page)   #creates new url for next page
            yield scrapy.Request(next_page,callback=self.parse)


        #with open(filename, 'wb') as f:
            #f.write(response.body)
        #self.log('Saved file %s' % filename)