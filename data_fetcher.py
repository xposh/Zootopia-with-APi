import requests


API_KEY = 'JnqwfRQPkiJd2aEYbutx8uzZ7Ze3UZNkyhRak64T'

def fetch_data(animal_name):
    """
    Fetches the animals data for the animal 'animal_name'.
    Returns: a list of animals, each animal is a dictionary.
    """
    api_url = f'https://api.api-ninjas.com/v1/animals?name={animal_name}'
    headers = {'X-Api-Key': API_KEY}
    response = requests.get(api_url, headers=headers)

    if response.status_code == 200:
        return response.json()
    else:
        print(f"Fehler: {response.status_code}")
        return []

