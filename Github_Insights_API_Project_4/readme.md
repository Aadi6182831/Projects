GitHub Insights API Project<br>
<br>
📌 Project Overview:<br>
This project fetches and analyzes repository data of a GitHub user using the GitHub REST API. The data is extracted, processed, and stored in a SQLite database for further analysis.<br>
<br>
<br>
🎯 Goal:<br>
The main objective of this project is to: <br>
Retrieve repositories of a GitHub user.<br>
Extract important details like repository name, stars, forks, and language.<br>
Store the data in a structured format for easy analysis.<br>
Perform basic data analysis on the collected repository data.<br>
<br>
<br>
🛠 Tools & Technologies Used:<br>
Programming Language: Python<br>
Libraries: requests, pandas, json, sqlite3, csv<br>
API Used: GitHub REST API<br>
Database: SQLite<br>
<br>
<br>
🧑‍💻 Skills Used:<br>
Working with REST APIs<br>
Authentication using API tokens<br>
JSON parsing and data extraction<br>
Data transformation using Pandas<br>
Storing and querying data in SQLite<br>
<br>
<br>
📌 Steps to Build the Project:<br>
Fetch Data from GitHub API:<br>
Use Python's requests library to send a GET request to the GitHub API.<br>
Authenticate using a GitHub personal access token.<br>
Retrieve and store repository details in JSON format.<br>
<br>
Process the Data:<br>
Extract useful information such as repository name, stars, forks, and language.<br>
Convert the JSON response into a structured format (list of dictionaries).<br>
Convert the structured data into a Pandas DataFrame.<br>
<br>
Store the Data:<br>
Save the extracted data into a CSV file for future reference.<br>
Load the data into an SQLite database for further analysis.<br>
<br>
Analyze the Data:<br>
Perform basic queries using SQL to retrieve insights.<br>
Group repositories by language and count the number of repositories per language.<br>
<br>
<br>
Logging Execution Details:<br>
Log the script execution time in a text file.<br>
<br>
<br>
✅ Final Result:<br>
Successfully retrieved repository data for the given GitHub user.<br>
Stored the data in both CSV and SQLite databases.<br>
Performed analysis to find the most used programming languages.<br>
<br>
<br>
⚡ Challenges Faced & How I Overcame Them:<br>
1. API Authentication Issues<br>
Initially faced authentication errors.<br>
Solved by using a GitHub personal access token correctly in the request headers.<br>
<br>
2. Handling Missing Data<br>
Some repositories had missing descriptions or languages.<br>
Used conditional statements to handle missing values gracefully.<br>
<br>
3. Storing Data Efficiently<br>
Faced issues while inserting large data into SQLite.<br>
Optimized insertion using batch inserts and structured queries.<br>
