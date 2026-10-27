#====== 05-10-2026 =======

#Task-1 :Dictionary Update

my_dict={'name': 'python', 'age': 25}
my_dict1={'city': 'west godavari'}
my_dict.update(my_dict1)
print(my_dict)

#Task-2 :Dictionary Access

product_info = {'name': 'laptop', 'brand': 'Dell', 'price': 1200}
print(product_info.get('price'))

#Task-3: Dictionary Removal

my_dict = {'name': 'John', 'age': 30, 'city': 'Bhimavaram'}
my_dict.pop('city')
print(my_dict)

#Task-4: Dictionary Keys

my_dict = {'name': 'python', 'age': 25, 'city': 'Rajahmundry'}
print(my_dict.keys())

#Task-5:Dictionary Values

my_dict = {'name': 'python', 'age': 25, 'city': 'tanuku'}
print(list(my_dict.values()))

#Exercise-1:Dictionary Updates

dict_1={
    "name1":"Padmasri",
    "name2":"Padhu",
    "name3":"Padmasrii",
}
dict_2={"name4":"Padhuu"}
dict_1.update(dict_2)
print(dict_1)

#Exercise-2: Dictionary Access

my_dict = {'name': 'Padmasri', 'age': 25}
print(my_dict.get('name'))

#Exercise-3: Dictionary Removal

dict_1 = {
    "name1": "Padmasri",
    "name2": "Padhu",
    "name3": "Padmasrii",
}
obj = dict_1.pop("name2")
print(obj)

#Exercise-4: Dictionary Keys

my_dict = {
    'name1': 'Padmasri',
    'name2': 'Padhu',
    'name3': 'Padmasrii'
}
print(list(my_dict.keys()))

#Exercise-5: Dictionary Values

my_dict = {
    'name1': 'Padmasri',
    'name2': 'Padhu',
    'name3': 'Padmasrii'
}
print(list(my_dict.values()))