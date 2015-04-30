# GEWatch
Scrapes and performs pattern matching on Runescape grand exchange data.

VERY much still a work in progress. For now the workflow is as follows:

## Setting up which items to scrape

Before doing anything, open up GrandExchange.py and input the ItemID numbers for the items you are interested in into `item_ids`

You can find itemIDs either on the Official Runescape Grand Exchange website by looking at the URL, or you can use a website like the Runescape Wiki.


## Scrape GrandExchangeWatch

Run ScrapeGE.py in your terminal

```
>>> python ScrapeGE.py
```

The data will be stored in .csv files in the directory ScrapeGE.py is located in

Note that in ScrapeGE.py there is a variable called `pagenums`, this determines how far back into GrandExchangeWatch's data the scraper will go. Some items aren't old enough to go back very far, and others can go back to the beginning of RS. GrandExchangeWatch gives how many days of data they have for each item, so some logic should be written to scrape all available days based on that information. 


## Perform Analysis

Run GEAnalysis_Mass.py the same way as ScrapeGE.py
```
>>> python GEAnalysis_Mass.py
```

This will run the pattern-matching on all members of your `item_ids` list as long as the .csv files have been generated. 

GEAnalysis_Mass.py will output another .csv file called ItemsOfInterest.csv, which will contain the items in your list which are projected to rise in price in the next 20 days. The Twitter bot uses this file to write its tweets.