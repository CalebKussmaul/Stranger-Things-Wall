import urllib3
import json

http = urllib3.PoolManager()
api_url = "http://71.192.174.127:8080/stranger_wall/1.0.0/"


def get_messages():
    r = http.request(
        retries=urllib3.Retry(2),
        method="POST",
        url=api_url + "messages",
        fields={
        }
    )
    return json.loads(r.data)
