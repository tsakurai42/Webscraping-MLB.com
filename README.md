# Project 2: Webscraping MLB.com

## Project guidelines
Perform ETL (Extract, Transform, Load) on two sources of data

## Project dependencies
json, requests, pandas, pymongo, BeautifulSoup, splinter'

## Details
Extracted data from mlb.com's API to collect data on the Rockies, top hitters and top pitchers (requests, Pandas, MongoDB)
Scraped data from mlb.com's "headline" box, parsed the text for player names and IDs. Scraped Rockies website for most recent Rockies video. Utilizing prior top hitters/top pitchers database, scraped for most recent video featuring each player. Combined pandas and splinter to pull standings table. Utilized Flask to present collected data and videos in a simple page.
