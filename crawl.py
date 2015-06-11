import searchengine
pagelist=[
	 'https://www.guokr.com'
	,'http://www.zhihu.com'
	,'http://www.douban.com'
	,'https://zh.wikipedia.org'
]

crawler=searchengine.crawler('searchindex.db')
crawler.crawl(pagelist)
