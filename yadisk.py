from pprint import pprint

import requests
tk = ''
f_l = 'C:\PyFiles\yadiskup.txt'
class YaUploader:
    def __init__(self, token):
        self.token = token

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

    def upload_file_to_disc(self, ya_file_path, path):
        href = self._get_upload_link(ya_file_path=ya_file_path).get('href', '')
        response = requests.put(href, data=open(path, 'rb'))
        response.raise_for_status()
        if response.status_code == 201:
            print('Success')

y = YaUploader(tk)
y.upload_file_to_disc('yadiskup.txt', 'C:\PyFiles\yadiskup.txt')
