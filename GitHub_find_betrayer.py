import requests
from bs4 import BeautifulSoup
from concurrent.futures import ThreadPoolExecutor
import time
nickname = input("닉네임을 입력하세요: ")
page_cnt = 1
following_List = []
while True:
    url = f"https://github.com/{nickname}?page={page_cnt}&tab=following"
    response = requests.get(url)
    soup = BeautifulSoup(response.content, "html.parser")
    following_spans = soup.find_all("span", class_="Link--secondary")
    if len(following_spans) <= 0:
        break
    for following in following_spans:
        following_name = following.text.strip()
        following_List.append(following_name)
        print(following_name)
    page_cnt += 1

if following_List:
    print("GitHub에서 팔로잉한 사용자 목록:")
    for following in following_List:
        print(following)
    print("팔로잉 수 : ",len(following_List))
else:
    print("팔로잉한 사람이 없습니다.")
    print("닉네임을 제대로 입력하였습니까?")
    exit(1)
    
follower_List = []
page_cnt = 1
while True:
    url = f"https://github.com/{nickname}?page={page_cnt}&tab=followers"
    response = requests.get(url)
    soup = BeautifulSoup(response.content, "html.parser")
    followers_spans = soup.find_all("span", class_="Link--secondary")
    if len(followers_spans) <= 0:
        break
    for follower in followers_spans:
        follower_name = follower.text.strip()
        follower_List.append(follower_name)
        print(follower_name)
    page_cnt += 1


if follower_List:
    print("GitHub에서 나를 팔로우한 사람 목록:")
    for follower in follower_List:
        print(follower)
    print("팔로워 수 : ",len(follower_List))
else:
    print("나를 팔로우한 사람이 없습니다.")
    print("닉네임을 제대로 입력하였습니까?")
    exit(1)
    
    
Last_list = []
cnt = 0
for following in following_List:
    if following not in follower_List and requests.get(f"https://github.com/orgs/{following}/repositories").status_code == 404:
        print(following, "은 나를 팔로우하지 않았습니다.")
        cnt += 1
print("나를 팔로우 하지 않은 사람 수 : ", cnt)
        
    
    


# 잘못 생각하고 만들었는데 아까워서 주석으로 남겨둠.

# def make_request(user,page_count):
#     url = f"https://github.com/{user}?page={page_count}&tab=following"
#     detected_url = f"https://github.com/orgs/{user}/repositories"
#     if page_count == 1:
#         if requests.get(detected_url).status_code != 404:
#             return False
#     response = requests.get(url)
#     soup = BeautifulSoup(response.content, "html.parser")
#     following_spans = soup.find_all("span", class_="Link--secondary")
#     if len(following_spans) <= 0:
#         un_following_list.append(user)
#         return False
#     if f"{nickname}" in following_spans:
#         print(user,"은 나를 팔로우하였습니다.")
#         return True
#     page_count += 1

# un_following_list = [] #https://github.com/orgs/Nautilus-Institute/repositories
# users = []
# for user in following_List:
#     users.append(user)

# print("나를 팔로우 하지 않은 사람을 찾습니다.")
# print("팔로잉한 사람의 숫자가 많을수록 많은 시간이 소요될 수 있습니다.")
# executor = ThreadPoolExecutor()
# for user in users:
#     executor.submit(make_request, user,1)

# executor.shutdown(wait=True)

# print("나를 팔로우하지 않는 사람의 목록은 다음과 같습니다. (Organization은 감지 대상에서 제외됩니다.)")
# for un_follwer in un_following_list:
#     print(un_follwer)
# print("총 인원수 : ", len(un_following_list))
