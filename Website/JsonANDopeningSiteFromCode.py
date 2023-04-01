import requests
import json
from collections import defaultdict

r = requests.get("https://jsonplaceholder.typicode.com/todos")

def count_user_frequency(tasks):
    completedTasksFrequencyByUser = defaultdict(int)
    for entry in tasks:
        if (entry["completed"] == True):
           completedTasksFrequencyByUser[entry["userId"]] +=1
           
            
    return completedTasksFrequencyByUser


def get_user_with_top_completed_tasks(completedTasksFrequencyByUser):
    userIdWithMaxCompletedAmountOfTasks =[]

    maxAmountOfCompletedTask = max(completedTasksFrequencyByUser.values())

    for userId, numberOfCompletedTask in completedTasksFrequencyByUser.items():
        if (numberOfCompletedTask == maxAmountOfCompletedTask):
            userIdWithMaxCompletedAmountOfTasks.append(userId)
        
        return userIdWithMaxCompletedAmountOfTasks
    


try:
    tasks = r.json()
except json.decoder.JsonDecodeError:
    print("Niepoprawny format")
else:
    completedTaskFrequencyByUser = count_user_frequency(tasks)

    usersWithTopCompletedTasks = get_user_with_top_completed_tasks(completedTaskFrequencyByUser)
"""
#sposób 1

r = requests.get("https://jsonplaceholder.typicode.com/users")

users = r.json()

for user in users:
    if (user["id"] in usersWithTopCompletedTasks):
            print("Ciastko wendruje do urzytkownika o imieniu: ",user["name"])
            usersWithTopCompletedTasks.remove(user["id"])
        """

"""#sposób 2

for userId in usersWithTopCompletedTasks:

   # r = requests.get("https://jsonplaceholder.typicode.com/users/",+ str(userId))
    r = requests.get("https://jsonplaceholder.typicode.com/users/",params = "id" + str(userId))
    user = r.json()

    print("Ciastko dostaje osoba o imieniu", user[0]("name"))"""

#sposób 3

def change_list_into_conj_of_param(my_list,key = "id"):

    conj_param = key = "id="


    lastIterationOfList = len(my_list)
    i = 0
    for item in my_list:
        i += 1

        if (i == lastIterationOfList):
            conj_param += str(item)
        else:    
            conj_param += str(item) +"&" + key +"="
    
    return conj_param


conj_param = change_list_into_conj_of_param(usersWithTopCompletedTasks)

r = requests.get("https://jsonplaceholder.typicode.com/users/",params = conj_param)

users = r.json()

for user in users:
    print("ciastko",user)