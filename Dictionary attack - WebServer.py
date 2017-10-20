#!/usr/bin/python2.7

import urllib.request,sys

host = sys.argv[1]
file_name = sys.argv[2]

file = open(file_name,"r")
data = file.readlines()

for line in data:
    word = line.strip("\n")
    strReq = "{0}/{1}".format(host,word)
    try:
        req = urllib.request.urlopen(strReq)
        if req.code == 200:
            print("[+] {0}/{1} is Found (200)".format(host,word))
    except:
         print("[-] {0}/{1} is Not Found (404)".format(host,word))
