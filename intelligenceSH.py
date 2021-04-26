
import requests

def id_heroes(hero_list):

    for hero in hero_list:
        hero_u = requests.get("https://superheroapi.com/api/2619421814940190/search/" + hero).json()
        id = hero_u['results'][0]['id']
        print(hero, 'id:', id)

def hero_intelligence(hero_list):

    hd = {}

    for hero in hero_list:
        hero_u = requests.get("https://superheroapi.com/api/2619421814940190/search/" + hero).json()
        for stats in hero_u['results']:
            if stats['id'] == '332' or stats['id'] == '149' or stats['id'] == '655':
                hd[hero] = stats['powerstats']['intelligence']
                print('intelligence -', hero + ':', hd[hero])

    sort_list = sorted(list(hd.items()), reverse=True)
    print("Самый умнный -", sort_list[0][0], 'с интелектом -', sort_list[0][1])


hr_list = ['Hulk', 'Captain America', 'Thanos']
id_heroes(hr_list)
hero_intelligence(hr_list)


