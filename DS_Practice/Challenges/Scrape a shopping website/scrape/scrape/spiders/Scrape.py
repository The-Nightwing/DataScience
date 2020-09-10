import scrapy
import pandas as pd

book_urls = []
book_titles = []
product_prices = []

class QuotesSpider(scrapy.Spider):
    name = "quotes"

    def start_requests(self):
        urls = [
            "http://books.toscrape.com/"
        ]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        for q in response.css("article.product_pod"):
            book_url = q.css("img.thumbnail::attr(src)").get()
            book_title = q.css('h3 a::attr(title)').get()
            product_price = q.css('p.price_color::text').get()

            book_urls.append(book_url)
            book_titles.append(book_title)
            product_prices.append(product_price)

        next_page = response.css('li.next a::attr(href)').get()  # next button se /page2/ aisa mila jayega
        if next_page is not None:
            next_page = response.urljoin(next_page)  # creates new url for next page
            yield scrapy.Request(next_page, callback=self.parse)

        dt = {'book_url': book_urls, 'book_title': book_titles, 'product_prices': product_prices}
        df=pd.DataFrame(dt)
        df.to_csv("sub.csv", index=False)
 
        yield dt
