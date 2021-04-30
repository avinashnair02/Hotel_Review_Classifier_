# -*- coding: utf-8 -*-
import scrapy
from.. items import NlpItem

class HotelsSpider(scrapy.Spider):
    name = 'hotels'
    allowed_domains = ['www.tripadvisor.in']
    start_urls = [
        'https://www.tripadvisor.co.uk/Hotel_Review-g187051-d239658-Reviews-Hotel_Hilton_London_Gatwick_Airport-Crawley_West_Sussex_England.html/',
                  'https://www.tripadvisor.co.uk/Hotel_Review-g186338-d193089-Reviews-Hilton_London_Metropole-London_England.html/',
                  'https://www.tripadvisor.co.uk/Hotel_Review-g186338-d192048-Reviews-Hilton_London_Euston-London_England.html/',
                  'https://www.tripadvisor.co.uk/Hotel_Review-g186338-d193102-Reviews-DoubleTree_by_Hilton_Hotel_London_West_End-London_England.html/',
                  'https://www.tripadvisor.co.uk/Hotel_Review-g504167-d192599-Reviews-Hilton_London_Croydon-Croydon_Greater_London_England.html']

    def parse(self, response):
        items = NlpItem()
        for review in response.xpath(
                '//*[contains(concat( " ", @class, " " ), concat( " ", "_3hFEdNs8", " " ))]'):
            #print ('PRinting')
            print (review)
            yield {
                'hotel_name': review.xpath(
                    '//*[(@id = "HEADING")]/text()').get(),
                'review_summary': review.xpath(
                    '//*[contains(concat( " ", @class, " " ), concat( " ", "glasR4aX", " " ))]/a/span/span/text()').get(),
                'review_p1': review.xpath(
                    '//*[contains(concat( " ", @class, " " ), concat( " ", "_3hDPbqWO", " " ))]/div/div/q/span[1]/text()').get(),
                'review_p2': review.xpath(
                    '//*[contains(concat( " ", @class, " " ), concat( " ", "_3hDPbqWO", " " ))]/div/div/q/span[2]/text()').get(),
                'score': review.xpath(
                    '//*[contains(concat( " ", @class, " " ), concat( " ", "nf9vGX55", " " ))]/span').get()

            }

        href = response.xpath('//a[@class="ui_button nav next primary "]/@href').get()

        next_page_url = 'https://www.tripadvisor.in/' + href


        yield scrapy.Request(url=next_page_url, callback=self.parse)