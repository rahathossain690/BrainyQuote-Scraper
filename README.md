# BrainyQuote Scraper
Web scraper to extract quotes from a page of brainyQuote.com and save those in CSV format.
# Install dependencies
```
pip install -r requirements.txt
```
# How to use
```
# Syntax 1 : Scrap from a link
python BrainyQuote-Scraper.py -l <LINK_TO_BrainyQuote_PAGE> -o <FILENAME_WITHOUT_EXTENSION> -r

# Syntax 2 : Scrap from a file
python BrainyQuote-Scraper.py -f <FILENAME_WITHOUT_EXTENSION> -o <FILENAME_WITHOUT_EXTENSION> -r
```
Example:
```
# Example 1
python brainyQuote-Scraper.py -l https://www.brainyquote.com/topics/positive-quotes -o Positive-Quotes -r

# Example 2
python brainyQuote-Scraper.py -f Inspiration -o My-quotes
```
Here
1. -l or --link argument is for link.
2. -f is for the filename-without-extension to scrap from. It always takes the extension as html. (It is mandatory to have -f or -l)
3. -o or --output stands for the filename(without extension) to save data. It is not mandatory. Takes 'output' as default value if not specified.
4. -r is flag for reading data. It is not mandatory. Shows data on terminal if specified.

Thank you.