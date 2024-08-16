class User:
    def __init__(self,user_id,user_name) -> None:
        self.id = user_id
        self.username = user_name
        self.followers = 0
        self.following = 0
    
    def follow(self,user):
        user.followers += 1
        self.following += 1
    
user_1 = User('01','geiniune_enemey')
user_2 = User("02","naat_okay")

user_1.follow(user_2)

print(F"{user_1.username} followers: {user_1.followers}")
print(F"{user_1.username} following: {user_1.following}")
print(F"{user_2.username} followers: {user_2.followers}")
print(F"{user_2.username} following: {user_2.following}")