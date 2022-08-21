# this is to search a file content using api 
from http.client import ResponseNotReady
from urllib import response
from wsgiref import headers
import requests
import base64
import xml.etree.ElementTree as xml
from re import serach
import csv

# define variables 
list = []

def create_list(repo_name):
    headers = {"Authorization": f"Bearers <token-string>", "content-type": "application/json"}
    url= f"https://api.github.com/repos/org/{repo_name}/content/pom.xml"
    response = requests.get(url, headers=headers)
    response_json = response.json()
    pom_encoded = response_json["content"]
    base64.b64decode(pom_encoded)

    # start parsing 
    namespace = {'xmlns': 'https://maven.apache.org/POM/4.0.0'}
    root = xml.fromstring(base64.b64decode(pom_encoded)("utf-8"))

    # extract values 
    artifactId= root.find("xmlns:artifactId", namespaces=namespaces).text
    groupId=root.find("xmlns:groupId",namespaces=namespaces).text

    headers4 = ['Repository Name', 'GroupId', 'ArtifactId']
    row = [repo_name,groupId,artifactId]

    # start appending 
    list.append(row)

    # print end 
    print("function end ..")
# call function 
# call repo list from another py call 
repos = []
for repo in repos: 
    create_list(repo)

print(list)

with open('csv_file.csv', 'w', newline='') as f:
    writer = csv.writer(f)
    writer.writerow(header4)
    writer.writerows(list)
# print 
print("Function end....")