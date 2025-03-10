📂 GitHub User Repositories Fetcher
<br>
📌 Project Overview:
This project fetches and displays all repositories of a GitHub user. It uses the GitHub REST API to get details like repository name, stars, and description.
<br>
<br>
🎯 Project Goal:
The goal of this project is to learn how to use APIs, work with authentication, and parse JSON data while getting useful information from GitHub.
<br>
<br>
🛠 Tools & Technologies Used:
Programming Language: Python
APIs: GitHub REST API
Libraries:requests (to make API calls), json (to handle API responses)
<br>
<br>
🔑 Skills Learned:
1.How to request data from the GitHub API
2.How to use token-based authentication
3.How to parse JSON responses and extract useful information
<br>
<br>
📌 Project Steps:<br>
1.Get User Input: Ask for a GitHub username.<br>
2.Make API Request: Use the GitHub REST API to fetch repositories of the given user.<br>
3.Authentication: Use a GitHub personal access token to make secure API requests.<br>
4.Parse and Display Data: Extract and show repository details like name, stars, and description.<br>
<br>
<br>
✅ Project Outcome:
Successfully retrieved and displayed repositories of any GitHub user.
Learned how to work with API authentication and JSON parsing.
<br>
<br>
⚡ Challenges Faced & How I Overcame Them:<br>
1.Authentication Issues<br>
Problem: Without authentication, some API requests failed due to rate limits.<br>
Solution: Used a GitHub personal access token to authenticate and avoid request limits.<br>
<br>
2.Handling Users Without Repositories<br>
Problem: Some users had no public repositories, leading to empty results.<br>
Solution: Added a check to display a friendly message when no repositories are found.<br>
<br>
3.Understanding JSON Responses<br>
Problem: Extracting the correct data from the API response was confusing at first.<br>
Solution: Used json.dumps(response, indent=4) to print and analyze the response format.<br>





