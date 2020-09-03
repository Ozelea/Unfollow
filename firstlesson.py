import tweepy
import time
consumer_key = "XXXXXXXXXXXXXXXXXX"
consumer_secret = "XXXXXXXXXXXXXXXXXXXXXX"
access_key = "XXXXXXXXXXXXXXXXXXXXXXXXXXX"
access_secret = "XXXXXXXXXXXXXXXXXXXXXXXXXX"

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_key, access_secret)
api = tweepy.API(auth, wait_on_rate_limit=True)

username =  #Enter You user name here
print("Script is Running.....")

file_name = "followers.txt"
def store_followers(file_name):
    followers = api.followers_ids(username, [-1])
    file_write = open(file_name, "w")
    for id in followers:
        file_write.write(str(id)+'\n')
    file_write.close()


file_name1 = "unfollower.txt"
def unfollowers(file_name1, unfollower):
    file_write1 = open(file_name1, "a")
    file_write1.write('https://twitter.com/' + str(unfollower) + '\n')
    file_write1.close	




def unfollow():
    updated_followers = api.followers_ids(username, [-1])
    
    with open(file_name, "r") as f:
        idsStrings = f.read().split('\n')
        del idsStrings[-1]                               
        ids = list(map(int, idsStrings))
        for i in ids:
            if i not in updated_followers:


                
                try:
                    user = api.get_user(i)
                    screen_name = user.screen_name
                    print("@" + screen_name)
                    unfollowers(file_name1, screen_name)
                  
                except Exception:
                    error_msg = "User Not Found"
                    unfollowers(file_name1, error_msg)

unfollow()    
time.sleep(2)
store_followers(file_name)
