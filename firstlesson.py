import tweepy
import time
consumer_key = "JPysYKuFx7mkYmXgRDef7CprE"
consumer_secret = "0ZcxGmCQWugsBNPKqLC1j9W9zeBO0ghyUACDdRi1UQdbR4T0ki"
access_key = "1195429060861669377-YVOvHfys7vMqPLlmazuw5B2s9eMbSn"
access_secret = "FdMjgUZfGqvvj8leCc8tw2T42AkrRdoffsyus61ohqSNl"

print("Script is Running.....")

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_key, access_secret)
api = tweepy.API(auth, wait_on_rate_limit=True)



file_name = "followers.txt"
def store_followers(file_name):
    followers = api.followers_ids("Abubakr160", [-1])
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
        for i in updated_followers:
            if i not in ids:
                api.destroy_friendship(i)


while True:
    unfollow()
    time.sleep(10)
    store_followers(file_name)
    time.sleep(600)
    

    
