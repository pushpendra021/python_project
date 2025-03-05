import requests
import json
import random
def fetch_random_user_from_freeapi():
    url="https://api.freeapi.app/api/v1/public/randomjokes?limit=10&query=science&inc=categories%2Cid%2Ccontent&page=1"
    response=requests.get(url)
    data=response.json()#convert string to json format
#     |
#     |
#     V
#data ke ander success present hai and data ke ander data hai to haam if ke under jayenge
    if data['success'] and "data" in data:
        user_data=data['data']
        user_limit=user_data["limit"]
        user_currentPageItems=user_data["currentPageItems"]
        jokes_list=user_data['data']

        if not jokes_list:
            raise Exception("No jokes found.")
        
        #select one random joke
        joke=random.choice(jokes_list)
        categories=joke['categories']
        content=joke["content"]


        

        
        return user_limit,user_currentPageItems,categories,content
    else:
        #raise the error
        raise Exception("Failed to fetch user data")





def main():
    try:
        user_limit,user_currentPageItems,categories,content=fetch_random_user_from_freeapi()
        print(f"Limit : {user_limit} \n currentPageItems: {user_currentPageItems} \n Categories: {categories} \n Content: {content}")

    except Exception as e:
        print(str(e))# used str because may be e have another format

if __name__=="__main__":
    main()
