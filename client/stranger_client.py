import urllib3
import json

http = urllib3.PoolManager()
api_url = "http://[your IP]:8080/stranger_wall/1.0.0/"


def get_messages():
    r = http.request(
        retries=urllib3.Retry(2),
        timeout=2.0,
        method="POST",
        url=api_url + "messages",
        fields={
        }
    )
    return json.loads(r.data)
