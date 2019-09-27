import requests

BASE_URL = "http://127.0.0.1:5000"  # LOCAL HOST

links = ["/Introduction.html", "/Theory.html", "/Objective.html", "/Experiment.html", "/Quizzes.html", "/Procedure.html", "/Further Readings.html", "/Random_Test.html"]

for current in links:
    response = requests.get(BASE_URL + current)
    try:
        assert response.status_code == 200, current
        code = str(response.status_code)
        print(BASE_URL + current + ":")
        print("status code=" + code + "; Link is working fine!\n")

    except:
        code = str(response.status_code)
        print(BASE_URL + current + ":")
        print("status code=" + code + "; Link does not exist\n")
