import scrapy


class DoctoraliaSpider(scrapy.Spider):
    name = 'doctoralia'
    allowed_domains = ['doctoralia.com']
    start_urls = [
        'https://www.doctoralia.com.br/pesquisa?q=Ginecologista&loc=&filters%5Bspecializations%5D%5B0%5D=36&page=1'
    ]

    def parse(self, response):
        cards = response.xpath('//div[contains(@class, "card-body")]')
        names = response.xpath('//span[@data-ga-label="Doctor Name"]/text()').extract()
        profile_links = response.xpath(
            '//div[contains(@class, "media-body")]//a[@data-id="address-context-cta"]/@href').extract()

        for (name, link) in zip(names, profile_links):
            address = response.xpath(
                f'//span[@data-ga-label="Doctor Name" and contains(text(), "{name}")]//ancestor::div[contains(@class, "dp-doctor-card")]/parent::div//div[not(contains(@class, "hide"))]/div[@data-id="result-address-item"]//span[@class="text-truncate"]/text()').extract_first()

            yield {
                "name": self.strip_text(name),
                "address": self.strip_text(address),
                "profile_url": self.strip_text(link),
            }

    @staticmethod
    def strip_text(text):
        if isinstance(text, str):
            text = text.strip()
        return text
