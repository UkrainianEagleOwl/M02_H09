
# Web Scraping with Scrapy

## Overview
This project uses the Scrapy framework to perform web scraping of quotes and author information from http://quotes.toscrape.com. It generates two JSON files, `quotes.json` and `authors.json`, which are structured for integration with a cloud database. The scraped data aligns with the structures required for previously developed database scripts.

## Features
- **Scrapy Web Scraping**:
  - Scrapes quotes and authors from all pages of the specified website.
- **JSON File Generation**:
  - `quotes.json`: Contains information about quotes.
  - `authors.json`: Contains details of authors of the scraped quotes.
- **Database Integration**:
  - Compatibility with cloud database scripts for loading scraped data.

## File Structure
- `quotes.json`: Stores scraped quotes data.
- `authors.json`: Stores scraped authors data.
- `main.py`: The primary script to initiate the web scraping process.

## Usage
1. **Running the Scraper**:
   - Execute `main.py` to start the web scraping process.
   - The script uses Scrapy to crawl http://quotes.toscrape.com and extracts the required data.
2. **JSON File Generation**:
   - The scraper will generate `quotes.json` and `authors.json` in the specified format.
3. **Database Integration**:
   - Use the existing database scripts to load data from JSON files into the cloud database.
   - Ensure compatibility with the database schema as per previous homework.

## Installation and Dependencies
- Clone the repository.
- Requires Python with Scrapy installed.
- Additional dependencies for database integration (e.g., cloud database client libraries).
