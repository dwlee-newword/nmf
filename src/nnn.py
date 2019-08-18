'''
과외를 위해 만든 파일입니다.
과외 중 movelens 데이터를 활용한 무언가를 할 예정입니다.
'''
import csv


raingFile = open('data/ratings.csv', 'r')
rdr = csv.reader(raingFile)

ratingList = []

for line in rdr:
    ratingList.append(line)

raingFile.close()


rateList = []

for rate in ratingList[1:]:
    rateList.append(rate)

movieIdList = list(set([int(user[1]) for user in ratingList[1:]]))

movieIdList.sort()

movieIdList = movieIdList[:5]

def avg(ratings):

    return sum(ratings) / len(ratings)

movieFile = open('data/movies.csv', 'r')
movie = csv.reader(movieFile)

movieList = []

for line in movie:
    movieList.append(line)

movieFile.close()

movieName =''

for movieId in movieIdList:

    for mId in movieList: # movies.csv
        if (mId[0]) == str(movieId):
            print(mId[1])

############################################################################################
############################################################################################

    userData = []

    for rateInfo in ratingList[1:]:
        if rateInfo[1] == str(movieId):
            userData.append(rateInfo)
############################################################################################
############################################################################################

    
    userRateList = []

    for rate in userData[:]:
        userRateList.append(float(rate[2]))


    print(avg(userRateList))