YouTube Data ETL Pipeline with Airflow and AWS<br><br>



Overview:<br>
This project extracts data from the YouTube API, transforms it into a structured format using pandas, and loads it into an AWS S3 bucket. <br>
It was built to automate the process of collecting video insights like views, likes, and comments—useful for content analysis, reporting, and data-driven decisions.<br>

Data Architecture:<br>
Here's a simple hand-drawn-style architecture to show how data flows in this project:<br>

![Airflow Project Architecture](https://github.com/user-attachments/assets/23b9a45a-21e9-4f59-94d4-0b4eb87bb009)<br>




Tech Stack:<br>
Apache Airflow            –  for scheduling and orchestrating the pipeline <br>
Python                    –  core logic for ETL <br>
YouTube Data API v3       –  for fetching video data <br>
Pandas                    –  for transforming data <br>
AWS S3                    –  for storing processed data <br>
Boto3                     –  for interacting with AWS services <br>



Key Features: <br>
Fetches and stores real-time YouTube video data<br>
Runs on a set schedule with Airflow DAGs<br>
Stores data securely in AWS S3 in .csv format<br>
Modular, simple code that’s easy to expand<br>
Built-in logging and error handling for smooth runs<br>



Lessons Learned: <br>
How to interact with external APIs like YouTube Data API <br>
Writing and scheduling DAGs in Apache Airflow <br>
Using AWS S3 and Boto3 for cloud storage <br>
Structuring ETL pipelines cleanly in Python <br>



Challenges Overcome: <br>
Configuring Airflow correctly on EC2 and locally <br>
Managing security groups and SSH access on AWS<br>
Figuring out how to parse and clean nested YouTube API responses <br>
Troubleshooting missing video stats for certain IDs <br>



Business Application : <br>
This pipeline can help content creators, marketing teams, and data analysts automate the process of tracking video performance on YouTube. <br>
By scheduling regular updates, it ensures access to fresh data without manual effort, enabling better decisions based on audience engagement.

