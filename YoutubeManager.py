import json
import time

def load_data():
    try:
        with open('youtube.txt','r') as file:
            test = json.load(file)
            return test
    except FileNotFoundError:
        return []


def save_data_helper(videos):
    with open('youtube.txt','w') as file:
        json.dump(videos,file)


def list_all_videos(videos):
    print("\n")
    print("*"*50)
    for ind,vid in enumerate(videos,start=1):
        print(f"{ind}: Name : {vid['name']}, Duration : {vid['time']}")

    time.sleep(3)


def add_video(videos):
    name = input("Enter video name: ")
    time = input("Enter video time: ")

    videos.append({'name':name,'time':time})
    save_data_helper(videos)


def update_video(videos):
    list_all_videos(videos)
    index = int(input("Enter the video number that you want to update: "))

    if 1<=index<=len(videos):
        name = input("Enter the new video name: ")
        time = input("Enter the new video duration: ")
        videos[index-1] = {"name":name,"time":time}
        save_data_helper(videos)
    else :
        print("Invalid index selected")    

def delete_video(videos):
    list_all_videos(videos)
    index = int(input("Enter the video number to be deleted: "))

    if 1<=index<=len(videos):
        del videos[index-1]
        save_data_helper(videos)
    else :
        print("Invalid index selected")   


def main():
    videos = load_data()
    while True:
        print('\n')
        print("*"*40)
        print("\n \tYouTube Manager\n")
        print("*"*40)
        print("\nChoose an Option\n")
        print("1. List a Favourite Video")
        print("2. Add a Youtube Video")
        print("3. Update Youtube Video details")
        print("4. Delete a Youtube Video")
        print("5. Exit the app")
        
        choice = input("Enter the choice: ")
        match choice:
            case '1':
                list_all_videos(videos)

            case '2':
                add_video(videos)  

            case '3':
                update_video(videos)     

            case '4':
                delete_video(videos)    

            case '5':
                break

            case _:
                print("Invalid Choice")


if __name__ == "__main__":
    main()                