names = []

def add_name(name):
    if name not in names:
        names.append(name)

def remove_name(name):
    if name in names:
        names.remove(name)

def search_name(name):
    return name in names

def show_all_names():
    return names

add_name("Juan")
add_name("Maria")
add_name("Juan") 
print(names)  
remove_name("Juan")
print(names)  
print(search_name("Maria"))  
print(show_all_names())  
