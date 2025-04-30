from datetime import datetime, timedelta
import os
import requests

def generate_url(start,end):
    '''
    start, end : start and end date for urls : str
    generate urls daily from startdate to enddate for GDELT v1 database
    '''
    startdate = datetime.strptime(start, "%Y%m%d")
    enddate = datetime.strptime(end, "%Y%m%d")
    urls = []

    while startdate <= enddate:
        date_str = startdate.strftime("%Y%m%d")
        url = f"http://data.gdeltproject.org/events/{date_str}.export.CSV.zip"
        urls.append(url)
        startdate += timedelta(days=1)
        
    return urls

def download_data(urls, save_path="data/raw"):







urls = generate_url("20230601","20250429")
print(len(urls))