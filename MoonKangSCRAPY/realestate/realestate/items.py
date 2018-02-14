# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class RealestateItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()

    State = scrapy.Field()
    City = scrapy.Field()
    Median_Home_Value = scrapy.Field()
    Median_Rent = scrapy.Field()
    Population = scrapy.Field()
    Area_Feel = scrapy.Field()
    Crime_Safty = scrapy.Field()
    Diversity = scrapy.Field()
    PublicSchool_level = scrapy.Field()
    Children_percent = scrapy.Field()
    Master_Degree = scrapy.Field()
    Bachelor_Degree = scrapy.Field()
    Associate_Degree = scrapy.Field()
    Jobs_Level = scrapy.Field()
    Median_salary = scrapy.Field()
    Cost_of_Living = scrapy.Field()
    Weather = scrapy.Field()
    NightLife = scrapy.Field()
    Outdoor_Activity = scrapy.Field()
    Numberof_reviews = scrapy.Field()
    Review_ratings = scrapy.Field()





    pass
