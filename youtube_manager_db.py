import sqlite3
con = sqlite3.connect("youtube_videos.db")#The returned Connection object con represents the connection to the on-disk database.

#In order to execute SQL statements and fetch results from SQL queries, we will need to use a database cursor. Call con.cursor() to create the Cursor
cursor = con.cursor()

cursor.execute('''
create table if not exists videos(
            id INTEGER PRIMARY KEY,
            name TEXT NOT NULL,
            time TEXT NOT NULL
            
            )
''')

def list_all_videos():
    cursor.execute("select * from videos")#The cursor will hold onto any values that appear.
    for row in cursor.fetchall():
        print(row)

def add_video(name,time):
    cursor.execute("insert into videos (name,time) values (?,?)", (name,time))
    con.commit()

def update_video(video_id,new_name,new_time):
    cursor.execute("update videos set name=?,time=? where id=?",(new_name,new_time,video_id))
    con.commit()

def delete_video(video_id):
    cursor.execute("delete from videos where id=?",(video_id,))
    con.commit()

def main():
        
    while True:
        print("\n Youtube Manager with DATABASE| choose an option")
        print("1. List all youtube videos ")
        print("2. Add a youtube videos ")
        print("3. Update a youtube video details ")
        print("4. Delete a youtube videos ")
        print("5. Exit the app ")

        choice=input("Enter your choice: ")
        # print(videos)

        match choice:
            case '1':
                list_all_videos()
            case '2':
                name=input("Enter the video name : ")
                time=input("Enter the video time : ")
                add_video(name,time)

            case '3':
                video_id=input("Enter the ID to update")
                name=input("Enter the video name : ")
                time=input("Enter the video time : ")
                update_video(video_id,name,time)

            case '4':
                video_id=input("Enter the ID to delete : ")
                delete_video(video_id)
            case '5':
                break
            case _:
                print("Invalid choice")
    con.close()
 

if __name__=="__main__":
    main()