import json

def WriteToJson(file_path: str, data_list: list):
    with open("./data/" + file_path, "w") as file_out:
        json.dump(data_list, file_out)