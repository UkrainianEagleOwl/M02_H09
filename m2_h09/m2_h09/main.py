

from scrapy.crawler import CrawlerProcess
from spiders.quotes import QuotesSpider
from spiders.authors import AuthorsSpider

if __name__ == '__main__':
    process = CrawlerProcess()

    # Run the QuotesSpider
    process.crawl(QuotesSpider)

    # Run the AuthorsSpider
    process.crawl(AuthorsSpider)

    process.start()