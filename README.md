# Automated Web Scraping and Data Processing

Automated scripts for web scraping product data from Wegmans using an API, storing it in an RDBMS, and checking URL statuses.

## Overview

This project automates the process of fetching product data from Wegmans using an API, saving the data to a JSON file, processing it to extract essential information (product name, price, URL), storing it in a relational database management system (RDBMS), and checking the status of saved URLs.

## Features

- **fetch_data.py**: Script to fetch product data from Wegmans API and save it to a JSON file (`data.json`).
- **process_data.py**: Script to process `data.json`, extract product details, store them in an RDBMS, and check URL statuses.
- **check_urls.py**: Service to verify if saved URLs are active and update the RDBMS accordingly.

## Prerequisites

- Python 3.x installed.
- Required Python packages: `requests`, `mysql-connector-python`.
- MySQL server installed and running.

## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/sujeesh-sunny/auto_scraping.git
   cd repository
