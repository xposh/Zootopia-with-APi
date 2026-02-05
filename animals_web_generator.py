import data_fetcher

def main():

    animal_name = input("Enter a name of an animal: ")
    animals_data = data_fetcher.fetch_data(animal_name) #Python gehe in das Modul data_fetcher und führe dort die Funktiom fetch-data aus.
    #user_animal_search = fetch_animal_data(input("Which animal are you looking for? "))

    output = ""

    # (Milestone 3)
    if not animals_data:
        # Falls die Liste leer ist, wird diese Meldung in das HTML geschrieben
        output = f"<h2>The animal '{animal_name}' doesn't exist.</h2>"
    else:
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

            output += '  </p>\n'
            output += '</li>\n'




    with open("animals_template.html", "r", encoding="utf-8") as f:
        template_content = f.read()

    new_html_content = template_content.replace("__REPLACE_ANIMALS_INFO__", output)

    with open("animals.html", "w", encoding="utf-8") as f:
        f.write(new_html_content)

    print(f"Website was successfully generated to the file animals.html for: {animal_name}")

if __name__ == "__main__":
    main()