import requests

def fetch_animal_data(animal_name):
  """ getting the data from Ninja (API) """
  api_url = f'https://api.api-ninjas.com/v1/animals?name={animal_name}'
  headers = {'X-Api-Key':'JnqwfRQPkiJd2aEYbutx8uzZ7Ze3UZNkyhRak64T'}
  response = requests.get(api_url, headers=headers)

  if response.status_code == 200:
      return response.json()
  else:
      print(f"Fehler: {response.status_code}")
      return []

# Milestone 1: "Fox"
animals_data = fetch_animal_data("Fox")


for animal in animals_data:
    output += '<li class="cards__item">'
    # Name prüfen und ausgeben
    if "name" in animal:
        output += f"  <div class='card__title'>{animal['name']}</div>\n"

    output += '  <p class="card__text">\n'

    #Diet prüfen und Achtung! *(liegt innerhalb von 'characteristics')
    if "characteristics" in animal and "diet" in animal["characteristics"]:
        output += f"<strong>Diet:</strong> {animal['characteristics']['diet']}<br/>\n" #<--- *

    #Location prüfen *(erstes Element der Liste 'locations')
    if "locations" in animal and len(animal["locations"]) > 0:
        output += f"<strong>Location:</strong> {animal['locations'][0]}<br/>\n" #* [0] = erstes Element

    #Type prüfen (liegt auch in 'characteristics')
    if "characteristics" in animal and "type" in animal["characteristics"]:
        output += f"<strong>Type:</strong> {animal['characteristics']['type']}<br/>\n"

    output += '</li>\n'



print(output)

with open("animals_template.html", "r", encoding="utf-8") as f:
    template_content = f.read()

new_html_content = template_content.replace("__REPLACE_ANIMALS_INFO__", output)

with open("animals.html", "w", encoding="utf-8") as f:
    f.write(new_html_content)