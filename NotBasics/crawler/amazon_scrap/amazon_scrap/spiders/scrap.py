# -*- coding: utf-8 -*-
import scrapy
from ..items import AmazonScrapItem


class ScrapSpider(scrapy.Spider):
    name = 'scrap'
    allowed_domains = ['https://www.amazon.in/s?k=laptop']
    start_urls = ['http://https://www.amazon.in/s?k=laptop/']

    def parse(self, response):
        items = AmazonScrapItem()
        product_name = response.css('.a-color-base.a-text-normal::text').extract()
        product_price = response.css('.a-price:nth-child(1) .a-price-whole').css('::text').extract()
        product_image_link = response.css('.a-spacing-none .s-image::attr(src)').extract()

        items['product_name'] = product_name
        items['product_price'] = product_name
        items['product_image_link'] = product_image_link
        
        yield items
