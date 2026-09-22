print("_____Iterable objects & RANGE_____")
# Iterate objects > string, dictionary, tuple, list, zip, range, map, filter

range_obj = range(3)
print(range_obj)

for letter in "MIT":
    print(f"the letter: {letter}")

for ele in range_obj:
    print(ele)


print("_____DICTIONARY_____")
# Dictonary is JSON Object!
person = {"name": "Jamolkhon", "age": 20, "ismarried": False}
person_obj = dict(name="Joseph", age=20, isMarried=False)
print(f"the person: {person}")
print(f"the person_obj: {person_obj}")

# name = person_obj["name"]
name = person_obj.get("name")
hobby = person_obj.get("hobby")
balance = person_obj.get("balance", 0)
print(f"the name: {name}, hobby: {hobby} and balance: {balance}")

# name2 = person_obj["hobby"]
# print(name2) => Error qaytaradi

del person_obj["isMarried"]
for key in person_obj:
    print(f"the key: {key} => value: {person_obj[key]}")
