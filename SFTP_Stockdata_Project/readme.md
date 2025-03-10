Real-Time Stock Price Collection and Analysis<br>

1. Project Aim:<br>
The goal of this project is to collect real-time stock prices, securely store them, design a model for the data, and load it into a data warehouse for further analysis. I aim to track stock price trends and make it easy to analyze them using SQL queries.
<br>
<br>
2. Tools Used:<br>
Yahoo Finance API: To get real-time stock prices and company data.<br>
Python (requests, paramiko, gnupg): To scrape data from the API, encrypt files, and upload them securely.<br>
SFTP (Secure File Transfer Protocol): To upload the encrypted files to a secure server.<br>
PostgreSQL: To store and manage the data in a database.<br>
SQL: To analyze the data by writing queries.<br>
<br>
<br>
3. Skills Used:<br>
API scraping to extract stock data.<br>
Data encryption for security.<br>
File handling and uploading via SFTP.<br>
Designing a dimensional model (fact and dimension tables).<br>
Writing SQL queries to analyze stock data.<br>
<br>
<br>
4. The Process:<br>
Step 1: API Scraping (Stock Market Data) I used the Yahoo Finance API to gather real-time stock prices, volumes, and company details. I stored the data in a simple file format like JSON or CSV for easy access.<br>
<br>
Step 2: Encrypt & Store Data in SFTP The data collected was encrypted using PGP to keep it secure. I used paramiko to upload the encrypted files to an SFTP server for storage.<br>
<br>
Step 3: Design a Dimensional Model I created a database model with:<br>
A fact table called stock_prices that stores stock prices, volume, open/close values, and timestamps.<br>
Dimension tables like companies for storing company details and dates for storing trading dates (day, week, month).<br>
<br>
Step 4: Load Data into a Data Warehouse The encrypted data was pulled from the SFTP server, decrypted, and loaded into PostgreSQL. I then used SQL queries to analyze stock trends over time.<br>
<br>
<br>
6. Challenges I Faced:<br>
Learning how to securely encrypt data and work with SFTP was difficult at first.<br>
Designing the database model was tricky, especially deciding which data to include in the fact and dimension tables.<br>
Writing SQL queries for analysis took some time to master.<br>
<br>
<br>
7. How I Overcame the Challenges:<br>
I researched online resources and tutorials to understand encryption and SFTP better.<br>
I studied dimensional modeling and practiced building models with different data sets.<br>
I practiced writing SQL queries daily to get better at analyzing data and understanding trends.<br>
