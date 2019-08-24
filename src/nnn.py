'''
과외를 위해 만든 파일입니다.
과외 중 movelens 데이터를 활용한 무언가를 할 예정입니다.
'''
import csv

# 평균 계산
def avg(ratings):

    return sum(ratings) / len(ratings)

# ratings.csv 읽어들여 ratingList에 저장
raingFile = open('data/ratings.csv', 'r')

rdr = csv.reader(raingFile)

ratingList = [line for line in rdr]

raingFile.close()

# 영화의 고유한 id값만 불러옴
movieIdList = list(set([int(user[1]) for user in ratingList[1:]]))

movieIdList.sort()

movieIdList = movieIdList[:5]

# movies.csv 파일에서 영화 정보 불러옴 
movieFile = open('data/movies.csv', 'r')
movie = csv.reader(movieFile)

movieList = [line for line in movie]

movieFile.close()

# 특정 영화의 전체 평점을 구함
for movieId in movieIdList:
    # 전체 영화에서 특정 영화의 아이디 불러옴

    for mId in movieList: # movies.csv
        # 영화의 실제 데이터를 가지고 있는 파일을 한줄씩 불러옴
        if (mId[0]) == str(movieId):
            # 불러온 줄의 영화 아이디와 현재 영화의 id를 비교하여 일치한다면
            print(mId[1])
            # 해당 영화의 실제 이름을 출력함

############################################################################################

    userData = []

    for rateInfo in ratingList[1:]:
        # 전체 평점 정보를 읽어옴
        if rateInfo[1] == str(movieId):
            # 전체 평점 중 현재 체크 중인 영화의 아이디와 일치하는 평점 정보가 있을 경우 
            userData.append(rateInfo)
            # userData라는 리스트에 평점 정보를 넣어 줌
############################################################################################
    userRateList = []

    for rate in userData[:]:
        # 전체 평점 정보를 불러와 그 중 실제 점수만 float 형식으로 바꿔 넣어줌
        userRateList.append(float(rate[2]))

    # 전체 평점의 평균 계산 후 출력
    print(avg(userRateList))




# Q. 각 유저별 전체 영화의 평균 평점 구하기


# Q. 유저가 평점을 주는 경향 구하기
#    (후하게 주는지? 짜게 주는지? 아니면 일반적으로 주는지?)


# Q. 유저가 가장 점수를 좋게 준 영화 상위 5개 구하기
#    (sub Q1. 중복될땐 id로 정렬하여 상위 5개만 구하기)
#    (sub Q2. 중복될땐 중복되는 점수의 영화 모두 구하기)