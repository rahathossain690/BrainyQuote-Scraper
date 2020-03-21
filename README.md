# BrainyQuotes Scraper
Web scraper to extract quotes from a page of BrainyQuotes.com and save those in CSV format.
# Install dependencies
```
pip install -r requirements.txt
```
# How to use
```
python BrainyQuotes-Scraper.py -l <LINK_TO_BrainyQuotes_PAGE> -o <FILENAME_WITHOUT_EXTENSION> -r
```
Example:
```
python BrainyQuotes-Scraper.py -l https://www.brainyquote.com/topics/positive-quotes -o Positive-Quotes -r
or
python BrainyQuotes-Scraper.py -l https://www.brainyquote.com/topics/attitude-quotes -o Attitude-Quotes
or
python BrainyQuotes-Scraper.py -l https://www.brainyquote.com/topics/positive-quotes
```
Here
* -l or --link argument is for link and is mandatory.
* -o or --output stands for the filename(without extension) to save data. It is not mandatory. Takes 'output' as default value if not specified.
* -r is flag for reading data. It is not mandatory. Shows data on terminal if specified.
Thank you.