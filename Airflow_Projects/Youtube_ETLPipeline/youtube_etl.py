from googleapiclient.discovery import build
import os
import pandas as pd
import boto3




api_key = os.getenv("YOUTUBE_API_KEY")
if not api_key:
    raise Exception("API key not found. Please set YOUTUBE_API_KEY.")

youtube = build('youtube', 'v3', developerKey=api_key)
print("Successfully connected to YouTube API.")



S3_BUCKET_NAME = "youtubeetl-pipeline-project1"
S3_FILE_NAME = "youtube_data.csv"


def extract_youtube_data(video_id):
    response = youtube.videos().list(part="snippet,statistics",id=video_id).execute()

    if not response['items']:
        return None
    
    # Extracting relevant data from the response
    videos_data = []
    
    for video in response['items']:
        data = {
        "video_id": video["id"],
        "title": video["snippet"]["title"],
        "channel": video["snippet"]["channelTitle"],
        "published_at": video["snippet"]["publishedAt"],
        "views": int(video["statistics"].get("viewCount", 0)),
        "likes": int(video["statistics"].get("likeCount", 0)),
        "comments": int(video["statistics"].get("commentCount", 0)),
        }
        videos_data.append(data)
    return  videos_data

def transform_data(data):
    return pd.DataFrame(data)


def load_to_s3(df):
    """Upload data to Amazon S3"""
    s3 = boto3.client('s3')  
    csv_stringtype_storage = df.to_csv(index=False)  
    s3.put_object(Bucket=S3_BUCKET_NAME, Key=S3_FILE_NAME, Body=csv_stringtype_storage ) 


def run_youtube_etl():
    video_id="FFtPSPByBmk,B8C38FSvd6Q"
    extracted_data=extract_youtube_data(video_id)
     
    if extracted_data:
        df=transform_data(extracted_data)
        load_to_s3(df)
        print(" ETL Pipeline Completed!✅")
    else:
        print(" No data extracted.⚠️")

if __name__ == "__main__":
    run_youtube_etl()
