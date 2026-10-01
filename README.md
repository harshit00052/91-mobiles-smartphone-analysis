# Mobile Market Analysis – 91mobiles

## Overview

This project focuses on collecting, cleaning, and analyzing smartphone data from [91mobiles](https://www.91mobiles.com/) using Python, Selenium, and BeautifulSoup.

The objective is to build a structured dataset containing information about smartphones, including their brands, prices, processors, RAM, storage, camera specifications, battery capacity, and display features.

The collected data provides a foundation for understanding smartphone market trends, comparing devices across different price segments, and exploring the relationship between technical specifications and pricing.

## Objectives

* Automate smartphone data collection using web scraping.
* Extract product details and technical specifications from 91mobiles.
* Handle dynamically loaded content using Selenium.
* Clean and preprocess the scraped dataset.
* Identify and handle missing values and inconsistencies.
* Standardize smartphone specifications for further analysis.
* Prepare a structured dataset for exploratory data analysis (EDA) and visualization.

## Technologies Used

| Technology       | Purpose                                         |
| ---------------- | ----------------------------------------------- |
| Python           | Core programming language                       |
| Selenium         | Browser automation and dynamic content handling |
| BeautifulSoup    | HTML parsing and data extraction                |
| Pandas           | Data cleaning and manipulation                  |
| NumPy            | Missing value handling and numerical operations |
| Matplotlib       | Data visualization                              |
| Seaborn          | Statistical visualization                       |
| Jupyter Notebook | Development and experimentation                 |

## Data Collection

The data was collected from [91mobiles](https://www.91mobiles.com/), a platform providing smartphone specifications, prices, and comparisons.

The scraping process involved:

1. Accessing smartphone listings using Selenium.
2. Extracting product information from the website's HTML structure.
3. Parsing HTML elements using BeautifulSoup.
4. Collecting smartphone specifications and pricing details.
5. Handling dynamically loaded content and pagination.
6. Storing the extracted information in structured lists.
7. Converting the collected data into a Pandas DataFrame.

## Dataset Features

The dataset includes the following attributes:

| Feature       | Description                                |
| ------------- | ------------------------------------------ |
| Brand         | Smartphone manufacturer                    |
| Model         | Smartphone model name                      |
| Price         | Listed price of the smartphone             |
| RAM           | Available RAM capacity                     |
| Storage       | Internal storage capacity                  |
| Processor     | Processor or chipset information           |
| Camera        | Camera specifications                      |
| Battery       | Battery capacity                           |
| Display Size  | Screen size in inches                      |
| AnTuTu Score  | Performance benchmark score                |
| Camera Count  | Number of camera sensors                   |
| Charging Type | Charging technology supported              |
| Display Type  | Display technology, such as AMOLED or OLED |

*Note: The exact availability of attributes may vary depending on the smartphone and the information provided on the source website.*

## Data Cleaning and Preprocessing

After scraping, the dataset underwent preprocessing to improve data quality and consistency.

Key preprocessing steps included:

* Identifying and handling missing values.
* Removing irrelevant records, such as keypad phones, where applicable.
* Standardizing smartphone specifications.
* Cleaning price, RAM, storage, and battery capacity fields.
* Handling inconsistencies in display technology names.
* Converting numerical attributes into appropriate data types.
* Identifying and addressing duplicate records.
* Preparing the dataset for exploratory analysis.

## Project Structure

```text
Mobile-Market-Analysis/
│
├── datasets/
│   ├── raw_mobile_data.csv
│   └── cleaned_mobile_data.csv
│
├── notebooks/
│   ├── web_scraping.ipynb
│   └── data_cleaning_eda.ipynb
│
├── README.md
└── requirements.txt
```

*Update the folder and file names according to your actual repository structure.*

## Installation and Setup

### 1. Clone the Repository

```bash
git clone <your-repository-url>
```

### 2. Navigate to the Project Directory

```bash
cd Mobile-Market-Analysis
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Run the Notebook

Open the Jupyter Notebook and execute the cells to explore the scraping, cleaning, and analysis process.

## Potential Analysis

The collected dataset can be used to explore several interesting questions:

* Which smartphone brands offer the most devices across different price segments?
* How does RAM capacity vary with smartphone pricing?
* Is there a relationship between battery capacity and price?
* How do display technologies differ across brands and price ranges?
* Which brands offer higher AnTuTu scores at relatively lower prices?
* How does camera configuration vary across smartphone categories?
* What are the most common specifications in the smartphone market?

## Key Learnings

Through this project, I gained practical experience in:

* Web scraping using Selenium and BeautifulSoup.
* Handling dynamic web pages and pagination.
* Extracting structured data from complex HTML elements.
* Cleaning and preprocessing real-world datasets.
* Handling missing values and inconsistent product specifications.
* Using Pandas and NumPy for data manipulation.
* Preparing scraped data for exploratory data analysis.
* Understanding the challenges of collecting data from real-world websites.

## Data Source

[91mobiles – Smartphone Specifications and Comparisons](https://www.91mobiles.com/)

**Disclaimer:** This project is intended for educational and analytical purposes. All data belongs to its respective source. Please respect the website's terms of use and scraping policies.

---

**Author:** Harshit Kumar

**Domain:** Data Analytics | Web Scraping | Python
