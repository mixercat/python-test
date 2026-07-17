def readJson():
    import json

    x = '{"name": "Mix", "age": 22, "city": "Bangkok"}'

    y = json.loads(x)

    print(y["age"])

def WriteJson():
    import json

    x = {
        "name": "Mix",
        "age": 22,
        "city": "Bangkok"
    }

    y = json.dumps(x)

    print(y)

readJson()
WriteJson() 