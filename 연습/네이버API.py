import requests
from pymongo import MongoClient
client = MongoClient('localhost', 27017)
db = client.prac


client_id = "ZUPIuFn5lLD_szUdXcao"
client_secret = "dcsdSoNnRY"


# Open API 검색 요청 개체 설정
header = {'X-Naver-Client-Id':client_id, 'X-Naver-Client-Secret':client_secret}
search_receive = '해리포터마법사의돌'

url = f"https://openapi.naver.com/v1/search/book.json?query={search_receive}&display=1"
res = requests.get(url, headers=header)
datalist = res.json()['items']


for data in datalist:
    title = data['title']
    image = data['image']
    link = data['link']
    # print (title, image, link)

    dic = {
        'title': title,
        'image': image,
        'link':link
    }
    db.prac.insert_one(dic)
    print(dic)



# get
# results = list(db.lovelist.find({}, {'_id': False}))
# for result in results:
    # print(result['title'])
    # for문을 돌려 나온 값 result의 ['listTitle']을 출력한다