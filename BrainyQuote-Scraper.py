import requests, argparse, csv
from bs4 import BeautifulSoup as soup

def scraper(link, file):
	try:
		# sends request
		r = requests.get(url = link)
		# gets data 
		data = r.text
		page_soup = soup(data, "html.parser")
		# BrainyQuotes:Quote's title is 'view quotes'
		# BrainyQuotes:Author's title is 'view author'
		quote_tag = page_soup.findAll("a", {"title" : "view quote"})
		author_tag = page_soup.findAll("a", {"title" : "view author"})
		# extracts real data
		quote = list(map(lambda x: x.text, quote_tag))
		author = list(map(lambda x: x.text, author_tag))
		i = 0
		# to store table contents
		tables = []
		while i < len(quote):
			tables.append([quote[i], author[i]])
			i += 1
		# writes to file
		writeCSV(tables, file)
	except:
		print("Scraping error. Try again with valid inputs.")

def writeCSV(finalList, fileName):
	# writes into file
	try:
		with open(fileName + ".csv", 'w') as file:
			writer = csv.writer(file)
			writer.writerows(finalList)
	except:
		print("Error in writing file")

def CSVReader(filename):
	# reads file data
	# can be formated
	try:
		with open(filename) as csv_file:
			csv_reader = csv.reader(csv_file, delimiter=',')
			
			print("Quote\t:\tquote\nAuthor\t:\tauthor\n");

			for row in csv_reader:
				string = "Quote\t:\t{0}\nAuthor\t:\t{1}\n".format(row[0], row[1])
				'''
				row[0] = Quote
				row[1] = author
				'''
				print(string)
	except:
		print("Error in reading file.")


if __name__ == '__main__':
	# main function
	try:
		# manages the arguments
		ap = argparse.ArgumentParser()
		ap.add_argument("-l", "--link", help="Page link of Brainyquote")
		ap.add_argument("-o", "--output", help="Output file-name-only")
		ap.add_argument("-r", "--read", action='store_true', help="Read flag")
		args = vars(ap.parse_args())

		# assigns values to missing arguments if necessery
		if args["output"] == None:
			args["output"] = "output"

		# checks if link is missing, if yes then raises exception
		if args["link"] == None or args == None:
			raise Exception("-l or --link is mandatory.")

		# calls scraper function
		scraper(args["link"], args["output"])

		#if read flag is true then read
		if args["read"]:
			CSVReader(args["output"] + ".csv")

	except:
		print("Try again")