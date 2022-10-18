from urllib import response
import requests
 
if __name__=='__main__':
    url='https://25hi3sjce7.execute-api.us-east-1.amazonaws.com/marketplace/v1/Login/SignIn'
    response=requests.get(url)
    if response.status_code==200:
        print(response.content)