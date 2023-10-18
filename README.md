Metadata for EC2 instance
Amazon Elastic Compute Cloud (Amazon EC2) is a web service that provides resizable compute capacity in the cloud. Each EC2 instance comes with metadata that you can access to obtain information about the instance. This metadata is available at a well-known URL, which is accessible from within the instance. The base URL for EC2 instance metadata is (http://169.254.169.254/latest/meta-data/).

Instance Metadata:

instance-id: The unique identifier for the instance. ami-id: The ID of the Amazon Machine Image used to launch the instance. instance-type: The type of EC2 instance (e.g., t2.micro, m5.large). local-hostname: The private DNS hostname of the instance. public-hostname: The public DNS hostname of the instance. local-ipv4: The private IPv4 address of the instance. public-ipv4: The public IPv4 address of the instance. mac: The MAC address of the instance's network interface

#Steps

Create EC2 instace in linux AMI (free tier)
connect to that instance
sudo yum install python3
sudo yum install git
Clone the Metadata repository : git clone https://github.com/Hedsnehp/metadata.git
Install PIP environment : sudo pip3 install pipenv
cd Metadata
Install the dependencies : pipenv install & pip3 install requests
run command : python3 get_metadata.py


Explaination :


1. `import requests` and `import json`:
   - These lines import two Python libraries. `requests` is used for making HTTP requests, and `json` is used for handling JSON data.

2. `response = requests.get("http://169.254.169.254/latest/dynamic/meta-data")`:
   - This line sends an HTTP GET request to a specific URL (an AWS metadata URL), and the response is stored in the variable `response`.

3. `print(r.text.split("\n"))`:
   - This line prints the content of the HTTP response body, `r.text`, after splitting it by newline characters (`\n`). It appears to contain AWS metadata.

4. `def get_aws_metadata():`:
   - This line defines a function named `get_aws_metadata`. This function is intended to retrieve specific AWS metadata.

5. `metadata = {...}`:
   - Inside the `get_aws_metadata` function, a dictionary named `metadata` is defined. It will store AWS metadata such as the public hostname, AMI ID, and instance ID.

6. `for key in metadata.keys():`:
   - This initiates a loop that iterates through the keys in the `metadata` dictionary.

7. `resp = requests.get(f'http://169.254.169.254/latest/meta-data/{key}', timeout=1)`:
   - Within the loop, this line sends an HTTP GET request to a specific AWS metadata URL based on the `key`. The `timeout` parameter ensures that the request times out after 1 second if no response is received.

8. `if resp.status_code != 200:`:
   - This condition checks if the response status code is not equal to 200, which typically indicates an error.

9. `data = json.loads(response.text)`:
   - If the status code is not 200, this line attempts to load the response content as JSON into the `data` variable. There is a small typo in the variable name; it should be `resp` instead of `response`.

10. `return data`:
    - This returns the `data` variable, which contains AWS metadata, from the function.

11. `else:`:
    - If none of the keys in the loop results in a successful metadata retrieval (i.e., all responses have status codes other than 200), this `else` block is entered.

12. `return {"error": "sorry metadata is not loaded"}`:
    - In this case, a dictionary with an error message is returned, indicating that the metadata was not successfully loaded.

13. `def get_metadata():`:
    - This line defines a new function named `get_metadata`.

14. `initial = ["meta-data/"]`:
    - Initializes a list called `initial` with a single string element.

15. `result = expand_tree(metadata_url, initial)`:
    - Calls a function `expand_tree` with the arguments `metadata_url` and `initial`, but the `metadata_url` variable is not defined in this code snippet.

16. `return result`:
    - Returns the `result` variable, which is the result of the `expand_tree` function.

17. `def get_metadata_json():`:
    - This line defines a function named `get_metadata_json`.

18. `metadata = get_aws_ec2_metadata()`:
    - Calls a function `get_aws_ec2_metadata` (the correct function name should be `get_aws_metadata` as defined earlier) and stores the result in the `metadata` variable.

19. `print(json.dumps(metadata, indent=2, sort_keys=True))`:
    - Converts the `metadata` dictionary to a JSON string with indentation and sorted keys, and then prints it.

20. `def is_json(myjson):`:
    - This line defines a function named `is_json` which checks whether a given input can be parsed as JSON.

21. `try:` and `except ValueError:`:
    - Inside the `is_json` function, this code attempts to parse the input as JSON and catches any `ValueError` exceptions.

22. `return False`:
    - If the input cannot be parsed as JSON, the function returns `False`.

23. `return True`:
    - If the input can be parsed as JSON without errors, the function returns `True`.

Make sure to correct the typos and variable names in your code and provide a clear explanation of the code's purpose and functionality when discussing it with the interviewer.
