# -*- coding: utf-8 -*-
import scrapy
from.. items import NlpItem

class HotelsSpider(scrapy.Spider):
    name = 'hotels'
    allowed_domains = ['www.tripadvisor.in']
    start_urls = [
       '/Hotel_Review-g304556-d2534781-Reviews-ITC_Grand_Chola_Chennai_a_Luxury_Collection_Hotel-Chennai_Madras_Chennai_District_Tami.html',
        '/Hotel_Review-g304556-d301636-Reviews-The_Park_Chennai-Chennai_Madras_Chennai_District_Tamil_Nadu.html',
        '/Hotel_Review-g304556-d730057-Reviews-GreenPark_Chennai-Chennai_Madras_Chennai_District_Tamil_Nadu.html',
        '/Hotel_Review-g304556-d1597314-Reviews-Hilton_Chennai-Chennai_Madras_Chennai_District_Tamil_Nadu.html',
        '/Hotel_Review-g304556-d1872115-Reviews-Hyatt_Regency_Chennai-Chennai_Madras_Chennai_District_Tamil_Nadu.html',
        '/Hotel_Review-g304556-d1164749-Reviews-Taj_Club_House-Chennai_Madras_Chennai_District_Tamil_Nadu.html',
        '/Hotel_Review-g304556-d306744-Reviews-Radisson_Blu_Hotel_GRT_Chennai-Chennai_Madras_Chennai_District_Tamil_Nadu.html',
        '/Hotel_Review-g304556-d1382155-Reviews-Lemon_Tree_Hotel_Chennai-Chennai_Madras_Chennai_District_Tamil_Nadu.html']

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