#! /usr/bin/env python

import sys
import searchengine

if __name__ == '__main__':
	if len(sys.argv) < 2:
		sys.exit(0)

	c=searchengine.crawler('searchindex.db')
	q=c.separatewords(sys.argv[1])
	e=searchengine.searcher('searchindex.db')
	e.query(" ".join(q))

