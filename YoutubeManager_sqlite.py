import sqlite3

conn = sqlite3.connect('youtube_videos_db')
cursor = conn.cursor()
cursor.execute(''' 
 Create table if not exists videos(
        id integer primary key, name text not null, time text not null)
''')

def list_all_videos():
    cursor.execute("Select * from videos")
    for row in cursor.fetchall():
        print(row)

def add_video(name,time):
    cursor.execute("Insert into videos (name,time) values (?,?)",(name,time))
    conn.commit()

def update_video(name,time,video_id):
    cursor.execute("Update videos set name=?,time =? where id=?",(name,time,video_id))
    conn.commit()

def delete_video(video_id):
    cursor.execute("Delete from videos where id=?",(video_id,))
    conn.commit()

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

    conn.close()            

if __name__=="__main__":
    main()