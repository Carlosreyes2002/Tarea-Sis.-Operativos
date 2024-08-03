names = []

def load_names():
    global names
    try:
        with open("names.txt", "r") as file:
            names = file.read().splitlines()
    except FileNotFoundError:
        names = []

def save_names():
    with open("names.txt", "w") as file:
        for name in names:
            file.write(name + "\n")

def add_name(name):
    if name not in names:
        names.append(name)
        save_names()

def remove_name(name):
    if name in names:
        names.remove(name)
        save_names()

def search_name(name):
    return name in names

def show_all_names():
    return sorted(names)

load_names()


add_name("Juan")
add_name("Maria")
add_name("Ana")
print(names)  
remove_name("Juan")
print(names)  
print(search_name("Maria"))  
print(show_all_names())  
