import json

def load_data():
    try:
        with open('youtube.txt','r') as file:
            test=json.load(file) #It will go into the file, extract data from there, and convert it into JSON.
            # print(test)
            # print(type(test))
            return test

    except (FileNotFoundError, json.JSONDecodeError):
        return []



def save_data_helper(videos):
    with open('youtube.txt','w') as file:
        json.dump(videos,file)#dump takes 2 parameter what write and where write
        



def list_all_videos(videos):
    print("\n")
    print("*" * 50)
    #It is used to iterate over an iterable (like a list) while keeping track of the index. 
    for index,video in enumerate(videos,start=1):
        print(f"{index}. {video['name']}, Duration:{video['time']}")
    print("\n")
    print("*" * 50)
 


def add_video(videos):
    name=input("Enter video name: ")
    time=input("Enter video time: ")
    #[{'name':name,'time':time}]
    videos.append({'name':name,'time':time})
    save_data_helper(videos)



def update_video(videos):
    # First, we should know the entire list.
    # Second, we need to know which index (video number) to update.
    # The index should be valid.
    # Take the name and time as input and update them at that index.
    list_all_videos(videos)
    index=int(input("Enter the video number to update: "))
    if 1<=index<=len(videos):
        name=input("Enter the new video name: ")
        time=input("Enter the new video time: ")
        #index-1 because user start indexinf from 1
        videos[index-1]={'name':name,'time':time}
        save_data_helper(videos)
    else:
        print("Invalid video index selected")




def delete_video(videos):
    # First, we should know the entire list.
    # Second, we need to know which index (video number) to delete.
    # The index should be valid.
    list_all_videos(videos)
    index=int(input("Enter the video number to be deleted: "))
    if 1<=index<=len(videos):
        del videos[index-1]
        save_data_helper(videos)
    else:
        print("Invalid video index selected")





def main():
    videos=load_data()
        
    while True:
        print("\n Youtube Manager | choose an option")
        print("1. List all youtube videos ")
        print("2. Add a youtube videos ")
        print("3. Update a youtube video details ")
        print("4. Delete a youtube videos ")
        print("5. Exit the app ")

        choice=input("Enter your choice: ")
        # print(videos)

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
                print("Invalid choice")



if __name__=="__main__":
    main()  