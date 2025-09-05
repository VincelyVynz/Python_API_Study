# ------------------------------ API Study ------------------------------ #

"""
This script takes a name as input and uses three public APIs to predict:
- Age (Agify API)
- Gender (Genderize API)
- Nationality (Nationalize API)

It then prints out the predicted information based on the given name.
"""


import requests, pycountry

params = {
    "name" : input("Enter your name: ")
}

try:
    # Agify API
    agify_response = requests.get("https://api.agify.io", params= params)
    agify_response.raise_for_status()
    agify_data = agify_response.json()

    # Genderize API
    genderize_response = requests.get("https://api.genderize.io", params= params)
    genderize_response.raise_for_status()
    genderize_data = genderize_response.json()

    #Nationalize API
    nationalize_response = requests.get("https://api.nationalize.io", params= params)
    nationalize_response.raise_for_status()
    nationalize_data = nationalize_response.json()




    #print output
    print(f"Name: {agify_data['name']}\n"
          f"Average age: {agify_data['age']}\n"
          f"(Based on {agify_data["count"]} samples.)\n"
          f"Gender: {genderize_data['gender']}\n"
          f"(Based on {genderize_data['count']} samples.)")


    #Get country name
    country =  nationalize_data['country'][0]['country_id']
    country_name = pycountry.countries.get(alpha_2=country).name
    print(f"Possible Nationality: {country_name}")

    country_prob = nationalize_data['country'][0]['probability']
    print(f"Probability: {country_prob * 100:.2f}% ")
    print(f"(Based on {nationalize_data['count']} samples.)")


except requests.exceptions.RequestException as e:
    print(e)
