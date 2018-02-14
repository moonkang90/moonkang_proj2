



from scrapy import Spider, Request
from realestate.items import RealestateItem


class RealestateSpider(Spider):

	name = "realestate_spider"
	allowed_urls = ["https://www.niche.com/places-to-live/search/best-cities-to-buy-a-house/?page=1"]
	#start_urls = ["https://www.niche.com/places-to-live/search/best-cities-to-buy-a-house/?page=1"]
	start_urls= ["https://www.niche.com/places-to-live/search/best-cities-to-buy-a-house/?page=" + str(x) for x in range(1,11)]




	def parse(self, response):
		
		#links = ["https://www.niche.com/places-to-live/search/best-cities-to-buy-a-house/?page=" + str(x) for x in range(1,11)]

		spans = response.xpath('//a[@class="search-result__link"]/@href').extract()
		# links = ["https://www.niche.com/places-to-live/search/best-cities-to-buy-a-house/" + link for link in spans]
		
		# reviews = response.xpath('//ol[@class="search-results__list"]')

		# for review in reviews:
			# content = response.xpath()


		# State = response.xpath('//ul[@class="search-result-tagline"]/li/text()').extract()
			# url = response.xpath('//a[@class="search-result__link"]/@href').extract()
			# print("hello")
			# City = response.xpath('//div[@class="card__inner"]/h2/text()').extract()
			# Numberof_reviews = response.xpath('//div[@class="review__stars review__stars--gray"]/span/text()').extract()
			# Review_ratings = response.xpath('//li[@class="search-result-tagline__item"]//div/span/@class').extract()
			# Population = response.xpath('//div[@class="search-result-fact"]/span/text()').extract()



		for url in spans:
			yield Request(url, callback=self.parse_detail)

	# def parse_top(self, response):


#		for url in links:
#			yield Request(url, callback=self.parse_detail, meta={'top_list': top_list})

#	def parse_detail(self, response):

		# for url in links:
		# 	yield Request(url, callback=self.parse_detail, meta={'top_list': top_list})

	def parse_detail(self, response):
		# State = response.meta['State']
		# City = response.meta['City']
		# Numberof_reviews = response.meta['Numberof_reviews']
		# Review_ratings = response.meta['Review_ratings']
		# Population = response.meta['Population']
		State = response.xpath('//div[@class="profile__bucket--3"]//span/text()').extract()[0]
		City = response.xpath('//div[@class="blank__bucket"]//a/text()').extract()[0]
		Numberof_reviews = response.xpath('//div[@class="review__stars review__stars--white"]//span/text()').extract()
		Review_ratings = response.xpath('//div[@class="review__stars review__stars--white"]//span/@class').extract()
		Population = response.xpath('//div[@class="scalar__value"]//span/text()').extract()[0]

		Median_Home_Value = response.xpath('//div[@class="scalar__value"]/span/text()').extract()[1]
		Median_Rent = response.xpath('//div[@class="scalar__value"]/span/text()').extract()[2]
		Area_Feel = response.xpath('//div[@class="scalar__value"]/span/text()').extract()[3]
		Crime_Safty = response.xpath('//ol[@class="ordered__list__bucket"]//div/text()').extract()[3]
		Diversity = response.xpath('//ol[@class="ordered__list__bucket"]//div/text()').extract()[11]
		PublicSchool_level = response.xpath('//ol[@class="ordered__list__bucket"]//div/text()').extract()[1]
		Children_percent = response.xpath('//div[@class="scalar__value"]/span/text()').extract()[5]
		Master_Degree = response.xpath('//ul[@class="breakdown-facts breakdown-facts--national"]//div/text()').extract()[1]
		Bachelor_Degree = response.xpath('//ul[@class="breakdown-facts breakdown-facts--national"]//div/text()').extract()[4]
		Associate_Degree = response.xpath('//ul[@class="breakdown-facts breakdown-facts--national"]//div/text()').extract()[7]
		Jobs_Level = response.xpath('//ol[@class="ordered__list__bucket"]//div/text()').extract()[13]
		Median_salary = response.xpath('//div[@class="scalar__value"]/span/text()').extract()[4]
		Cost_of_Living = response.xpath('//ol[@class="ordered__list__bucket"]//div/text()').extract()[17]
		Weather = response.xpath('//ol[@class="ordered__list__bucket"]//div/text()').extract()[15]
		NightLife = response.xpath('//ol[@class="ordered__list__bucket"]//div/text()').extract()[7]
		Outdoor_Activity = response.xpath('//ol[@class="ordered__list__bucket"]//div/text()').extract()[21]
		




		
		item = RealestateItem()

		item['State'] = State
		item['City'] = City
		item['Median_Home_Value'] = Median_Home_Value
		item['Median_Rent'] = Median_Rent
		item['Population'] = Population
		item['Area_Feel'] = Area_Feel
		item['Crime_Safty'] = Crime_Safty
		item['Diversity'] = Diversity
		item['PublicSchool_level'] = PublicSchool_level
		item['Children_percent'] = Children_percent
		item['Master_Degree'] = Master_Degree
		item['Bachelor_Degree'] = Bachelor_Degree
		item['Associate_Degree'] = Associate_Degree
		item['Jobs_Level'] = Jobs_Level
		item['Median_salary'] = Median_salary
		item['Cost_of_Living'] = Cost_of_Living
		item['Weather'] = Weather
		item['NightLife'] = NightLife
		item['Outdoor_Activity'] = Outdoor_Activity
		item['Numberof_reviews'] = Numberof_reviews
		item['Review_ratings'] = Review_ratings

		yield item
