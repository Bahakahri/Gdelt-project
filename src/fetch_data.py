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
    '''
    urls : list or url that has each file from GDLET daily database
    using urls generated download each file seperatly
    '''
    os.makedirs(save_path, exist_ok=True)
    for url in urls:
        filename = os.path.join(save_path, url.split("/")[-1])
        if not os.path.exists(filename):
            print("Downloading ...")
            r = requests.get(url)
            print(filename)
            if r.status_code == 200:
                with open(filename, "wb") as f:
                    f.write(r.content)
            else :
                print("Failed to download")
        else :
            print("Already downloaded")
    return 1



urls = generate_url("20220601","20230301")
download_data(urls)
       
    







