from pprint import pprint

import requests
tk = ''
f_l = ['yadiskup.txt', 'Ght.txt']

class YaUploader:
    def __init__(self, token, file_list):
        self.token = token
        self.file_list = file_list

    def get_headers(self):
        return {
            'Content-Type': 'application/json',
            'Authorization': 'OAuth {}'.format(self.token)
        }

    def _get_upload_link(self, ya_file_path):
        upload_url = "https://cloud-api.yandex.net/v1/disk/resources/upload"
        headers = self.get_headers()
        params = {"path": ya_file_path, "overwrite": "true"}
        response = requests.get(upload_url, headers=headers, params=params)
        pprint(response.json())
        return response.json()

    def upload_file_to_disc(self):
        for i in self.file_list:
            href = self._get_upload_link(ya_file_path=i).get('href', '')
            with open(i, 'rb') as f:
                response = requests.put(href, data=f)
                response.raise_for_status()
                if response.status_code == 201:
                    print('Success')

y = YaUploader(tk, f_l)
y.upload_file_to_disc()
