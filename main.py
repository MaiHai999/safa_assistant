# import requests
# from bs4 import BeautifulSoup
# import webbrowser
# import urllib.request
# from googlesearch import search
# from selenium import webdriver
# from time import sleep
# from selenium import webdriver
# from webdriver_manager.chrome import ChromeDriverManager
# from selenium.webdriver.common.by import By
# import re
# from googletrans import Translator
#
#
# #
# # location = "nam định"
# # driver = webdriver.Chrome(ChromeDriverManager().install())
# # driver.get("https://www.google.com/maps/@9.779349,105.6189045,11z?hl=vi-VN")
# # Place = driver.find_element(By.CLASS_NAME, "tactile-searchbox-input")
# # Place.send_keys(location)
# # Submit = driver.find_element(By.XPATH, "/html/body/div[3]/div[9]/div[3]/div[1]/div[1]/div[1]/div[2]/div[1]/button")
# # Submit.click()
# # sleep(5)
# # directions = driver.find_element(By.XPATH,"/html/body/div[3]/div[9]/div[9]/div/div/div[1]/div[2]/div/div[1]/div/div/div[4]/div[1]/button")
# # directions.click()
# # sleep(6)
# # find = driver.find_element(By.XPATH,"/html/body/div[3]/div[9]/div[3]/div[1]/div[2]/div/div[3]/div[1]/div[1]/div[2]/div[1]/div/input")
# # find.send_keys("đông hà , đức linh , bình thuận")
# # search = driver.find_element(By.XPATH,"/html/body/div[3]/div[9]/div[3]/div[1]/div[2]/div/div[3]/div[1]/div[1]/div[2]/button[1]")
# # search.click()
#
#
#
#
# #
# # # define a translate object
# # translate = Translator()
# # # Translate some text
# # result = translate.translate('i am', src='en', dest='vi')
# # print(result.text)
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
# # txt = "- đường tới [Thành phố Huế, tỉnh Thừa Thiên Huế](location)"
# #
# # #Search for a sequence that starts with "he", followed by 0 or more  (any) characters, and an "o":
# #
# # x = re.findall("\[.*\)", txt)
# #
# # print(x)
#
#
#
#
#
#
# from time import sleep
# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.chrome.service import Service
# from webdriver_manager.chrome import ChromeDriverManager
#
#
#
# driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
# driver.get("https://www.google.com/maps/@9.779349,105.6189045,11z?hl=vi-VN")
#
# #
# # def searchplace(location):
# #     Place = driver.find_element(By.CLASS_NAME,"tactile-searchbox-input")
# #     Place.send_keys(location)
# #     Submit = driver.find_element(By.XPATH,"/html/body/div[3]/div[9]/div[3]/div[1]/div[1]/div[1]/div[2]/div[1]/button")
# #     Submit.click()
# #     sleep(5)
# #     directions = driver.find_element(By.XPATH,"/html/body/div[3]/div[9]/div[9]/div/div/div[1]/div[2]/div/div[1]/div/div/div[4]/div[1]/button")
# #     directions.click()
# #     sleep(6)
# #     find = driver.find_element(By.XPATH,"/html/body/div[3]/div[9]/div[3]/div[1]/div[2]/div/div[3]/div[1]/div[1]/div[2]/div[1]/div/input")
# #     find.send_keys("đông hà , đức linh , bình thuận")
# #     search = driver.find_element(By.XPATH,"/html/body/div[3]/div[9]/div[3]/div[1]/div[2]/div/div[3]/div[1]/div[1]/div[2]/button[1]")
# #     search.click()
# #
#
# location = "nam định"
# Place = driver.find_element(By.CLASS_NAME,"tactile-searchbox-input")
# Place.send_keys(location)
# Submit = driver.find_element(By.XPATH,"/html/body/div[3]/div[9]/div[3]/div[1]/div[1]/div[1]/div[2]/div[1]/button")
# Submit.click()
# sleep(5)
# directions = driver.find_element(By.XPATH,"/html/body/div[3]/div[9]/div[9]/div/div/div[1]/div[2]/div/div[1]/div/div/div[4]/div[1]/button")
# directions.click()
# sleep(6)
# find = driver.find_element(By.XPATH,"/html/body/div[3]/div[9]/div[3]/div[1]/div[2]/div/div[3]/div[1]/div[1]/div[2]/div[1]/div/input")
# find.send_keys("đông hà , đức linh , bình thuận")
# search = driver.find_element(By.XPATH,"/html/body/div[3]/div[9]/div[3]/div[1]/div[2]/div/div[3]/div[1]/div[1]/div[2]/button[1]")
# search.click()
# sleep(20)
# #searchplace(location)
#
#
#
#
# #
# # def directions():
# #     sleep(10)
# #     directions = driver.find_element(By.XPATH,"/html/body/div[3]/div[9]/div[9]/div/div/div[1]/div[2]/div/div[1]/div/div/div[4]/div[1]/button")
# #     directions.click()
# #
# #
# # directions()
# #
# #
# # def find():
# #     sleep(6)
# #     find = driver.find_element(By.XPATH,"/html/body/div[3]/div[9]/div[3]/div[1]/div[2]/div/div[3]/div[1]/div[1]/div[2]/div[1]/div/input")
# #     find.send_keys("đông hà , đức linh , bình thuận")
# #     sleep(2)
# #     search = driver.find_element(By.XPATH,"/html/body/div[3]/div[9]/div[3]/div[1]/div[2]/div/div[3]/div[1]/div[1]/div[2]/button[1]")
# #     search.click()
# #
# #
# # find()
# #
# #
# #
# #
# #
# #
# #
# #
# #
# # driver = webdriver.Chrome(ChromeDriverManager().install())
# # driver.get("https://www.google.com/maps/@9.779349,105.6189045,11z?hl=vi-VN")
# # sleep(2)
# #
# #
# # def searchplace():
# #     Place = driver.find_element("tactile-searchbox-input")
# #     Place.send_keys("Tiruchirappalli")
# #     Submit = driver.find_element(
# #         "/html/body/jsl/div[3]/div[9]/div[3]/div[1]/div[1]/div[1]/div[2]/div[1]/button")
# #     Submit.click()
# #
# #
# # searchplace()
# #
# #
# # def directions():
# #     sleep(10)
# #     directions = driver.find_element(
# #         "/html/body/jsl/div[3]/div[9]/div[7]/div/div[1]/div/div/div[5]/div[1]/div/button")
# #     directions.click()
# #
# #
# # directions()
# #
# #
# # def find():
# #     sleep(6)
# #     find = driver.find_element_by_xpath(
# #         "/html/body/jsl/div[3]/div[9]/div[3]/div[1]/div[2]/div/div[3]/div[1]/div[1]/div[2]/div/div/input")
# #     find.send_keys("Tirunelveli")
# #     sleep(2)
# #     search = driver.find_element_by_xpath(
# #         "/html/body/jsl/div[3]/div[9]/div[3]/div[1]/div[2]/div/div[3]/div[1]/div[1]/div[2]/button[1]")
# #     search.click()
# #
# #
# # find()
# #
# #
# # def kilometers():
# #     sleep(5)
# #     Totalkilometers = driver.find_element_by_xpath(
# #         "/html/body/jsl/div[3]/div[9]/div[7]/div/div[1]/div/div/div[5]/div[1]/div[1]/div[1]/div[1]/div[2]/div")
# #     print("Total Kilometers:", Totalkilometers.text)
# #     sleep(5)
# #     Bus = driver.find_element_by_xpath(
# #         "/html/body/jsl/div[3]/div[9]/div[7]/div/div[1]/div/div/div[5]/div[1]/div[1]/div[1]/div[1]/div[1]/span[1]")
# #     print("Bus Travel:", Bus.text)
# #     sleep(7)
# #     Train = driver.find_element_by_xpath(
# #         "/html/body/jsl/div[3]/div[9]/div[7]/div/div[1]/div/div/div[5]/div[2]/div[1]/div[2]/div[1]/div")
# #     print("Train Travel:", Train.text)
# #     sleep(7)
# #
# #
# # kilometers()
# #
# #
# # def available():
# #     print("*COVID-19 Special Trains*")
# #     sleep(7)
# #     trainone = driver.find_element_by_xpath(
# #         "/html/body/jsl/div[3]/div[9]/div[7]/div/div[1]/div/div/div[5]/div[2]/div[1]/div[2]/div[2]/span/span[2]/span[1]/span[1]/span")
# #     print("Train No:1", trainone.text)
# #
# #
# # def availableone():
# #     trainsec = driver.find_element_by_xpath(
# #         "/html/body/jsl/div[3]/div[9]/div[7]/div/div[1]/div/div/div[5]/div[2]/div[1]/div[2]/div[2]/span/span[8]/span[1]/span[1]/span")
# #     print("Train No:2", trainsec.text)
# #
# #
# # available()
# # availableone()
# #
# #
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
# #
# # wf = open('datasong.txt', 'a' , encoding="utf-8" )
# #
# #
# # import requests
# # from bs4 import BeautifulSoup
# #
# #
# # links = ['https://tuoitre.vn/phap-luat.htm',
# #          'https://tuoitre.vn/xe.htm',
# #          'https://dulich.tuoitre.vn',
# #          'https://tuoitre.vn/nhip-song-tre.htm',
# #          'https://tuoitre.vn/van-hoa.htm',
# #          'https://tuoitre.vn/giai-tri.htm',
# #          'https://tuoitre.vn/the-thao.htm',
# #          'https://tuoitre.vn/suc-khoe.htm',
# #          'https://tuoitre.vn/gia-that.htm',
# #          'https://tuoitre.vn/ban-doc-lam-bao.htm']
# #
# # for link in links:
# #     response = requests.get(link)
# #     soup = BeautifulSoup(response.content, "html.parser")
# #     titles = soup.findAll('h3', class_='title-news')
# #     links = [link.find('a').attrs["href"] for link in titles]
# #     for link in links:
# #         news = requests.get("https://tuoitre.vn" + link)
# #         soup = BeautifulSoup(news.content, "html.parser")
# #         title = soup.find("h1", class_="article-title").text
# #         wf.write(title + "\n")
# #         print("Tiêu đề: " + title)
# #         print("_________________________________________________________________________")
# #
# #
# #
#
# #
# # textToSearch = "tình hình Ukraine"
# # url = "https://thanhnien.vn/tim-kiem/?q="
# # query = urllib.parse.quote(textToSearch)
# # webbrowser.open(url + query)
# #
# #
# # web = "định lý  đảo wikipedia"
# # for url in search(web, stop=1):
# #     webbrowser.open(url)
#
#
#
#
#
#
#
#
#
#
# #
# # # rất quan trọng
# #
# # url = "https://gianongsan.org"
# #
# # r = requests.get(url)
# # soup = BeautifulSoup(r.content, "html.parser")
# # a = soup.select_one("#post-501 > div > figure:nth-child(12) > table > tbody")
# # b = a.select("tr")
# #
# #
# #
# # for i in range(1,len(b)):
# #     text = b[i].select_one("td:nth-child(1)").text
# #     if(text != "\n"):
# #         print(text)
#
#
#
#
#
#
#
#
#
#
# #
# # path = "https://www.shopeeanalytics.com/vn/search/keyword"
# #
# #
# # response = requests.get(path)
# # soup = BeautifulSoup(response.content, "lxml")
# # all_tags = soup.select_one('#DataTables_Table_0 > tbody > tr:nth-child(1) > td:nth-child(2)')
# #
# # print(all_tags)
# #
#
#
#
#
#
#
#
# #
# # wf = open('song.txt', 'a' , encoding="utf-8" )
# #
# #
# #
# # data_path = "datasong.txt"
# # with open(data_path, "r", encoding="utf-8") as f:
# #     lines = f.read().split("\n")
# #
# #
# #
# # h = ' '
# #
# # for i in range(len(lines)):
# #     row = lines[i]
# #     a1 = re.findall("-.*\[", row)
# #     a2 = re.findall("\).*", row)
# #     a = a1[0] + a2[0]
# #     if(h != a):
# #         wf.write( row + " \n")
# #         h = a
# #
# #    wf.write("    - " + x[0] + " \n")
#
#
#
# #   wf.write( "    - " + x[0] + "\n")
#
#
#
#
# #
# #
# #
# #
# #
# #
# #
# #
# #
# #
# #
# # data = []
# # for i,line in enumerate(lines):
# #     a = i + 3
# #     if(a % 3 == 0):
# #         data.append(line)
# #
# #
# #
# # sp = []
# #
# # for line in data:
# #     a , b,c = line.split("\t")
# #     sp.append(b)
#
#
#
#
#
#
#
#
#
#
#
# # data1 = []
# # for line in data:
# #     a = line.replace("-","")
# #     data1.append(a)
# #
# # data2 = []
# #
# # for line in data1:
# #     a = line.replace("     ","")
# #     data2.append(a)
# #
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
# #
# #
# # body > div.e > div.e-n-l.fl > div.e-n-d > div.news-detail-body > table > tbody > tr:nth-child(2) > td:nth-child(2) > p
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#



import requests
sender = input("What is your name?\n")
bot_message = ""
while bot_message != "Bye":
    message = input("What's your message?\n")
    print("Sending message now...")
    r = requests.post('http://localhost:5002/webhooks/rest/webhook', json={"sender": sender, "message": message})
    print("Bot says, ",end=' ')
    for i in r.json():
        bot_message = i['text']
        print(f"{i['text']}")


