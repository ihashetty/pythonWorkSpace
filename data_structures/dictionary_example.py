"""Dictionary example"""


information = {"name": "Alice",
               "age": 28,
               "address": {"home": {"street": "123 Main St",
                                    "city": "Wonderland", "zip": "12345"},
                           "work": {"street": "456 Work Rd",
                                    "city": "Worktown", "zip": "67890"},
                           "natives": {"street": "456 Work Rd",
                                       "city": "Worktown", "zip": "67890"}},
               "hobbies": ["reading", "traveling", "swimming"]}

print(information["name"])
print(information["address"]["natives"]["city"])
print(information["hobbies"][1])
print(information["address"]["natives"]["zip"])
