import searchengine
pagelist=[
	 'http://www.guokr.com'
	,'http://www.zhihu.com'
	,'http://www.douban.com'
]

crawler=searchengine.crawler('searchindex.db')
crawler.crawl(pagelist)
