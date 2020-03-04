from user import User
""" 
    #table of users
    users = [
        User(1, 'alice', 'coffee')
    ]

    #to get the username without iterating
    username_mapping = {
        u.username: u for u in users
    }
    userid_mapping = {
        u.id: u for u in users
    }
"""

def authenticate(username, password):
    """ user = username_mapping.get(username, None) #default value of you can't find this username """
    user = User.find_by_username(username) #can use the class now
    if user and user.password == password:
        return user

def identity(payload): #payload = contents of JWT token
    user_id = payload['identity']
    # return userid_mapping.get(user_id, None)
    return User.find_by_id(user_id)