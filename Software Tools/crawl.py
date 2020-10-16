'''
#! usr/bin/python3
import requests
from bs4 import BeautifulSoup
import os

res = requests.get("http://www.cricbuzz.com/cricket-match/live-scores")

soup = BeautifulSoup(res.content,"lxml")

print("\t\t\t\tWELCOME TO LIVE CRICKET SCORE")
print("\n\n\n\n")
#print(soup.find_all("a",{"class":"cb-lv-scrs-well-live"})[0].text)
for item in soup.find_all("a",{"class":"cb-lv-scrs-well-live"}):
	print("\t\t\t"+item.text)	
	os.system('notify-send  "Live Cricket Score" "%s"' % (item.text) )

print("\n\n\n")
print("\n\n\n powered by cricbuzz.com")
'''

'''
from bs4 import BeautifulSoup
import numpy as np
import pandas as pd
import requests

page = requests.get("http://www.cricbuzz.com/cricket-series/2678/india-and-bangladesh-in-sri-lanka-t20i-tri-series-2018/points-table")

soup = BeautifulSoup(page.text)
#print(soup.prettify())


scoretable = soup.find('table',class_='table cb-srs-pnts')
team_name = [tn.get_text() for tn in scoretable.find_all('td',class_='cb-srs-pnts-name')]
#team_name.insert(0,'Team')
#print(team_name)



table_head = [th.get_text() for th in scoretable.find_all('td',class_='cb-srs-pnts-th')]
table_head.insert(5,'pts')
#print(table_head)



scores = [s.get_text() for s in soup.find_all('td',class_='cb-srs-pnts-td')]
teams_point = np.array(scores)
teams_point=teams_point.reshape(3,7)
#print(teams_point)

df = pd.DataFrame([teams_point[0][:],teams_point[1][:],teams_point[2][:]]
,index=team_name,columns=table_head)
df.columns.name = 'Teams'
print(df)
'''

import requests
from bs4 import BeautifulSoup
def web(page,WebUrl):
    if(page>0):
        url = WebUrl
        code = requests.get(url)
        plain = code.text
        s = BeautifulSoup(plain, "html.parser")
        for link in s.findAll('a', {'class':'s-access-detail-page'}):
            tet = link.get('title')
            print(tet)
            tet_2 = link.get('href')
            print(tet_2)
web(1,'http://www.amazon.in/s/ref=s9_acss_bw_cts_VodooFS_T4_w?rh=i%3Aelectronics%2Cn%3A976419031%2Cn%3A%21976420031%2Cn%3A1389401031%2Cn%3A1389432031%2Cn%3A1805560031%2Cp_98%3A10440597031%2Cp_36%3A1500000-99999999&bbn=1805560031&rw_html_to_wsrp=1&pf_rd_m=A1K21FY43GMZF8&pf_rd_s=merchandised-search-3&pf_rd_r=2EKZMFFDEXJ5HE8RVV6E&pf_rd_t=101&pf_rd_p=c92c2f88-469b-4b56-936e-0e65f92eebac&pf_rd_i=1389432031')

