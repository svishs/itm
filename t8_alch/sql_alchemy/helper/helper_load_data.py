import json 

#возвращает json объект
def json_loader(file: str):
    with open(file) as read_file:
        data = json.load(read_file)
    return data