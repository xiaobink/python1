import scrapy
from bs4 import BeautifulSoup
from ..items import JobuiItem

class JobuiSpider(scrapy.Spider):
    name='jobs'
    allowed_domains=['www.jobui.com']
    start_urls=['https://www.jobui.com/rank/company/']

    def parse(self,response):
        soup=BeautifulSoup(response.text,'html.parser')
        url_jobs = soup.find('ul', class_='rowList jobList').find_all('ul', class_='textList flsty cfix')

        for i in range(len(url_jobs)):
            url_data = url_jobs[i].find_all('a')

            for urls in url_data:
                url = 'https://www.jobui.com' + urls['href'] + 'jobs/'

                yield scrapy.Request(url,callback=self.parse_job) #用yield语句把requests对象传递个引擎，用scrapy.Request构造request对象，callback参数设置调用parsejob方法

    def parse_job(self,response):
        soup=BeautifulSoup(response.text,'html.parser')
        company=soup.find(id='companyH1').find('a').text
        datas=soup.find(id='companyJobsJobList').find_all(class_="job-simple-content")
        for data in datas:
            item=JobuiItem()
            item['company']=company
            item['job']=data.find('a').text.strip()
            item['address']=data.find(class_='job-desc').find_all('span')[0].text
            item['others']=data.find(class_='job-desc').find_all('span')[1].text
            item['url_detail']='https://www.jobui.com'+data.find('a')['href']

            yield item   #用yield语句把item传递给引擎


