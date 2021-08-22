#population based on country name dic
population = { "china" : 143, 
                "india" : 136, 
                "usa" : 32, 
                "pakistan" : 21 }

# print the country name and population
def printall():
    for country_name in population:
        print(f"{country_name}==>{population[country_name]}")

# add the country name and population
def add():
    country_name = input("enter the country name : ")
    country_name = country_name.lower()
    if country_name not in population:
        country_population = int(input("enter the population of country : "))
        population[country_name] = country_population
        printall()  
    else:
        print("that it exist!")     

# remove the country name and population
def remove():
    country_name = input("enter the country name : ")
    country_name = country_name.lower()
    if country_name in population:
        del population[country_name]
        printall()
    else:
        print("that country doesn't exist!")

# query the country name and population
def query():
    country_name = input("enter the country name : ")
    country_name = country_name.lower()
    if country_name in population:
        print(f"{country_name}==>{population[country_name]}")
    else:
        print("that country doesn't exist!")  

# edit the country name and population
def edit():
    country_name = input("enter the country name : ")
    country_name = country_name.lower()
    if country_name in population:
        country_population = int(input("enter the population of country : "))
        population[country_name] = country_population
        printall()
    else:
        print("that country doesn't exist!")

# main function
def main():
    user_input = input('enter the input (print, add, remove, edit, and query) to continue : ')
    user_input = user_input.lower()
    if user_input == 'print':
        printall()
    elif user_input == 'add':
        add()
    elif user_input == 'remove':
        remove()
    elif user_input == 'query':
        query()     
    elif user_input == 'edit':
        edit()

# main block
if __name__ == '__main__':
    while True:
        main()
        user = input('enter the exit to quit or any button to continue : ')
        user = user.lower()
        if user == 'exit':
            print("application is exit!!!")
            break
        else:
            continue
        