import requests


def movie_recommendations(age, gender):
    url = "https://streaming-availability.p.rapidapi.com/search/basic"
    movies_list = []
    genre = []
    if age == "0-2" or age == "4-6" or age == "8-12":
        genre = ["14", "16"]
    elif age == "15-20":
        if gender == "Male":
            genre = ["3", "5", "18", "27", "28", "80"]
        else:
            genre = ["10749", "10764"]
    else:
        if gender == "Male":
            genre = ["1", "5", "27", "28", "80", "10752", "10763", "10767"]
        else:
            genre = ["4", "14", "18", "35", "10749", "10751", "10764", "10763", "10767"]
    for i in range(7):
        querystring = {"country": "us", "service": "netflix", "type": "movie", "genre": genre, "page": str(i + 1),
                       "language": "en"}
        headers = {
            'x-rapidapi-host': "streaming-availability.p.rapidapi.com",
            'x-rapidapi-key': "cbc32de3e5msh7f292422092efcdp15d9bdjsnb45a67bf4723"
        }
        response = requests.request("GET", url, headers=headers, params=querystring)
        age_split = age.split('-')
        if int(age_split[0]) >= 18:
            age_split[0] = 18
            age_split[1] = 100
        for j in response.json()["results"]:
            if int(age_split[0]) <= (j["age"]) <= int(age_split[1]):
                movies_list.append(j["posterURLs"]["original"])

    return movies_list
