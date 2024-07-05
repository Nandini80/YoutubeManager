# install pip install pymongo before using 
from pymongo import MongoClient
from bson import ObjectId
# ytManager is database name(write anything after /)
# client = MongoClient("mongodb+srv://youtubepy:youtubepy@cluster0.jba2kv0.mongodb.net/ytManager")
# or

client = MongoClient("mongodb+srv://youtubepy:youtubepy@cluster0.jba2kv0.mongodb.net/",tlsAllowInvalidCertificates = True)
db = client["ytManager"]

video_collection = db["videos"]
print(video_collection) #connect should be True


def list_all_videos():
    for video in video_collection.find():
        print(f"ID : {video['_id']}, Name: {video["name"]}, Time: {video['time']}")

def add_video(name,time):
    video_collection.insert_one({"name":name,"time":time })

def update_video(name,time,video_id):
    video_collection.update_one(
        # kisko update krna hai
        {'_id':ObjectId(video_id)},
        # kya set/update krna hai
        {'$set': {"name":name,"time":time}}
    )

def delete_video(video_id):
    video_collection.delete_one({'_id':ObjectId(video_id)})


def main():
    while True:
        print('\n')
        print("*"*40)
        print("\n \tYouTube Manager with DB\n")
        print("*"*40)
        print("\nChoose an Option\n")
        print("1. Check all Favourite Videos")
        print("2. Add a Youtube Video")
        print("3. Update Youtube Video details")
        print("4. Delete a Youtube Video")
        print("5. Exit the app")
        
        choice = input("Enter the choice: ")
        match choice:
            case '1':
                list_all_videos()

            case '2':
                name = input("Enter video name : ")
                time = input("Enter video duration : ")
                add_video(name,time)

            case '3':
                video_id = input("Enter the video index to be updated : ")
                name = input("Enter new video name : ")
                time = input("Enter new video duration : ")
                update_video(name,time,video_id)   

            case '4':
                video_id = input("Enter the video index to be updated : ")
                delete_video(video_id)    

            case '5':
                break

            case _:
                print("Invalid Choice")


if __name__ == "__main__":
    main()
