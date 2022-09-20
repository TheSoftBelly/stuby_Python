import requests
from bs4 import BeautifulSoup

BASE_URL = 'https://www.thebell.co.kr/free/content/article.asp?page=1&svccode=00'
res = requests.get(BASE_URL)
soup= BeautifulSoup(res.text , 'html.parser')
asideBox = soup.select('#contents > div.contentSection > div > div.asideBox > div.bestBox.tp2 > div > ul > li > ul > li > a')
asideBox_all_titles=[]
asideBox_hrefs = []
asideBox_call_hrefs = soup.find_all('a', class_='txtE')
for asideBox_href in asideBox_call_hrefs:
    asideBox_hrefs.append('https://www.thebell.co.kr/'+asideBox_href.attrs['href'])
for asideBox_title in asideBox:
    asideBox_titles=asideBox_title.text.strip()
    asideBox_all_titles.append(asideBox_titles)
# 첫페이지 신규 내용 크롤링
BASE_LIST_URL = 'https://www.thebell.co.kr/free/content/Article.asp?svccode=00'
res = requests.get(BASE_LIST_URL)
soup = BeautifulSoup(res.text , 'html.parser')
main_texts_titles = soup.select('#contents > div.contentSection > div > div.newsBox > div.newsList > div.listBox > ul > li > dl > a > dt')
main_texts_contents = soup.select('#contents > div.contentSection > div > div.newsBox > div.newsList > div.listBox > ul > li > dl > a > dd')
main_texts_reporters = soup.select('#contents > div.contentSection > div > div.newsBox > div.newsList > div.listBox > ul > li > dl > dd > span.user')
main_texts_titles_list=[]
main_texts_contents_list=[]
main_texts_reporters_list=[]
for main_text in main_texts_titles:
    main_texts_titles_list.append(main_text.text)
for main_texts_content in main_texts_contents:
    main_texts_contents_list.append(main_texts_content.text)
for main_texts_reporter in main_texts_reporters:
    main_texts_reporters_list.append(main_texts_reporter.text.strip().replace('\xa0',' '))


#날씨 크롤링
weather_url = 'https://search.naver.com/search.naver?where=nexearch&sm=top_hty&fbm=1&ie=utf8&query=%EB%82%A0%EC%94%A8'
weather_res = requests.get(weather_url)
soup= BeautifulSoup(weather_res.text, 'html.parser')
weather_box = soup.find_all('div', class_="list_box _weekly_weather")
weather_today_daylist = []
weather_today_numdaylist = []
weather_like_todayresultslist = []
weather_today_temlist=[]
for weather_todays in weather_box:
    weather_today=weather_todays.select('ul > li > div > div.cell_date > span > strong')
    for weather_today_day in weather_today[0:3]:
        weather_today_daylist.append(weather_today_day.text)

for weather_today_num in weather_box:
    weather_today_numdays=weather_today_num.select('ul > li > div > div.cell_date > span > span')
    for weather_today_numday in weather_today_numdays[0:3]:
        weather_today_numdaylist.append(weather_today_numday.text)

for weather_likes in weather_box:
    weather_like = weather_likes.select('ul > li > div > div.cell_weather')
    for weather_like_todayresults in weather_like[0:3]:
        weather_like_todayresultslist.append(weather_like_todayresults.text.strip())

for weather_tems in weather_box:
    weather_today_tems = weather_tems.select('ul > li > div > div.cell_temperature > span')
    for weather_today_tem in weather_today_tems[0:3]:
        weather_today_temlist.append(weather_today_tem.text.strip())

asideBox_ul=''
#html로 바꾸기
for asideBox_num_for_ul in range(len(asideBox_hrefs)):
    asideBox_ul = asideBox_ul+'<ul><a href="{asideBox_href}" style="color: black; font-size: initial;">{rank}.  {asideBox_all_title}</a></ul>'.format(asideBox_href=asideBox_hrefs[asideBox_num_for_ul],asideBox_all_title=asideBox_all_titles[asideBox_num_for_ul],rank=asideBox_num_for_ul+1)


