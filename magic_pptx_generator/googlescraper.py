from bs4 import BeautifulSoup, SoupStrainer
from html.parser import *
import http.client
import urllib.request
from urllib.request import urlopen, Request



def get_google_images(search_term, link_limit, named):

	#99 questions
	yes = ['y','ye','yes']
	img_formats = ['png', 'jpg', 'jpeg', 'gif']

	#search_term = str(input('Google Image Search: ')).replace(" ", "+")

	#link_limit = int(input("Enter link limit (1-100): "))

	#save_links_yn = str(input("Write links to a file? (y/n) ")).lower()
	#if save_links_yn in yes:
	#    filename_links = str(input("How should the file be named? "))
	save_links_yn = 'y'
	filename_links = named

	#download_pictures_yn = str(input("Download pictures? (y/n) ")).lower()
	#if download_pictures_yn in yes:
	#    filename_pictures = str(input("How should the image files be named? "))
	#    filepath_pictures = filename_pictures+'/'+filename_pictures
	filename_pictures = named
	download_pictures_yn = 'y'
	filepath_pictures = 'img/' + named + '/' + named


	#sets google url according to input
	search_url='+'.join(search_term.split())
	google_url = 'https://www.google.ch/search?site=webhp&tbm=isch&source=hp&q='+search_url+'&oq='+search_url

	#just checking the search url for mistakes
	print("Checking following URL:\n"+google_url+"\n")

	#adding headers to fool google
	req = Request(google_url, headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.2743.116 Safari/537.36'})
	soup = BeautifulSoup(urllib.request.urlopen(req), 'html.parser')


	#    for debugging and reverse engineering purposes
	#open('souptest1.html', 'w').write(str(soup.encode("utf-8")))
	#open('souptest2.txt', 'w').write(str(soup))


	#find all divs with class rg_meta because that's where the links are
	divs = soup.findAll("div", { "class" : "rg_meta" })


	link_counter = 0
	exception_counter = 0
	file_names = []
	for div in divs:
		try:
			#stripping elements of unnecessary characters
			div = str(div).partition('"ou":"')[-1]
			div = div.rpartition('","ow"')[0]
			div = str(div)

			#writing links to a file
			if save_links_yn in yes:
				open('img/' + filename_links+'.txt', 'a').write(div+"\n")

			#downloading the images
			if download_pictures_yn in yes:
				ext = div.split('.')[-1].split('/')[0].split('?')[0].split('#')[0]
				if ext not in img_formats:
					continue
				file_name =  filename_pictures+str(link_counter+1)+ '.' + ext
				file_names.append(file_name)
				urllib.request.urlretrieve(div, 'img/' + file_name)

			#if counter's limit reached, stop
			link_counter += 1
			if link_counter == link_limit:

				break
		except IOError:
			print("Error with:",div)
			exception_counter += 1
			link_counter -= 1

	print("\nlinks found:", link_counter)
	print("\nexceptions thrown:", exception_counter)

	return file_names

if __name__ == "__main__":
	get_google_images('big data engineer', 5, 'bde')