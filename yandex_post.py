import requests


class YaUploader:
    def __init__(self, token: str):
        self.token = token

    def _get_href(self, file_path):
        upload_url = 'https://cloud-api.yandex.net/v1/disk/resources/upload'
        headers = {
            'Content-Type': 'application/json',
            'Authorization': 'OAuth {}'.format(self.token)
        }
        params = {'path': file_path, 'overwrite': 'true'}
        response = requests.get(upload_url, headers=headers, params=params)
        return response.json()["href"]

    def upload(self, file_path):
        response = requests.put(self._get_href(file_path), data=open(file_path, 'rb'))
        response.raise_for_status()
        if response.status_code == 201:
            print("Succes")


if __name__ == '__main__':
    path_to_file = "test.txt"
    token = "TOKEN"
    uploader = YaUploader(token)
    uploader.upload(path_to_file)
