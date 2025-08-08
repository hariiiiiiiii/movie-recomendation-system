
url = "https://api.themoviedb.org/3/movie/285/images"

headers = {
    "accept": "application/json",
    "Authorization": "Bearer eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiI1MzU4Mzc5OWYyNDhhZTY2Nzg4ZTFlZjM3NWFmM2RkMyIsIm5iZiI6MTc1NDM4NTgwNy45OSwic3ViIjoiNjg5MWNkOGYzNWQxMDY4ZGNmNzcyOGMyIiwic2NvcGVzIjpbImFwaV9yZWFkIl0sInZlcnNpb24iOjF9.fiyk9TvCsODgd6VunEer8tECQOc7Om0WlU85xmwcYAg"
}

response = requests.get(url, headers=headers)

print(response.text)