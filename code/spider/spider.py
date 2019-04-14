from urllib import request

# 断点调试
class Spider():
    url = 'https://www.panda.tv/cate/lol'
    
    def __fetch_content():
       r =  request.urlopen(Spider.url)
       # bytes
       htmls = r.read()
       str(htmls, encoding = 'utf-8')
       a = 1
       
    def __analysis(self):
        pass
    
    def go(self):
        htmls = self.__fetch_content()
        self.__analysis(htmls)
        
spider = Spider()
spider.go()