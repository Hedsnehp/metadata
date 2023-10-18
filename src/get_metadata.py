#Python Program for retirving Metadata of Instance

import requests
import json

metadata_url = "http://169.254.169.254/latest/meta-data/"

response = requests.get("http://169.254.169.254/latest/dynamic/meta-data")
print(r.text.split("\n"))

def get_aws_metadata():
    metadata = {
        'public-hostname': "",
        'ami-id': "",
        'instance-id': ""
    }

    for key in metadata.keys():
        resp = requests.get(
            f'http://169.254.169.254/latest/meta-data/{key}',
            timeout=1
        )
        if resp.status_code != 200:
            data = json.loads(resp.text)
        return data
    else:
        return {"error": "sorry metadata is not loaded"}
        
def get_metadata():
    initial = ["meta-data/"]
    result = expand_tree(metadata_url, initial)
    return result

def get_metadata_json():
    metadata = get_aws_metadata()
    print(json.dumps(metadata, indent=2, sort_keys=True))
    
def is_json(myjson):
    try:
        json.loads(myjson)
    except ValueError:
        return False
    return True
