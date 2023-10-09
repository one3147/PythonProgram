from github import Github
import time

access_token = "깃허브 액세스 토큰"
repository_name = "레포지토리 이름"
file_name = "파일명, 미리 생성 해야함"


cnt = int(input("커밋 수를 입력하세요.\n>>>>"))
print(f"{cnt}커밋을 시작합니다. 시간이 소요될 수 있습니다..")


g = Github(access_token)
repo = g.get_user().get_repo(repository_name)


start_time = time.time()
for i in range(1, cnt + 1):
    file = repo.get_contents(file_name)
    repo.delete_file(file.path, f"Remove {file_name}", file.sha)
    repo.create_file(file_name, f"Create {file_name}",f"Commit King {i}")
    print(f"{i} 커밋 완료!")
    time.sleep(2)# commit이 서버에 적용되는 시간차를 고려한 대기 시간
    
end_time = time.time()
commit_time = end_time - start_time
print(f"{cnt}커밋 완료, 소요 시간 : {commit_time}")

