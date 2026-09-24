# Kenyan Stock Market Analysis

An analysis of historical Nairobi Securities Exchange data comparing Safaricom (SCOM), Equity Group (EQTY), and KenGen (KEGN) from April 2008 to October 2025.

## Project overview

The project combines yearly stock data, cleans dates and prices, checks duplicate records, and compares the three stocks using Python and Power BI. The dashboard shows a monthly price trend and each stock's ending price index.

## Tools

- Python: pandas and matplotlib
- Power BI Desktop

## Data source

[Nairobi Securities Exchange Stocks Data on Kaggle](https://www.kaggle.com/datasets/macmini62/nairobi-securities-exchangense-stocks-data)

The downloaded files cover 2007–2025. This three-stock comparison begins on 23 April 2008, when Safaricom data becomes available.

## Data preparation

- Combined 19 yearly CSV files into 301,005 rows.
- Standardized changing column names and parsed two date formats.
- Removed rows without an essential date, stock code, or day price.
- Removed 91 extra identical records.
- Set aside 272 rows from conflicting date-and-stock-code records for review.
- Used 300,639 records in the cleaned analysis dataset.

## Comparison method

Each stock's first available price in the comparison period is set to an index of 100. Equity's prices before 26 March 2009 are divided by 10 to account for its 10-for-1 share split. The split is documented in [Equity Bank's 2009 annual report](https://equitygroupfoundation.com/wp-content/uploads/2019/10/Equity-Bank-Annual-Report-2009.pdf).

The monthly chart uses the last available trading price in each month. The price index excludes dividends and may not account for other corporate actions. It should not be interpreted as total investment return.

## Dashboard results

| Stock | Ending price index, October 2025 |
| --- | ---: |
| Safaricom (SCOM) | 605.0 |
| Equity Group (EQTY) | 312.5 |
| KenGen (KEGN) | 42.7 |

![Power BI dashboard](images/powerbi_dashboard.png)

## Project structure

- `python/` — data inspection, cleaning, comparison, and plotting scripts
- `dashboard/` — Power BI report
- `images/` — chart and dashboard screenshots
- `data/` — downloaded and generated CSV files on the local computer