import requests
input_search = str(input("apiNumworkSearch: "))
url="http://localhost:3000/?q="

request = requests.get(url + input_search)
if request.status_code == 200:
    request1link = {"name": request.json()["data"][0]["name"], "link": request.json()["data"][0]["link"]}
    request2link = {"name": request.json()["data"][1]["name"], "link": request.json()["data"][1]["link"]}
    print(request1link["link"] + " |crée par: " + request1link["name"])
    print(request2link["link"] + " |crée pARGEar: " + request2link["name"])
elif request.status_code == 404:
    request_error = request.json()["data"]
    print(request_error + "pas de project trouvé")
elif request.status_code == 500:
    request_error = {"error": request.json()["error"], "message": request.json()["message"]}
    print("error 500 | " + request_error["error"] + " | " + request_error["message"])
else:
    request_error = {"codeError": request.json()["statusCode"],
                     "error": request.json()["error"],
                     "message": request.json()["message"]}
    print("error " + request_error["codeError"] + " | " + request_error["error"] + " | " + request_error["message"])