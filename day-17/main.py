class User:
    def __init__(self, user_id, username):
        print("Hello")
        self.id = user_id
        self.username = username
        self.followers = 0 
        

user_1 = User("001", "Dachs")
user_2 = User("002", "Tom")

# user_1.id = "001"
# user_1.username = "thomas"

print(user_1.id)
print(user_1.username)
print(user_1.followers)

print(user_2.id)
print(user_2.username)
print(user_2.followers)

