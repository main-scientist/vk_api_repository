import requests
import xlsxwriter
import json


# url for get access_token https://oauth.vk.com/authorize?client_id=51629247&display=page&redirect_uri=https://oauth.vk.com/blank.html&scope='messages'&response_type=token&v=5.131


def get_owner_id(access_token, GROUP_NAME, API_VERSION):
    url = f'https://api.vk.com/method/groups.getById?v={API_VERSION}&access_token={access_token}&group_id={GROUP_NAME}'
    response = requests.api.get(url)
    data = response.json()
    owner_id = data['response'][0]['id']
    return str(owner_id)


def get_info(access_token, owner_id, COUNT, API_VERSION):
    url = f'https://api.vk.com/method/wall.get?v={API_VERSION}&access_token={access_token}&owner_id={owner_id}&count={COUNT}'
    response = requests.api.get(url)
    data = response.json()['response']['items']
    contents = list()
    for i in range(COUNT):
        contents.append(data[i]['text'])
    return contents
    # print(data['response']['items'][0]['text'])
    # formatted_json = json.dumps(data, indent=2, ensure_ascii=False)
    # print(formatted_json)


if __name__ == '__main__':
    access_token = 'vk1.a.9V1vs3-QFHMthAsekcR0PQSOHqr2sx7o6ZZU0-Pu0eAF2pm62Sl9YOvUdRsD4JUMRmN9o4kdnqET8Y9UzqYOtPYLTVXBGCActdv8txnXI8p1WyFRH3s-7Hx6g5hnQIEgD2ps0VFcpUFdAdLn-DPiN3Zo0l92rlrfyc0N-kHmq-XwMnmkwfKRBRF1ECrlfQ-B&expires_in=86400'
    GROUP_NAME = 'donday_volgodonsk'
    API_VERSION = '5.81'
    owner_id = '-' + get_owner_id(access_token, GROUP_NAME, API_VERSION)
    COUNT = 5
    contents = get_info(access_token, owner_id, COUNT, API_VERSION)

    workbook = xlsxwriter.Workbook('Data.xlsx')
    worksheet = workbook.add_worksheet()

    row = 0
    col = 0
    for text in contents:
        worksheet.write(row, col, text)
        row += 1
    workbook.close()


