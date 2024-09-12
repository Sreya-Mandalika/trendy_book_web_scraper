# Ethics of the Trendy Book Webscraping Project
## Purpose of data collection
I am collecting this data for two main reasons:
1. For educational purposes - I need to do web-scraping for a class project
2. I am interested in books, so I wanted to focus on a book-related website that allowed web-scraping.
   The website features a random book generator, but I wanted to focus on books deemed "trendy"
   (aka ones more users are more likely to read) and pick a random book from that section.

## Data sources and robots.txt
This site prohibits users from accessing API or search realted info (ex. searches within the website). 
However, it allows the main sections of the website (such as the trending books or many other browse sections, for instance)
to be scraped.

## Collection practices
I have only done scraping on one main section of the website (trending books) to avoid major disruption to the wesite. 
There are no password protections I have bypassed, 
and I have added a time.sleep(1) function to avoid bothering the server too much.

## Data handling and privacy
There is no confidential data within the file; it is only data publicly accessible to everyone looking at the website.

## Data usage
This data will only be used for educational purposes (for a class project), and not for any other reason, monetary or otherwise.
