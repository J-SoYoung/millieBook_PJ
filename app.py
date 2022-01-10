from flask import Flask, render_template, jsonify, request, json
from bson import json_util

app = Flask(__name__)

import requests
from bs4 import BeautifulSoup

from pymongo import MongoClient
# client = MongoClient('localhost', 27017)
client = MongoClient('mongodb://test:test@localhost', 27017)
db = client.millie


## html 주는 부분
@app.route('/')
def home():
    return render_template('index.html')

@app.route('/bookReview')
def bookReview():
    return render_template('book-review.html')

@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/regist')
def regist():
    return render_template('regist.html')


## API 역할을 하는 부분
@app.route('/book', methods=['GET'])
def listing():
    type_receive = request.args.get('type_give')
    booklist = []

    if type_receive == 'novel':
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}
        data = requests.get(
            'http://book.interpark.com/display/collectlist.do?_method=BestsellerHourNew201605&bestTp=1&dispNo=028005',
            headers=headers)  # 소설url
        html = data.text
        soup = BeautifulSoup(html, 'html.parser')

        books = soup.select(
            '#content > div.rankBestWrapper > div.rankBestContainer > div.rankBestContents > div > div.rankBestContentList > ol > li')

        for book in books:
            title = book.select_one(' div > a > div.itemName > strong').text
            img = book.select_one('div > div.cover > div.coverImage > label > a > img').get('src')
            writer = book.select_one('div > a > div.itemMeta > span.author').text
            url = (book.select_one('div > a')).get('href')

            dic = {
                'img': img, 'title': title, 'writer': writer, 'url': (f"http://book.interpark.com{url}")}

            booklist.append(dic)
            # print(booklist)

        return jsonify({'booklist': booklist})

    if type_receive == 'humanities':
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}
        data = requests.get(
            'http://book.interpark.com/display/collectlist.do?_method=BestsellerHourNew201605&bestTp=1&dispNo=028013',
            headers=headers)  # 인문url
        html = data.text
        soup = BeautifulSoup(html, 'html.parser')

        books = soup.select(
            '#content > div.rankBestWrapper > div.rankBestContainer > div.rankBestContents > div > div.rankBestContentList > ol > li')

        for book in books:
            title = book.select_one(' div > a > div.itemName > strong').text
            img = book.select_one('div > div.cover > div.coverImage > label > a > img').get('src')
            writer = book.select_one('div > a > div.itemMeta > span.author').text
            url = (book.select_one('div > a')).get('href')

            dic = {
                'img': img, 'title': title, 'writer': writer, 'url': (f"http://book.interpark.com{url}")}

            booklist.append(dic)
            # print(booklist)

        return jsonify({'booklist': booklist})

    if type_receive == 'poem':
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}
        data = requests.get(
            'http://book.interpark.com/display/collectlist.do?_method=BestsellerHourNew201605&bestTp=1&dispNo=028037',
            headers=headers)  # 시url
        html = data.text
        soup = BeautifulSoup(html, 'html.parser')

        books = soup.select(
            '#content > div.rankBestWrapper > div.rankBestContainer > div.rankBestContents > div > div.rankBestContentList > ol > li')

        for book in books:
            title = book.select_one(' div > a > div.itemName > strong').text
            img = book.select_one('div > div.cover > div.coverImage > label > a > img').get('src')
            writer = book.select_one('div > a > div.itemMeta > span.author').text
            url = (book.select_one('div > a')).get('href')

            dic = {
                'img': img, 'title': title, 'writer': writer, 'url': (f"http://book.interpark.com{url}")}

            booklist.append(dic)
            # print(booklist)

        return jsonify({'booklist': booklist})



@app.route('/search', methods=['POST'])
def search():
    search_receive = request.form['search_give']
    comment_receive = request.form['comment_give']

    client_id = "ZUPIuFn5lLD_szUdXcao"
    client_secret = "dcsdSoNnRY"

    # Open API 검색 요청 개체 설정
    header = {'X-Naver-Client-Id': client_id, 'X-Naver-Client-Secret': client_secret}
    url = f"https://openapi.naver.com/v1/search/book.json?query={search_receive}&display=1"
    res = requests.get(url, headers=header)
    datalist = res.json()['items']

    for data in datalist:
        title = data['title']
        image = data['image']
        link = data['link']
        author = data['author']

        # print (title, image, link)

        dic = {
            'title': title,
            'image': image,
            'link': link,
            'author': author,
            'comment' : comment_receive
        }
        db.millieDB.insert_one(dic)
        print(dic)

    return jsonify({'result': 'DB저장'})


@app.route('/search', methods=['GET'])
def review():
    result = list(db.millieDB.find({}, {'_id': False}))
    print(result)

    return jsonify({'msg':'success', 'result': result})



if __name__ == '__main__':
    app.run('0.0.0.0', port=5000, debug=True)

