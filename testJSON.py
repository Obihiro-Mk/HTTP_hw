from pprint import pprint
import requests
# hr = requests.get("https://superheroapi.com/api/2619421814940190/search/Hulk").json()
# for i in hr['results']:
#     if i['id'] == '332':
#         pprint(i['powerstats']['intelligence'])
# # pprint(hr)
def id_heroes(hero_list):

    for hero in hero_list:
        hero_u = requests.get("https://superheroapi.com/api/2619421814940190/search/" + hero).json()
        id = hero_u['results'][0]['id']
        print(hero, 'id:', id)
        # pprint(hero_u['results']['id'])
        # for id in hero_u['results'][0]:
        #     print(id['id'])
hr_list = ['Hulk', 'Captain America', 'Thanos']
id_heroes(hr_list)