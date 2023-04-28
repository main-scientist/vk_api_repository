from Vk_api import API
from Convert_xlsx import Convert_xlsx
from Format_Content import Format_Content

if __name__ == '__main__':
    access_token = 'vk1.a.9V1vs3-QFHMthAsekcR0PQSOHqr2sx7o6ZZU0-Pu0eAF2pm62Sl9YOvUdRsD4JUMRmN9o4kdnqET8Y9UzqYOtPYLTVXBGCActdv8txnXI8p1WyFRH3s-7Hx6g5hnQIEgD2ps0VFcpUFdAdLn-DPiN3Zo0l92rlrfyc0N-kHmq-XwMnmkwfKRBRF1ECrlfQ-B&expires_in=86400'
    GROUP_NAME = 'donday_volgodonsk'
    API_VERSION = '5.81'
    owner_id = '-' + API.get_owner_id(access_token, GROUP_NAME, API_VERSION)
    COUNT = 100
    contents = API.get_info(access_token, owner_id, COUNT, API_VERSION)

    formatted_contents = list()
    for content in contents:
        formatted_contents.append(Format_Content.formatting_volgodonsk(content))

    Convert_xlsx.create_xlsx_by_list(formatted_contents)