file = open('html_test.html','w',encoding='UTF-8')
file_contents=f'''<div style="background-color: white;padding-bottom: 15%;">
        <div style="font-size: -webkit-xxx-large; text-align: center; color: #ff2222; padding-top: 5%;padding-bottom: 5%;">오늘의 뉴스</div>
        <a href="https://search.naver.com/search.naver?where=nexearch&amp;sm=top_hty&amp;fbm=1&amp;ie=utf8&amp;query=%EB%82%A0%EC%94%A8" style="display: block;text-align: -webkit-center;padding-top: 15px;padding-bottom: 15px; color: black;">오늘의 날씨</a>
    <div style="display: grid;padding: 15px;grid-template-columns: 1fr 1fr 1fr;text-align: center; font-size: 17px;">
        <div class="day_data"> 
            <div class="cell_date">
                <span class="date_inner">
                    <strong class="day">content</strong>
                    <span class="date">{weather_today_numdaylist[0]}</span>
                </span>
            </div> 
            <div class="cell_weather">{weather_like_todayresultslist[0]} 
        </div> <div class="cell_temperature">{weather_today_temlist[0]}
        </div>
        </div>
        <div class="day_data"> 
            <div class="cell_date">
                <span class="date_inner">
                    <strong class="day">{weather_today_daylist[1]}</strong>
                    <span class="date">{weather_today_numdaylist[1]}</span>
                </span>
            </div> 
            <div class="cell_weather">{weather_like_todayresultslist[1]} 
        </div> <div class="cell_temperature">{weather_today_temlist[1]}
        </div>
        </div>
        <div class="day_data"> 
            <div class="cell_date">
                <span class="date_inner">
                    <strong class="day">{weather_today_daylist[2]}</strong>
                    <span class="date">{weather_today_numdaylist[2]}</span>
                </span>
            </div> 
            <div class="cell_weather">{weather_like_todayresultslist[2]} 
        </div> <div class="cell_temperature">{weather_today_temlist[2]}
        </div>
        </div>
    
    </div>
        <table style="padding:15px 0px 15px 0px;border:0;width:100%;height:0;background:none;border-top-width:1px;border-top-style:dashed;border-top-color: red;margin:0 0"></table>
            <div style="margin-left: 5%;margin-right: 5%;padding-bottom: 30px;" class="rank">
                {asideBox_ul}
            </div>
            <table style="padding:15px 0px 15px 0px;border:0;width:100%;height:0;background:none;border-top-width:1px;border-top-style:dashed;border-top-color: red;margin:0 0"></table>
        </div>'''.format(asideBox_ul=asideBox_ul)

file.write(file_contents)
file.close()

#메일 보내는 라이브러리 / send_who 에는 이메일 주소를 string 으로 보내준다 
#만약에 리스트라면 ", ".join(send_who) 를 하지만 그게 아니라면 그냥 '메일, 메일'형태로 보내줌
#여기서 핵심은 ,후에 한번 뛰우는거다.

def mail_form(send_who):
    SMTP_SEVER = 'smtp.naver.com'
    SMTP_PORT = 465
    SMTP_USER = 'jjoon1024@naver.com'
    SMTP_PASSWORD = open('./email_config.txt','r').readline().rstrip()

    from email.mime.multipart import MIMEMultipart 
    from email.mime.text import MIMEText

    #편지봉투 만들기
    msg = MIMEMultipart('alternative')
    #html 파일 열기
    f=open("html_test.html", 'r')


    #편지 내용 = html파일을 읽어온 것
    contents = f.read()

    msg['From'] = SMTP_USER 
    msg['To'] = send_who
    msg['Subject'] = '오늘의 뉴스'

    text = MIMEText(contents,'html')

    msg.attach(text)

    import smtplib

    try:
        smtp=smtplib.SMTP_SSL(SMTP_SEVER, SMTP_PORT)
        print('메일 서버 접속 성공')
        smtp.login(SMTP_USER, SMTP_PASSWORD)
        print('로그인 성공')
        smtp.sendmail(SMTP_USER,send_who.split(',') , msg.as_string())
        print('이메일 발송 성공!')


    except Exception as e:
        print('###에러발생###')
        print(e)
    finally:
        smtp.close()
        print('파이널리')

mail_form(input('메일 주소를 입력해주세요. 만약에 보내는 곳이 한 곳 이상이면 ex)메일, 메일, 메일 형태로 작성해주세요!:'))


