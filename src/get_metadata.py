#Python Program for retirving Metadata of Instance

import requests
import json


def get_aws_ec2_metadata():
    url = "http://169.254.169.254/latest/dynamic/instance-identity/document"
    response = requests.get(url)
    if response.status_code == 200:
        data = json.loads(response.text)
        return data
    else:
        return {"error": "sorry metadata is not loaded"}


def get_metadata():
    initial = ["meta-data/"]
    result = expand_tree(metadata_url, initial)
    return result


def get_metadata_json():
    metadata = get_aws_ec2_metadata()
    print(json.dumps(metadata, indent=2, sort_keys=True))
    
def is_json(myjson):
    try:
        json.loads(myjson)
    except ValueError:
        return False
    return True
