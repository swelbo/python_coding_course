# call a dictinary 
programming_dictionary = {
    "Bug": "An error in a program that prevents the program from running as expected.", "Function": "A piece of code that you can easily call over and over again." 
}

# Retrieving items from dictionary
print(programming_dictionary["Bug"])

# Adding new items to dictionary
programming_dictionary["Loop"] = "yes"

# dictionary of countries and cities


# example of a nested dictionary - list inside a dictionary
travel_log = {
    "France": ["Paris", "Lille", "Dijon"],
    "Germany": ["Berlin", "Hamburg", "Stuttgart"]
}

# example of a nested dictionary - dict inside dict
travel_log = {
    "France": {
        "cities_visited": ["Paris", "Lille", "Dijon"], 
        "total_visits": 12, 
        "total_spend": 1000
        },
    "Germany": {
        "cities_visited": ["Berlin", "Hamburg", "Stuttgart"],
        "total_visits": 5,
        "total_spend": 700
        }
}
    
print(travel_log["France"]["total_spend"])
print(travel_log["Germany"]["cities_visited"])

# example of a nested dictionary - dict inside a list
travel_log = [
    {
    "country": "France", 
    "cities_visited": ["Paris", "Lille", "Dijon"], 
    "total_visits": 12, 
    "total_spend": 1000
    },
    
    {
    "country": "Germany", 
    "cities_visited": ["Berlin", "Hamburg", "Stuttgart"],
     "total_visits": 5,
     "total_spend": 700
     },
]
