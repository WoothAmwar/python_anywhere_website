import requests
from YoutubeData.youtube import complete_reload
from YoutubeData.youtube_database import (mongo_insert_test, get_all_user_google)

def youtube_job():
    """
    Calls the complete_reload function at a specific time every day
    :return: None
    """
    # print("Doing the thing")
    mongo_insert_test(calledAsIntended=False)
    all_user_google_ids = get_all_user_google()
    for googleID in all_user_google_ids:
        complete_reload(googleID, doReturn=False)
    # with scheduler.app.app_context():
    # complete_reload(doReturn=False)

def malw_job():
    r = requests.post("https://malw-api.onrender.com/api", timeout=300)
    print(r.json())

youtube_job()
malw_job()