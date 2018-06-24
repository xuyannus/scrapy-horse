import scrapy


class HorseScrapy(scrapy.Spider):
    name = "horse"

    def start_requests(self):
        urls = [
            "http://www.hkjc.com/english/racing/horse.asp?HorseNo=B249&Option=1#htop"
        ]

        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):

        for row in response.xpath("//table//table[@class='bigborder']//tr[@bgcolor]"):

            record = {
                'Race_Index': self.remove_special_chars(row.xpath('td[1]//text()').extract_first()),
                'Pla': self.remove_special_chars(row.xpath('td[2]//text()').extract_first()),
                'Date': row.xpath('td[3]//text()').extract_first(),
                'RC_Track_Course': row.xpath('td[4]//text()').extract_first(),
                'Dist': row.xpath('td[5]//text()').extract_first(),
                'G': row.xpath('td[6]//text()').extract_first(),
                'Race_Class': self.remove_special_chars(row.xpath('td[7]//text()').extract_first()),
                'Dr': self.remove_special_chars(row.xpath('td[8]//text()').extract_first()),
                'Rtg': self.remove_special_chars(row.xpath('td[9]//text()').extract_first()),
                'Trainer': self.remove_special_chars(row.xpath('td[10]//text()').extract_first()),
                'Jockey': self.remove_special_chars(row.xpath('td[11]//text()').extract_first()),
                'LBW': row.xpath('td[12]//text()').extract_first(),
                'Win_Odds': row.xpath('td[13]//text()').extract_first(),
                'Act. Wt.': self.remove_special_chars(row.xpath('td[14]//text()').extract_first()),
                'Running_Position': row.xpath('td[15]//text()').extract_first(),
                'Finish_Time': row.xpath('td[16]//text()').extract_first(),
                'Declar_Horse_Wt': self.remove_special_chars(row.xpath('td[17]//text()').extract_first()),
                'Gear': row.xpath('td[18]//text()').extract_first(),
                'Video_Replay': row.xpath('td[19]//text()').extract_first(),
            }

            yield (record)

    def remove_special_chars(self, s):
        return ''.join(e for e in s if e.isalnum())
