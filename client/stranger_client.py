import urllib3
import json
from settings import settings

http = urllib3.PoolManager()
api_url = "http://"+settings.server_ip+":"+str(settings.server_port)+"/stranger/"


def get_messages():
    r = http.request(
        retries=urllib3.Retry(2),
        timeout=2.0,
        method="POST",
        url=api_url + "messages",
        fields={
            "password": settings.password
        }
    )
    return json.loads(r.data)
