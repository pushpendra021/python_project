import requests
import json
def fetch_random_user_from_freeapi():
    url="https://api.freeapi.app/api/v1/public/randomusers/user/random"
    response=requests.get(url)
    data=response.json()#convert string to json format
#     |
#     |
#     V
#data ke ander success present hai and data ke ander data hai to haam if ke under jayenge
    if data['success'] and "data" in data:
        user_data=data['data']
        username=user_data["login"]["username"]
        country=user_data['location']['country']
        return username,country
    else:
        #error ko raise karta hai
        raise Exception("Failed to fetch user data")





def main():
    try:
        username,countary=fetch_random_user_from_freeapi()
        print(f"User name : {username} \n Countary: {countary}")

    except Exception as e:
        print(str(e))# used str because may be e have another format

if __name__=="__main__":
    main()
