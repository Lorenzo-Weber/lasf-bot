import json
import subprocess

def getInfos():

    status = "curl --request GET --url https://api.iproxy.online/v1/connections?with_statuses=1 --header 'authorization: PRXGYSLDEKNK4YGDHERFKXT'"
    result = subprocess.run(status, shell=True, capture_output=True, text=True)

    return formatData(str(result))

def formatData(data):
    index_start = data.find('[{"id"')
    data = data[index_start:]

    index_end = data.find("}', stderr")
    data = data[:index_end]

    if data.endswith('"}'):
        data += "]"
    
    return data

def storeData(data):
    try:
        json_data = json.loads(data)
    except json.JSONDecodeError as e:
        print(f"Error parsing JSON: {e}")
        json_data = None

    if json_data:
        with open('data.json', 'w') as json_file:
            json.dump(json_data, json_file, indent=4)

def run():
    data = getInfos()
    storeData(data)