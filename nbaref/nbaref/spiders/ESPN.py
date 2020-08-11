import scrapy
from scrapy.selector import Selector
import csv

year = 0
header =[]
dictionary =[]




class QuotesSpider(scrapy.Spider):
    name = "advanced"
    allowed_domains = ['basketball-reference.com']
    start_urls = ['https://www.basketball-reference.com/leagues/NBA_2020_advanced.html']


    def parse(self, response):
        cols = response.xpath("//div[@id='div_advanced_stats']/table//thead//tr//th")
        header.append('year')
        for col in cols[1:]:
            item= col.css('::attr(data-stat)').extract_first()
            header.append(item)
        global year
        url = ("https://www.basketball-reference.com/leagues/NBA_")
        end = ("_advanced.html")
        year =2020
        search = url + str(year) + end
        yield scrapy.Request(search, callback=self.parse_detail)
        print("hello")

    def parse_detail(self,response):
        global year
        print (response)
        rows = response.xpath("//div[@id='div_advanced_stats']/table//tbody//tr")
        info= rows.css('::text').extract_first()
        for row in rows:
            table = {}
            item= row.css('td')
            table['year']=year
            for data in item:
                column= data.css('::attr(data-stat)').extract_first()
                info= data.css('::text').extract_first()
                if info == "Bertāns,Dāvis":
                    break
               
                table[column] = info
            dictionary.append(table.copy())
        csv_file = (str(year)+"ref.csv")
        try:
            with open(csv_file, 'w', encoding="utf-8") as csvfile:
                writer = csv.DictWriter(csvfile, fieldnames=header)
                writer.writeheader()
                for data in dictionary:
                    writer.writerow(data)
        except IOError:
            print("I/O error")