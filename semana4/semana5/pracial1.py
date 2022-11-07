
studies_dict = {
        "U": {
            "description":"Ultrasonido",
            "price": 8900
        },
        "T": {
            "description":"Tomografia",
            "price": 12640
        },
        "R": {
            "description":"Resonancia",
            "price": 15600
        }
    }

print(studies_dict.get("U").get("description"))


        