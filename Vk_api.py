import requests


class API:

    # url for get access_token https://oauth.vk.com/authorize?client_id=51629247&display=page&redirect_uri=https://oauth.vk.com/blank.html&scope='messages'&response_type=token&v=5.131

    @staticmethod
    def get_owner_id(access_token, GROUP_NAME, API_VERSION):
        url = f'https://api.vk.com/method/groups.getById?v={API_VERSION}&access_token={access_token}&group_id={GROUP_NAME}'
        response = requests.api.get(url)
        if response.status_code != 200:
            print(response.status_code)
            exit()
        data = response.json()
        owner_id = data['response'][0]['id']
        return str(owner_id)

    @staticmethod
    def get_info(access_token, owner_id, COUNT, API_VERSION):
        url = f'https://api.vk.com/method/wall.get?v={API_VERSION}&access_token={access_token}&owner_id={owner_id}&count={COUNT}'
        response = requests.api.get(url)
        if response.status_code != 200:
            print(response.status_code)
            exit()
        data = response.json()['response']['items']
        contents = list()
        for i in range(COUNT):
            contents.append(data[i]['text'])
        return contents
