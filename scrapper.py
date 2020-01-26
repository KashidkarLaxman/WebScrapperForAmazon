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
	container=page_soup.findAll("div",{"class":"item-container"})
	return container

#check whether file is downloadable or not	
def is_Downloadable(url) :
	
	h=requests.head(url, allow_redirects=True)
	header=h.headers
	return True
		
def persist_image(url:str) :
	global x
	x=x+1;
	img='img_'+str(x)+'.jpg'
	url=url[2:len(url)]
	url='https://'+url
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
		url="https://www.newegg.com/Video-Cards-Video-Devices/Category/ID-38?pk=video%20card"
		listout=UrlScrapper(url)
		for elements in listout:
			persist_image(elements.a.img['data-src'])
			time.sleep(1)
	except Exception as E :
		print("Error :invalid error",E)

if __name__ == "__main__":
	x=0;
	main()
