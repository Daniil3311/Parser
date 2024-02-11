import scrapy


class ParserMoviesSpider(scrapy.Spider):
    name = "Parser_movies"
    allowed_domains = ["www.scrapethissite.com"]
    start_urls = ["https://www.scrapethissite.com/pages/ajax-javascript/"]

    def parse(self, response):
        # hre = response.xpath("//div[@class='col-md-12 text-center']/a/href").extract_first()
        # hre = response.css('.col-md-12 text-center')
        year_movies = response.css('.row')
        print('================')
        print(year_movies)
        print('================')
