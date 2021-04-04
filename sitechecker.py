#!/usr/bin/python
# -*- coding: utf-8 -*-

#import modules
import re
from urlextract import URLExtract
import requests
import cloudscraper

#initialize modules
s = cloudscraper.create_scraper()
extractor=URLExtract()

#banner
print("-"*50)
print("|         Website Checking tool by Samit          |")
print("-"*50)
print("*"*50)

#open a text file
path=input("Enter the path to file containing URLs :")
st = open(path,'r').read()
print("*"*50)
print("[+] FILE OPENED ")
print("*"*50)
#extract all urls
print("[+] URLs Found:")
u=extractor.find_urls(st)
for urls in u:
    print("[->]" +urls)
print("*"*50)
check=-1
for i in u:
    str="https://securityscan.getastra.com/malware-scanner?site="+i
    x=s.get(str)
    check=x.text.find("pill severity high")
    if(check==-1):
        print("[+] "+i+"     [Safe]")
    else:
        print("[-] "+i+"     [Unsafe]")
print("*"*50)
