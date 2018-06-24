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
                'Race_Index': int(self.remove_special_chars(row.xpath('td[1]//text()').extract_first())),
                'Pla': self.remove_special_chars(row.xpath('td[2]//text()').extract_first()),
                'Date': row.xpath('td[3]//text()').extract_first(),
                # 'RC_Track_Course': row.xpath('td[4]//text()').extract_first(),
                'RC_Track_Course': ''.join(row.xpath('td[4]//text()').extract()).replace(' ',''),
                'Dist': row.xpath('td[5]//text()').extract_first(),
                'G': row.xpath('td[6]//text()').extract_first().strip(),
                'Race_Class': self.remove_special_chars(''.join(row.xpath('td[7]//text()').extract())),
                'Dr': self.remove_special_chars(row.xpath('td[8]//text()').extract()),
                'Rtg': self.remove_special_chars(row.xpath('td[9]//text()').extract_first()),
                'Trainer': row.xpath('td[10]//a//text()').extract_first().strip(),
                'Jockey': row.xpath('td[11]//a//text()').extract_first().strip(),
                'LBW': row.xpath('td[12]//text()').extract_first().strip(),
                'Win_Odds': row.xpath('td[13]//text()').extract_first(),
                'Act. Wt.': self.remove_special_chars(row.xpath('td[14]//text()').extract_first()),
                'Running_Position': self.remove_special_chars(row.xpath('td[15]//text()').extract()),
                'Finish_Time': row.xpath('td[16]//text()').extract_first(),
                'Declar_Horse_Wt': self.remove_special_chars(row.xpath('td[17]//text()').extract_first()),
                'Gear': row.xpath('td[18]//text()').extract_first(),
            }

            yield (record)

    def remove_special_chars(self, s):
        if isinstance(s, list):
            result_list = []
            for item in s:
                item = ''.join(e for e in item if e.isalnum()).strip()
                result_list.append(item) if item else None

            return result_list

        return ''.join(e for e in s if e.isalnum()).strip()



# tt = ['\r\n\t', '1', '\xa0\xa01', '\xa0\xa02', '\t\r\n\t\r\n\t']
# print(HorseScrapy.remove_special_chars(tt))