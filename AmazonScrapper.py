import os
import bs4
import requests
from sys import *
import time
from urllib.request import urlopen
import io
import shutil

def UrlScrapper(url):
	connection=urlopen(url)
	raw_html=connection.read()
	connection.close()
	page_soup=bs4.BeautifulSoup(raw_html,"html.parser")
	container=page_soup.findAll("div",{"class":"a-row a-spacing-base"})
	print('in urlscrapper')
	return container

#check whether file is downloadable or not	
def is_Downloadable(url) :
	
	h=requests.head(url, allow_redirects=True)
	header=h.headers

	return True
#save image into file
def persist_image(url:str) :
	global x
	x=x+1;
	img='img_'+str(x)+'.jpg'
	print(url)
	d=is_Downloadable(url)
	if d :
		try:
			img_data = requests.get(url).content
			with open(img, 'wb') as handler:
				handler.write(img_data)
		
		except Exception as e :
			print("cant Download")
	else :
		print("it seems other file")
def main():
	print("image scrapper by laxman kashidkar")
	print("Application name:"+argv[0])
	try :
		url="https://www.amazon.in/b/ref=br_msw_pdt-4?_encoding=UTF8&node=20603713031&smid=A2QX6NNXDXIFAE&pf_rd_m=A1VBAL9TL5WCBF&pf_rd_s=&pf_rd_r=YJMHQS9R6YD7EA41H3CK&pf_rd_t=36701&pf_rd_p=3ee7fd98-e85f-47bb-91a5-7de85fe7ede5&pf_rd_i=desktop"
		listout=UrlScrapper(url)
		for elements in listout:
			if elements.a.img :
				persist_image(elements.a.img['src'])
				time.sleep(1)
			else :
				print(' not image')
	except Exception as E :
		print("Error :invalid error",E)

if __name__ == "__main__":
	x=0;
	main()
