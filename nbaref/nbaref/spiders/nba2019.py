import scrapy
from scrapy.selector import Selector
import csv



class QuotesSpider(scrapy.Spider):
    name = "nba"
    allowed_domains = ['basketball-reference.com/']
    start_urls = ['https://www.basketball-reference.com/leagues/NBA_2020_per_game.html']


    def parse(self, response):
        #table = response.css("id.per_game_stats")
        #print(table)
        #table = response.css('document.querySelector.per_game_stats')
        #print(table)
        #table = Selector(text = '<table id =document.querySelector("#per_game_stats")')
        #print(table)
        #for col in response.xpath("//div[@id='div_per_game_stats']/table//tr"):
        #    print (col)
        #table = response.xpath("//div[@id='div_per_game_stats']/table//thead//tr//th")
        dictionary = []
        #table = {}
        header = []
        #colu = response.xpath("//div[@id='div_per_game_stats']/table//tbody//tr")
        #dta = colu.css('td')
        #for value in dta:
        #    vale= value.css('::attr(data-stat)').extract_first()
        #    print (vale)


        cols = response.xpath("//div[@id='div_per_game_stats']/table//thead//tr//th")
        for col in cols[1:]:
            item= col.css('::attr(data-stat)').extract_first()
            header.append(item)
            
        rows = response.xpath("//div[@id='div_per_game_stats']/table//tbody//tr")
        for row in rows:
            table = {}
            item= row.css('td')
            clas = row.css('::attr(class)').extract_first()
            #print (clas)
            for data in item:
                column= data.css('::attr(data-stat)').extract_first()
                info= data.css('::text').extract_first()
                if info == "Bertāns,Dāvis":
                    break
                #table[i] = {column : info}
                #if clas != "thead":
                table[column] = info
                #print (column, ": ", info)
            dictionary.append(table.copy())
           
        #yield table
        csv_file = "NBA2019.csv"
        try:
            with open(csv_file, 'w', encoding="utf-8") as csvfile:
                writer = csv.DictWriter(csvfile, fieldnames=header)
                writer.writeheader()
                for data in dictionary:
                    writer.writerow(data)
        except IOError:
            print("I/O error")


        #for row in table:
        #    get = row.xpath("//div[@id='div_per_game_stats']/table//thead//tr//th//text()").extract_first()
        #    print (get)