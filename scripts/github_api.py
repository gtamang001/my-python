# this is script to call github api using python to extrac the details of the github data
# use this to call api for getting the list of repos for certain code snippet
from http.client import ResponseNotReady
from urllib import response
from wsgiref import headers
import requests
import base64
import xml.etree.ElementTree as xml
from re import serach
import csv

# variables 
count = 0
repos_n_url = {}
repos = []

# define headers 
headers = {"Authorization": f"Bearer <token-string>", "content-type": "application/json"}
string_search_api_url= f"https://api.github.com/search/code?q=Maven+POM&q=in%3Afile+filename%3Apom.xml+libs-release-local&type=code"
reponse = requests.get(string_search_api_url, headers=headers)
response_json = request.json()
data = response_json["items"]

# iterate through the data this only give the firs  page 
for entry in data:
    repos_n_url[entry["repository"]["name"]]= entry["repository"]["html_url"]

# for multipage search
while response.links['next']['url'] != response.links['last']['url']:
    print(response.links)['next']['url']
    response = requests.get(response.links['next']['url'], headers=headers)
    response_json = response.json()
    data = response_json["item"]

    for entry in data:
        repos_n_url[entry["repository"]["name"]]= entry["repository"]["html_url"]

# print the length of it 
print(len(repos_n_url))

# Second part 

