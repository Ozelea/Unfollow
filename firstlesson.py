import tweepy
import time
consumer_key = "XXXXXXXXXXXXXXXXXX"
consumer_secret = "XXXXXXXXXXXXXXXXXXXXXX"
access_key = "XXXXXXXXXXXXXXXXXXXXXXXXXXX"
access_secret = "XXXXXXXXXXXXXXXXXXXXXXXXXX"

username = "Enter Your User Name"
print("Script is Running.....")

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_key, access_secret)
api = tweepy.API(auth, wait_on_rate_limit=True)



file_name = "followers.txt"
def store_followers(file_name):
    followers = api.followers_ids(username, [-1])
    file_write = open(file_name, "w")
    for id in followers:
        file_write.write(str(id)+'\n')
    file_write.close()
    



def unfollow():
    updated_followers = api.followers_ids("Abubakr160", [-1])
    
    with open(file_name, "r") as f:
        idsStrings = f.read().split('\n')
        del idsStrings[-1]                               #delete last empty string generated
        ids = list(map(int, idsStrings))
        for i in ids:
            if i not in updated_followers:
                
                
                try:
                    user = api.get_user(i)
                    screen_name = user.screen_name
                    print("@" + screen_name)
                except Exception:
                    print("User Not Found")
while True:
    unfollow()
    time.sleep(10)
    store_followers(file_name)
    time.sleep(600)

    

    

    
