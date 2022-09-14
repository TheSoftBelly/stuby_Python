import requests
from bs4 import BeautifulSoup

BASE_URL = 'https://www.thebell.co.kr/free/content/article.asp?page=1&svccode=00'
res = requests.get(BASE_URL)
soup= BeautifulSoup(res.text , 'html.parser')
asideBox = soup.select('#contents > div.contentSection > div > div.asideBox > div.bestBox.tp2 > div > ul > li > ul > li > a')
asideBox_all_titles=[]
asideBox_hrefs = []
asideBox_results = []
asideBox_call_hrefs = soup.find_all('a', class_='txtE')
for asideBox_href in asideBox_call_hrefs:
    asideBox_hrefs.append('https://www.thebell.co.kr/'+asideBox_href.attrs['href'])
for asideBox_title in asideBox:
    asideBox_titles=asideBox_title.text.strip()
    asideBox_all_titles.append(asideBox_titles)
for asideBox_num in range(1,11):
    asideBox_result={'순위':asideBox_num,'제목':asideBox_all_titles[asideBox_num-1], '링크':asideBox_hrefs[asideBox_num-1]}
    asideBox_results.append(asideBox_result)
#날씨 크롤링
weather_url = 'https://search.naver.com/search.naver?where=nexearch&sm=top_hty&fbm=1&ie=utf8&query=%EB%82%A0%EC%94%A8'
weather_res = requests.get(weather_url)
soup= BeautifulSoup(weather_res.text, 'html.parser')
weather_box = soup.find_all('div', class_='day_data')
weather_box_result=weather_box[:3]

#html로 바꾸기
import os
print(os.path.isfile("html_test.html"))

file = open('html_test.html','w',encoding='UTF-8')

file.write(f'''<div style="background-color: linen; padding-bottom: 15%;">
    <div style="font-size: -webkit-xxx-large; text-align: center; color: #ff2222; padding-top: 5%;padding-bottom: 5%;">오늘의 뉴스</div>
         <a href="https://search.naver.com/search.naver?where=nexearch&sm=top_hty&fbm=1&ie=utf8&query=%EB%82%A0%EC%94%A8" style="display: block;text-align: -webkit-center;padding-top: 15px;padding-bottom: 15px; color: black;">오늘의 날씨</a>
        <table style="padding:15px 0px 15px 0px;border:0;width:100%;height:0;background:none;border-top-width:1px;border-top-style:dashed;border-top-color:#c9c9c9;margin:0 0"></table>
        <div style="margin-left: 10%; padding-bottom: 30px;" class="rank">
            <ul>
                <a href='{asideBox_hrefs[0]}' style="color: black;">1. {asideBox_all_titles[0]}</ul>
            </ul>
            <ul>
                <a href='{asideBox_hrefs[1]}' style="color: black;">2. {asideBox_all_titles[1]}</ul>
            </ul>
            <ul>
                <a href='{asideBox_hrefs[2]}' style="color: black;">3. {asideBox_all_titles[2]}</ul>
            </ul>
            <ul>
                <a href='{asideBox_hrefs[3]}' style="color: black;">4. {asideBox_all_titles[3]}</a>
            </ul>
            <ul>
                <a href='{asideBox_hrefs[4]}' style="color: black;">5. {asideBox_all_titles[4]}</a>
            </ul>
            <ul>
                <a href='{asideBox_hrefs[5]}' style="color: black;">6. {asideBox_all_titles[5]}</a>
            </ul>
            <ul>
                <a href='{asideBox_hrefs[6]}' style="color: black;">7. {asideBox_all_titles[6]}</a>
            </ul>
            <ul>
                <a href='{asideBox_hrefs[7]}' style="color: black;">8. {asideBox_all_titles[7]}</a>
            </ul>
            <ul>
                <a href='{asideBox_hrefs[8]}' style="color: black;">9. {asideBox_all_titles[8]}</a>
            </ul>
            <ul>
                <a href='{asideBox_hrefs[9]}' style="color: black;">10. {asideBox_all_titles[9]}</a>
            </ul>''')
file.close()

