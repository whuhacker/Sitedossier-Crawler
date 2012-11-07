Sitedossier-Crawler
===================

A web crawler for sitedossier.com

* Start from the url and crawl the web pages with a specified depth.  
* Save the pages which contain a keyword(if provided) into database.  
* Support multi-threading.  
* Support logging.  
* Support self-testing.  



System Requirement
-------------
```shell
$ yum install python
$ yum install python-argparse
$ yum install python-BeautifulSoup
```

Usage
-------------
```shell
$ python crawler_ns.py -ns dns.baidu.com
# To save the result to a text file:
$ python crawler_ns.py -ns dns.baidu.com >> result.txt
```