
import requests, time
from bs4 import BeautifulSoup as BeSo

#url = requests.get('https://metallportal.com/o-kompanii')
#soup = BeSo(url.content, "html.parser")

#ee = soup.find_all("p")[9].text
#ee = soup.find_all(class_ = 'col policy')[0].find_all('p')[4].text

#content_head = soup.find(class_ = 'content-ind').find_parent("div", "container")
#content_content = soup.find("div", class_ = 'content-wrap').find(class_ = 'content-ind').text

#print(ee)



class Parsing_web(object):

    def __init__(self, url):
        self.url = url
        
    def Reference_order(self):
        pass

    def Guide_Suppliers(self):
        pass

    def Reference_references(self):
        pass

    def Reference_resources(self, parametrs_string):

        if self.url == 'https://metallportal.com/': url = self.url + 'o-kompanii'
        elif self.url == 'https://prom-market.com/': url = self.url + 'about/'
        else: url = self.url

        parametrs_list = parametrs_string.split(':')
        request_web = requests.get(url)
        soup = BeSo(request_web.content, "html.parser")

        text = soup.find_all(class_ = parametrs_list[0])[int(parametrs_list[1])].find_all(parametrs_list[2])[int(parametrs_list[3])].text

        return text.replace("\n", '')
        

    def Orders(self):
        pass

    def Reference_files(self):
        pass

    def Proposal(self):
        pass


