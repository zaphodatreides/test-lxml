#! /usr/bin/python

import requests
from lxml import etree
from lxml import html
import io

headers={"User-Agent":"Mozilla/5.0 (Linux; Android 8.0.0; SM-G930F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.101 Mobile Safari/537.36"}

response= requests.get ("http://127.0.0.1",headers=headers)
if response.status_code != 200:
 print ("Error getting page")
 exit(1)
print (response.text)
parser=etree.HTMLParser()
tree=etree.parse(io.StringIO(response.text),parser=parser)
elements=tree.xpath("/html/body/text()")
for element in elements:
 print (element)

