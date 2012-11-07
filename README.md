Sitedossier-Crawler
===================

A web crawler for sitedossier.com

* Query information about a particular name server


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