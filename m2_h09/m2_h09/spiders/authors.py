import scrapy

class AuthorsSpider(scrapy.Spider):
    name = "authors"
    allowed_domains = ["quotes.toscrape.com"]
    custom_settings = {"FEED_FORMAT": "json", "FEED_URI": "authors.json"}
    start_urls = ["https://quotes.toscrape.com"]
    
    
    def __init__(self, *args, **kwargs):
        super(AuthorsSpider, self).__init__(*args, **kwargs)
        self.processed_authors = set()

    def parse(self, response):
        # Follow links to author pages
        author_links = response.xpath("/html//div[@class='quote']//span/a")
        self.logger.info(f"Links: {author_links}")
        for author_link in author_links:
            author_page_url = author_link.xpath("@href").get()
            yield response.follow(author_page_url, self.parse_author)
            
        next_link = response.xpath("//li[@class='next']/a/@href").get()
        if next_link:
            yield scrapy.Request(url=self.start_urls[0] + next_link)

    def parse_author(self, response):
        author_name = response.xpath("//h3[@class='author-title']/text()").get()
        author_birthdate = response.xpath("//span[@class='author-born-date']/text()").get()
        author_birthplace = response.xpath("//span[@class='author-born-location']/text()").get()
        author_bio = response.xpath("//div[@class='author-description']/text()").get()

        if author_name and author_name not in self.processed_authors:
            self.processed_authors.add(author_name)
            yield {
                "fullname": author_name.strip(),
                "born_date": author_birthdate.strip(),
                "born_location" : author_birthplace.strip(),
                "description": author_bio.strip()
            }
        
    def start_requests(self):
        yield scrapy.Request(url=self.start_urls[0], callback=self.parse)

