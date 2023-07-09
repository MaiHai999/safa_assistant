from rasa_sdk import Action
from rasa_sdk.events import SlotSet
import webbrowser
import urllib.request
import re
from googlesearch import search
from datetime import date
from datetime import datetime
import requests
from bs4 import BeautifulSoup
from time import sleep
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from googletrans import Translator


class ActionAccessWeb(Action):
    def name(self):
      return "action_request_access_web"

    def run(self, dispatcher, tracker, domain):
      web = tracker.get_slot("web")
      for url in search(web, stop=1):
          webbrowser.open(url)
      dispatcher.utter_message(text=f"bạn có hài lòng với kết quả trên không ?")
      return []



class ActionSearchSong(Action):
    def name(self):
      return "action_find_song"

    def run(self, dispatcher, tracker, domain):
      song = tracker.get_slot("song")
      textToSearch = song
      query = urllib.parse.quote(textToSearch)
      html = urllib.request.urlopen("https://www.youtube.com/results?search_query=" + query)
      video_ids = re.findall(r"watch\?v=(\S{11})", html.read().decode())
      url = "https://www.youtube.com/watch?v=" + video_ids[0]
      webbrowser.open(url)
      dispatcher.utter_message(text=f"bạn có hài lòng với kết quả trên không ?")
      return []




class Actioncheckdayduong(Action):
    def name(self):
      return "action_check_day_duong"

    def run(self, dispatcher, tracker, domain):

      today = date.today()
      d1 = today.strftime("%d/%m/%Y")
      day = "hôm này là ngày :" + d1
      dispatcher.utter_message(day)
      return []


class Actionchecktime(Action):
    def name(self):
      return "action_check_time"

    def run(self, dispatcher, tracker, domain):
      now = datetime.now()
      dt_string = now.strftime("%H:%M")
      time_now = "hiện tại là : " + dt_string
      dispatcher.utter_message(time_now)
      return []

class Actioncheckdayam(Action):
    def name(self):
      return "action_check_day_am"

    def run(self, dispatcher, tracker, domain):
      path = "https://www.xemlicham.com"
      response = requests.get(path)
      soup = BeautifulSoup(response.content, "html.parser")
      lunar_day = soup.findAll('span', class_="lunar-date")
      lunar_day1 = "ngày âm là : " + lunar_day[0].text
      dispatcher.utter_message(lunar_day1)
      return []


class Actioncheckxoso(Action):
    def name(self):
      return "action_xoso"

    def run(self, dispatcher, tracker, domain):

      def xo_so1(soup):
        title = soup.select_one("body > section > div.col-l > div:nth-child(4) > h2 > strong > a:nth-child(3)").text
        db = soup.select_one("#load_kq_tinh_0 > div.one-city > table > tbody > tr.db > td.v-giai.number > span").text
        giai1 = soup.select_one("#load_kq_tinh_0 > div.one-city > table > tbody > tr:nth-child(8) > td.v-giai.number > span").text
        giai2 = soup.select_one("#load_kq_tinh_0 > div.one-city > table > tbody > tr:nth-child(7) > td.v-giai.number > span").text
        giai3a = soup.select_one("#load_kq_tinh_0 > div.one-city > table > tbody > tr:nth-child(6) > td.v-giai.number > span.v-g3-0").text
        giai3b = soup.select_one("#load_kq_tinh_0 > div.one-city > table > tbody > tr:nth-child(6) > td.v-giai.number > span.v-g3-1").text
        giai3 = giai3a + "   " + giai3b
        giai4a = soup.select_one("#load_kq_tinh_0 > div.one-city > table > tbody > tr.g4 > td.v-giai.number > span.v-g4-0").text
        giai4g = soup.select_one("#load_kq_tinh_0 > div.one-city > table > tbody > tr.g4 > td.v-giai.number > span.v-g4-1").text
        giai4b = soup.select_one("#load_kq_tinh_0 > div.one-city > table > tbody > tr.g4 > td.v-giai.number > span.v-g4-2").text
        giai4c = soup.select_one("#load_kq_tinh_0 > div.one-city > table > tbody > tr.g4 > td.v-giai.number > span.v-g4-3").text
        giai4d = soup.select_one("#load_kq_tinh_0 > div.one-city > table > tbody > tr.g4 > td.v-giai.number > span.v-g4-4").text
        giai4e = soup.select_one("#load_kq_tinh_0 > div.one-city > table > tbody > tr.g4 > td.v-giai.number > span.v-g4-5").text
        giai4f = soup.select_one("#load_kq_tinh_0 > div.one-city > table > tbody > tr.g4 > td.v-giai.number > span.v-g4-6").text
        giai4 = giai4a + "   " + giai4b + "   " + giai4c + "   " + giai4d + "   " + giai4e + "   " + giai4f + "   " + giai4g
        giai5 = soup.select_one("#load_kq_tinh_0 > div.one-city > table > tbody > tr:nth-child(4) > td.v-giai.number > span").text
        giai6a = soup.select_one("#load_kq_tinh_0 > div.one-city > table > tbody > tr:nth-child(3) > td.v-giai.number > span.v-g6-0").text
        giai6b = soup.select_one("#load_kq_tinh_0 > div.one-city > table > tbody > tr:nth-child(3) > td.v-giai.number > span.v-g6-1").text
        giai6c = soup.select_one("#load_kq_tinh_0 > div.one-city > table > tbody > tr:nth-child(3) > td.v-giai.number > span.v-g6-2").text
        giai6 = giai6a + "   " + giai6b + "   " + giai6c
        giai7 = soup.select_one("#load_kq_tinh_0 > div.one-city > table > tbody > tr:nth-child(2) > td.v-giai.number > span").text
        giai8 = soup.select_one("#load_kq_tinh_0 > div.one-city > table > tbody > tr.g8 > td.v-giai.number > span").text

        kp = title + "\n" + "giải ĐB: " + db + "\n" + "giải 1: " + giai1 + "\n" + "giải 2: " + giai2 + "\n" + "giải 3: " + giai3 + "\n" + "giải 4: " + giai4 + "\n" + "giải 5: " + giai5 + "\n" + "giải 6: " + giai6 + "\n" + "giải 7: " + giai7 + "\n" + "giải 8: " + giai8 + "\n"
        return kp

      def xo_so2(soup):
        title = soup.select_one("body > section > div.col-l > div:nth-child(4) > h2 > strong > a:nth-child(3)").text
        db = soup.select_one("#load_kq_tinh_0 > div.one-city > table > tbody > tr.db > td.v-giai.number > span").text
        giai1 = soup.select_one("#load_kq_tinh_0 > div.one-city > table > tbody > tr:nth-child(3) > td.v-giai.number > span").text
        giai2a = soup.select_one("#load_kq_tinh_0 > div.one-city > table > tbody > tr:nth-child(4) > td.v-giai.number > span.v-g2-0").text
        giai2b = soup.select_one("#load_kq_tinh_0 > div.one-city > table > tbody > tr:nth-child(4) > td.v-giai.number > span.v-g2-1").text
        giai2 = giai2a + "   " + giai2b
        giai3a = soup.select_one("#load_kq_tinh_0 > div.one-city > table > tbody > tr:nth-child(5) > td.v-giai.number > span.v-g3-0").text
        giai3b = soup.select_one("#load_kq_tinh_0 > div.one-city > table > tbody > tr:nth-child(5) > td.v-giai.number > span.v-g3-1").text
        giai3c = soup.select_one("#load_kq_tinh_0 > div.one-city > table > tbody > tr:nth-child(5) > td.v-giai.number > span.v-g3-2").text
        giai3d = soup.select_one("#load_kq_tinh_0 > div.one-city > table > tbody > tr:nth-child(5) > td.v-giai.number > span.v-g3-3").text
        giai3e = soup.select_one("#load_kq_tinh_0 > div.one-city > table > tbody > tr:nth-child(5) > td.v-giai.number > span.v-g3-4").text
        giai3f = soup.select_one("#load_kq_tinh_0 > div.one-city > table > tbody > tr:nth-child(5) > td.v-giai.number > span.v-g3-5").text
        giai3 = giai3a + "   " + giai3b + "   " + giai3c + "   " + giai3d + "   " + giai3e + "   " + giai3f
        giai4a = soup.select_one("#load_kq_tinh_0 > div.one-city > table > tbody > tr:nth-child(6) > td.v-giai.number > span.v-g4-0").text
        giai4b = soup.select_one("#load_kq_tinh_0 > div.one-city > table > tbody > tr:nth-child(6) > td.v-giai.number > span.v-g4-1").text
        giai4c = soup.select_one("#load_kq_tinh_0 > div.one-city > table > tbody > tr:nth-child(6) > td.v-giai.number > span.v-g4-2").text
        giai4d = soup.select_one("#load_kq_tinh_0 > div.one-city > table > tbody > tr:nth-child(6) > td.v-giai.number > span.v-g4-3").text
        giai4 = giai4a + "   " + giai4b + "   " + giai4c + "   " + giai4d
        giai5a = soup.select_one("#load_kq_tinh_0 > div.one-city > table > tbody > tr:nth-child(7) > td.v-giai.number > span.v-g5-0").text
        giai5b = soup.select_one("#load_kq_tinh_0 > div.one-city > table > tbody > tr:nth-child(7) > td.v-giai.number > span.v-g5-1").text
        giai5c = soup.select_one("#load_kq_tinh_0 > div.one-city > table > tbody > tr:nth-child(7) > td.v-giai.number > span.v-g5-2").text
        giai5d = soup.select_one("#load_kq_tinh_0 > div.one-city > table > tbody > tr:nth-child(7) > td.v-giai.number > span.v-g5-3").text
        giai5e = soup.select_one("#load_kq_tinh_0 > div.one-city > table > tbody > tr:nth-child(7) > td.v-giai.number > span.v-g5-4").text
        giai5f = soup.select_one("#load_kq_tinh_0 > div.one-city > table > tbody > tr:nth-child(7) > td.v-giai.number > span.v-g5-5").text
        giai5 = giai5a + "   " + giai5b + "   " + giai5c + "   " + giai5d + "   " + giai5e + "   " + giai5f
        giai6a = soup.select_one("#load_kq_tinh_0 > div.one-city > table > tbody > tr:nth-child(8) > td.v-giai.number > span.v-g6-0").text
        giai6b = soup.select_one("#load_kq_tinh_0 > div.one-city > table > tbody > tr:nth-child(8) > td.v-giai.number > span.v-g6-1").text
        giai6c = soup.select_one("#load_kq_tinh_0 > div.one-city > table > tbody > tr:nth-child(8) > td.v-giai.number > span.v-g6-2").text
        giai6 = giai6a + "   " + giai6b + "   " + giai6c
        giai7a = soup.select_one("#load_kq_tinh_0 > div.one-city > table > tbody > tr.g7 > td.v-giai.number > span.v-g7-0").text
        giai7b = soup.select_one("#load_kq_tinh_0 > div.one-city > table > tbody > tr.g7 > td.v-giai.number > span.v-g7-1").text
        giai7c = soup.select_one("#load_kq_tinh_0 > div.one-city > table > tbody > tr.g7 > td.v-giai.number > span.v-g7-2").text
        giai7d = soup.select_one("#load_kq_tinh_0 > div.one-city > table > tbody > tr.g7 > td.v-giai.number > span.v-g7-3").text
        giai7 = giai7a + "   " + giai7b + "   " + giai7c + "   " + giai7d
        kp = title + "\n" + "giải ĐB: " + db + "\n" + "giải 1: " + giai1 + "\n" + "giải 2: " + giai2 + "\n" + "giải 3: " + giai3 + "\n" + "giải 4: " + giai4 + "\n" + "giải 5: " + giai5 + "\n" + "giải 6: " + giai6 + "\n" + "giải 7: " + giai7 + "\n"

        return kp

      links = ['https://xoso.me/xsqn-sxqn-ket-qua-xo-so-quang-ninh.html',
               'https://xoso.me/xsbn-sxbn-ket-qua-xo-so-bac-ninh.html',
               'https://xoso.me/xshp-sxhp-ket-qua-xo-so-hai-phong.html',
               'https://xoso.me/xsnd-sxnd-ket-qua-xo-so-nam-dinh.html',
               'https://xoso.me/xstb-sxtb-ket-qua-xo-so-thai-binh.html',
               'https://xoso.me/mien-nam/xscm-ket-qua-xo-so-ca-mau-p8.html',
               'https://xoso.me/mien-nam/xsdt-ket-qua-xo-so-dong-thap-p12.html',
               'https://xoso.me/mien-nam/xshcm-ket-qua-xo-so-thanh-pho-ho-chi-minh-p14.html',
               'https://xoso.me/mien-nam/xsbl-ket-qua-xo-so-bac-lieu-p3.html',
               'https://xoso.me/mien-nam/xsbt-ket-qua-xo-so-ben-tre-p4.html',
               'https://xoso.me/mien-nam/xsvt-ket-qua-xo-so-vung-tau-p22.html',
               'https://xoso.me/mien-nam/xsct-ket-qua-xo-so-can-tho-p9.html',
               'https://xoso.me/mien-nam/xsdn-ket-qua-xo-so-dong-nai-p11.html',
               'https://xoso.me/mien-nam/xsst-ket-qua-xo-so-soc-trang-p17.html',
               'https://xoso.me/mien-nam/xsag-ket-qua-xo-so-an-giang-p2.html',
               'https://xoso.me/mien-nam/xsbth-ket-qua-xo-so-binh-thuan-p7.html',
               'https://xoso.me/mien-nam/xstn-ket-qua-xo-so-tay-ninh-p18.html',
               'https://xoso.me/mien-nam/xsbd-ket-qua-xo-so-binh-duong-p5.html',
               'https://xoso.me/mien-nam/xstv-ket-qua-xo-so-tra-vinh-p20.html',
               'https://xoso.me/mien-nam/xstv-ket-qua-xo-so-tra-vinh-p20.html',
               'https://xoso.me/mien-nam/xsvl-ket-qua-xo-so-vinh-long-p21.html',
               'https://xoso.me/mien-nam/xsbp-ket-qua-xo-so-binh-phuoc-p6.html',
               'https://xoso.me/mien-nam/xshg-ket-qua-xo-so-hau-giang-p13.html',
               'https://xoso.me/mien-nam/xsla-ket-qua-xo-so-long-an-p16.html',
               'https://xoso.me/mien-nam/xsdl-ket-qua-xo-so-da-lat-p10.html',
               'https://xoso.me/mien-nam/xskg-ket-qua-xo-so-kien-giang-p15.html',
               'https://xoso.me/mien-nam/xstg-ket-qua-xo-so-tien-giang-p19.html',
               'https://xoso.me/mien-trung/xspy-ket-qua-xo-so-phu-yen-p31.html',
               'https://xoso.me/mien-trung/xstth-ket-qua-xo-so-thua-thien-hue-p36.html',
               'https://xoso.me/mien-trung/xsdlk-ket-qua-xo-so-dac-lac-p25.html',
               'https://xoso.me/mien-trung/xsqnm-ket-qua-xo-so-quang-nam-p34.html',
               'https://xoso.me/mien-trung/xsbdi-ket-qua-xo-so-binh-dinh-p23.html',
               'https://xoso.me/mien-trung/xsqt-ket-qua-xo-so-quang-tri-p35.html',
               'https://xoso.me/mien-trung/xsgl-ket-qua-xo-so-gia-lai-p27.html',
               'https://xoso.me/mien-trung/xsnt-ket-qua-xo-so-ninh-thuan-p30.html',
               'https://xoso.me/mien-trung/xsdno-ket-qua-xo-so-dac-nong-p26.html',
               'https://xoso.me/mien-trung/xsqng-ket-qua-xo-so-quang-ngai-p33.html',
               'https://xoso.me/mien-trung/xskt-ket-qua-xo-so-kon-tum-p29.html',
               'https://xoso.me/mien-trung/xsdng-ket-qua-xo-so-da-nang-p24.html',
               'https://xoso.me/mien-trung/xskh-ket-qua-xo-so-khanh-hoa-p28.html',
              ]

      location = tracker.get_slot("location")
      key = "xổ số " + location + " xoso.me hôm nay"
      for url in search(key, stop=1):
        web = url

      for i, link in enumerate(links):
        if (i <= 4 and web == link):
          response = requests.get(web)
          soup = BeautifulSoup(response.content, 'lxml')
          utter_xoso = xo_so2(soup)
          break
        elif (i > 4 and web == link):
          response = requests.get(web)
          soup = BeautifulSoup(response.content, 'lxml')
          utter_xoso = xo_so1(soup)
          break
        elif(location == "hà nội" or location == "ha noi" or location == "Hà Nội" or location == "HÀ NỘI" or location == "HÀ NỘI"):
          response = requests.get("https://xoso.me/xo-so-ha-noi.html")
          soup = BeautifulSoup(response.content, 'lxml')
          utter_xoso = xo_so2(soup)
          break
        else:
          utter_xoso = "xin lỗi tôi không thể tìm ra kết quả tỉnh này"

      dispatcher.utter_message(utter_xoso)
      return []


class ActionAccessshopee(Action):
    def name(self):
      return "action_request_access_shopee"

    def run(self, dispatcher, tracker, domain):
      textToSearch = tracker.get_slot("product")
      url = "https://shopee.vn/search?keyword="
      query = urllib.parse.quote(textToSearch)
      webbrowser.open(url + query)

      dispatcher.utter_message(text=f"tôi đã tìm được một số sản phẩm trên shopee hy vọng có thứ bạn cần ")
      return []


class ActionAccesssWikipedia(Action):
    def name(self):
      return "action_search_knowledge"

    def run(self, dispatcher, tracker, domain):
      web = tracker.get_slot("concept")
      title = web + " trên wikipedia"
      for url in search(title, stop=2):
          url1 = url
      webbrowser.open(url1)
      dispatcher.utter_message(text=f"tôi đã tìm được một só kiến thức hy vọng bạn thích nó")
      return []


class ActionAccessthanhnien(Action):
    def name(self):
      return "action_doc_bao"

    def run(self, dispatcher, tracker, domain):
      textToSearch = tracker.get_slot("news")
      query = urllib.parse.quote(textToSearch)
      url = "https://thanhnien.vn/tim-kiem/?q=" + query
      webbrowser.open(url)
      dispatcher.utter_message(text=f"tôi đã tìm được một số tin tức có trên báo Thanh Niên hy vọng nó có ích cho bạn")
      return []


class ActionAccessbaothanhnien(Action):
    def name(self):
      return "action_doc_bao_thanh_nien"

    def run(self, dispatcher, tracker, domain):
      url = "https://thanhnien.vn"
      webbrowser.open(url)
      dispatcher.utter_message(text=f"tôi đã mở báo Thanh Niên")
      return []


def price_product(path,soup):
    raw = soup.select_one(path).text
    price = raw.replace("\n", "").replace("\t","").replace(" ","")
    return price

class Actionsearchprice(Action):
    def name(self):
        return "action_price"

    def run(self, dispatcher, tracker, domain):
        url = "https://gianongsan.org"
        r = requests.get(url)
        soup = BeautifulSoup(r.content, "html.parser")

        product = tracker.get_slot("product")
        if (product == "bắp non" or product == "Bắp Non" or product == "BẮP NON" or product == "bắp NON" or product == "Bắp NON"  ):
            path = "#post-501 > div > figure.wp-block-table.is-style-regular > table > tbody > tr:nth-child(2) > td:nth-child(5)"
            price = "giá bắp non là:" + price_product(path,soup)+ "/1kg"
        elif (product == "bắp cải trắng" or product == "Bắp Cải Trắng" or product == "BẮP CẢI TRẮNG" ):
            path = "#post-501 > div > figure.wp-block-table.is-style-regular > table > tbody > tr:nth-child(3) > td:nth-child(5)"
            price = "giá bắp cải tím là:" + price_product(path,soup)+ "/1kg"
        elif (product == "bắp cải tím" or product == "Bắp Cải Tím" or product == "BẮP CẢI TÍM" ):
            path = "#post-501 > div > figure.wp-block-table.is-style-regular > table > tbody > tr:nth-child(4) > td:nth-child(5)"
            price = price_product(path,soup)+ "/1kg"
        elif (product == "bí đỏ"):
            path = "#post-501 > div > figure.wp-block-table.is-style-regular > table > tbody > tr:nth-child(5) > td:nth-child(5)"
            price = price_product(path,soup)+ "/1kg"
        elif (product == "bí đao"):
            path = "#post-501 > div > figure.wp-block-table.is-style-regular > table > tbody > tr:nth-child(6) > td:nth-child(5)"
            price = price_product(path,soup)+ "/1kg"
        elif (product == "dưa leo"):
            path = "#post-501 > div > figure.wp-block-table.is-style-regular > table > tbody > tr:nth-child(7) > td:nth-child(5)"
            price = price_product(path,soup)+ "/1kg"
        elif (product == "khổ qua"):
            path = "#post-501 > div > figure.wp-block-table.is-style-regular > table > tbody > tr:nth-child(8) > td:nth-child(5)"
            price = price_product(path,soup)+ "/1kg"
        elif (product == "khoai tây"):
            path = "#post-501 > div > figure.wp-block-table.is-style-regular > table > tbody > tr:nth-child(9) > td:nth-child(5)"
            price = price_product(path,soup)+ "/1kg"
        elif (product == "cà rốt"):
            path = "#post-501 > div > figure.wp-block-table.is-style-regular > table > tbody > tr:nth-child(10) > td:nth-child(5)"
            price = price_product(path,soup)+ "/1kg"
        elif (product == "cà tím"):
            path = "#post-501 > div > figure.wp-block-table.is-style-regular > table > tbody > tr:nth-child(11) > td:nth-child(5)"
            price = price_product(path,soup)+ "/1kg"
        elif (product == "cải bó xôi"):
            path = "#post-501 > div > figure.wp-block-table.is-style-regular > table > tbody > tr:nth-child(12) > td:nth-child(5)"
            price = price_product(path,soup)+ "/1kg"
        elif (product == "cải ngọt"):
            path = "#post-501 > div > figure.wp-block-table.is-style-regular > table > tbody > tr:nth-child(13) > td:nth-child(5)"
            price = price_product(path,soup)+ "/1kg"
        elif (product == "cải thảo"):
            path = "#post-501 > div > figure.wp-block-table.is-style-regular > table > tbody > tr:nth-child(14) > td:nth-child(5)"
            price = price_product(path,soup)+ "/1kg"
        elif (product == "cải bẹ xanh"):
            path = "#post-501 > div > figure.wp-block-table.is-style-regular > table > tbody > tr:nth-child(15) > td:nth-child(5)"
            price = price_product(path,soup)+ "/1kg"
        elif (product == "cải "):
            path = "#post-501 > div > figure.wp-block-table.is-style-regular > table > tbody > tr:nth-child(16) > td:nth-child(5)"
            price = price_product(path,soup)+ "/1kg"
        elif (product == "cần tây "):
            path = "#post-501 > div > figure.wp-block-table.is-style-regular > table > tbody > tr:nth-child(17) > td:nth-child(5)"
            price = price_product(path,soup)+ "/1kg"
        elif (product == "rau muốn"):
            path = "#post-501 > div > figure.wp-block-table.is-style-regular > table > tbody > tr:nth-child(18) > td:nth-child(5)"
            price = price_product(path,soup)+ "/1kg"
        elif (product == "rau má"):
            path = "#post-501 > div > figure.wp-block-table.is-style-regular > table > tbody > tr:nth-child(19) > td:nth-child(5)"
            price = price_product(path,soup)+ "/1kg"
        elif (product == "rau mùng tơi"):
            path = "#post-501 > div > figure.wp-block-table.is-style-regular > table > tbody > tr:nth-child(20) > td:nth-child(5)"
            price = price_product(path,soup)+ "/1kg"
        elif (product == "xà lách gai"):
            path = "#post-501 > div > figure.wp-block-table.is-style-regular > table > tbody > tr:nth-child(21) > td:nth-child(5)"
            price = price_product(path,soup)+ "/1kg"
        elif (product == "xà lách xong"):
            path = "#post-501 > div > figure.wp-block-table.is-style-regular > table > tbody > tr:nth-child(22) > td:nth-child(5)"
            price = price_product(path,soup)+ "/1kg"
        elif (product == "su su"):
            path = "#post-501 > div > figure.wp-block-table.is-style-regular > table > tbody > tr:nth-child(23) > td:nth-child(5)"
            price = price_product(path,soup)+ "/1kg"
        elif (product == "nấm bào ngư"):
            path = "#post-501 > div > figure.wp-block-table.is-style-regular > table > tbody > tr:nth-child(24) > td:nth-child(5)"
            price = price_product(path,soup)+ "/1kg"
        elif (product == "nấm đùi gà"):
            path = "#post-501 > div > figure.wp-block-table.is-style-regular > table > tbody > tr:nth-child(25) > td:nth-child(5)"
            price = price_product(path,soup)+ "/1kg"
        elif (product == "nấm rong cô"):
            path = "#post-501 > div > figure.wp-block-table.is-style-regular > table > tbody > tr:nth-child(26) > td:nth-child(5)"
            price = price_product(path,soup)+ "/1kg"
        elif (product == "cà chua "):
            path = "#post-501 > div > figure.wp-block-table.is-style-regular > table > tbody > tr:nth-child(27) > td:nth-child(5)"
            price = price_product(path,soup)+ "/1kg"
        elif (product == "bắp cải"):
            path = "#post-501 > div > figure.wp-block-table.is-style-regular > table > tbody > tr:nth-child(28) > td:nth-child(5)"
            price = price_product(path,soup)+ "/1kg"
        elif (product == "hành lá"):
            path = "#post-501 > div > figure.wp-block-table.is-style-regular > table > tbody > tr:nth-child(29) > td:nth-child(5)"
            price = price_product(path,soup)+ "/1kg"
        elif (product == "hành tây"):
            path = "#post-501 > div > figure.wp-block-table.is-style-regular > table > tbody > tr:nth-child(30) > td:nth-child(5)"
            price = price_product(path,soup)+ "/1kg"
        elif (product == "gừng"):
            path = "#post-501 > div > figure.wp-block-table.is-style-regular > table > tbody > tr:nth-child(31) > td:nth-child(5)"
            price = price_product(path,soup)+ "/1kg"
        elif (product == "ớt"):
            path = "#post-501 > div > figure.wp-block-table.is-style-regular > table > tbody > tr:nth-child(32) > td:nth-child(5)"
            price = price_product(path,soup)+ "/1kg"
        elif (product == "tỏi"):
            path = "#post-501 > div > figure.wp-block-table.is-style-regular > table > tbody > tr:nth-child(33) > td:nth-child(5)"
            price = price_product(path,soup)+ "/1kg"
        elif (product == "ngò rí"):
            path = "#post-501 > div > figure.wp-block-table.is-style-regular > table > tbody > tr:nth-child(34) > td:nth-child(5)"
            price = price_product(path,soup)+ "/1kg"
        elif (product == "ngò gai"):
            path = "#post-501 > div > figure.wp-block-table.is-style-regular > table > tbody > tr:nth-child(35) > td:nth-child(5)"
            price = price_product(path,soup)+ "/1kg"
        elif (product == "cá tra"):
            path = "#post-501 > div > figure.wp-block-table.aligncenter > table > tbody > tr:nth-child(2) > td:nth-child(5)"
            price = price_product(path,soup)+ "/1kg"
        elif (product == "lươn"):
            path = "#post-501 > div > figure.wp-block-table.aligncenter > table > tbody > tr:nth-child(3) > td:nth-child(5)"
            price = price_product(path,soup)+ "/1kg"
        elif (product == "cá lóc"):
            path = "#post-501 > div > figure.wp-block-table.aligncenter > table > tbody > tr:nth-child(4) > td:nth-child(5)"
            price = price_product(path,soup)+ "/1kg"
        elif (product == "cá điêu hông"):
            path = "#post-501 > div > figure.wp-block-table.aligncenter > table > tbody > tr:nth-child(5) > td:nth-child(5)"
            price = price_product(path,soup)+ "/1kg"
        elif (product == "cá rô phi"):
            path = "#post-501 > div > figure.wp-block-table.aligncenter > table > tbody > tr:nth-child(6) > td:nth-child(5)"
            price = price_product(path,soup)+ "/1kg"
        elif (product == "cá bống"):
            path = "#post-501 > div > figure.wp-block-table.aligncenter > table > tbody > tr:nth-child(7) > td:nth-child(5)"
            price = price_product(path,soup)+ "/1kg"
        elif (product == "cá kèo"):
            path = "#post-501 > div > figure.wp-block-table.aligncenter > table > tbody > tr:nth-child(8) > td:nth-child(5)"
            price = price_product(path,soup)+ "/1kg"
        elif (product == "cá thát lát"):
            path = "#post-501 > div > figure.wp-block-table.aligncenter > table > tbody > tr:nth-child(9) > td:nth-child(5)"
            price = price_product(path,soup)+ "/1kg"
        elif (product == "cá mú"):
            path = "#post-501 > div > figure.wp-block-table.aligncenter > table > tbody > tr:nth-child(10) > td:nth-child(5)"
            price = price_product(path,soup)+ "/1kg"
        elif (product == "cá nục"):
            path = "#post-501 > div > figure.wp-block-table.aligncenter > table > tbody > tr:nth-child(11) > td:nth-child(5)"
            price = price_product(path,soup)+ "/1kg"
        elif (product == "cá chim"):
            path = "#post-501 > div > figure.wp-block-table.aligncenter > table > tbody > tr:nth-child(12) > td:nth-child(5)"
            price = price_product(path,soup)+ "/1kg"
        elif (product == "tôm"):
            path = "#post-501 > div > figure.wp-block-table.aligncenter > table > tbody > tr:nth-child(13) > td:nth-child(5)"
            price = price_product(path,soup)+ "/1kg"
        elif (product == "mực"):
            path = "#post-501 > div > figure.wp-block-table.aligncenter > table > tbody > tr:nth-child(14) > td:nth-child(5)"
            price = price_product(path,soup)+ "/1kg"
        elif (product == "nghêu"):
            path = "#post-501 > div > figure.wp-block-table.aligncenter > table > tbody > tr:nth-child(15) > td:nth-child(5)"
            price = price_product(path,soup)+ "/1kg"
        elif (product == "tôm càng xanh"):
            path = "#post-501 > div > figure.wp-block-table.aligncenter > table > tbody > tr:nth-child(16) > td:nth-child(5)"
            price = price_product(path,soup)+ "/1kg"
        elif (product == "tôm thẻ"):
            path = "#post-501 > div > figure.wp-block-table.aligncenter > table > tbody > tr:nth-child(17) > td:nth-child(5)"
            price = price_product(path,soup)+ "/1kg"
        elif (product == "tôm hùng"):
            path = "#post-501 > div > figure.wp-block-table.aligncenter > table > tbody > tr:nth-child(18) > td:nth-child(5)"
            price = price_product(path,soup)+ "/1kg"
        elif (product == "thịt ba chỉ"):
            path = "#post-501 > div > figure:nth-child(9) > table > tbody > tr:nth-child(2) > td:nth-child(4)"
            price = price_product(path,soup)+ "/1kg"
        elif (product == "sườn non"):
            path = "#post-501 > div > figure:nth-child(9) > table > tbody > tr:nth-child(3) > td:nth-child(4)"
            price = price_product(path,soup)+ "/1kg"
        elif (product == "nạc thăn"):
            path = "#post-501 > div > figure:nth-child(9) > table > tbody > tr:nth-child(4) > td:nth-child(4)"
            price = price_product(path,soup)+ "/1kg"
        elif (product == "thịt lơn xay"):
            path = "#post-501 > div > figure:nth-child(9) > table > tbody > tr:nth-child(5) > td:nth-child(4)"
            price = price_product(path,soup)+ "/1kg"
        elif (product == "thịt nạc vai"):
            path = "#post-501 > div > figure:nth-child(9) > table > tbody > tr:nth-child(6) > td:nth-child(4)"
            price = price_product(path,soup)+ "/1kg"
        elif (product == "thịt bò úc"):
            path = "#post-501 > div > figure:nth-child(9) > table > tbody > tr:nth-child(7) > td:nth-child(4)"
            price = price_product(path,soup)+ "/1kg"
        elif (product == "gầu bò"):
            path = "#post-501 > div > figure:nth-child(9) > table > tbody > tr:nth-child(8) > td:nth-child(4)"
            price = price_product(path,soup)+ "/1kg"
        elif (product == "thăn bò"):
            path = "#post-501 > div > figure:nth-child(9) > table > tbody > tr:nth-child(9) > td:nth-child(4)"
            price = price_product(path,soup)+ " /1kg"
        elif (product == "thịt bò xay"):
            path = "#post-501 > div > figure:nth-child(9) > table > tbody > tr:nth-child(10) > td:nth-child(4)"
            price = price_product(path,soup)+ " /1kg"
        elif (product == "bắp bò loại 1"):
            path = "#post-501 > div > figure:nth-child(9) > table > tbody > tr:nth-child(11) > td:nth-child(4)"
            price = price_product(path,soup)+ " /1kg"
        elif (product == "thịt gà"):
            path = "#post-501 > div > figure:nth-child(9) > table > tbody > tr:nth-child(12) > td:nth-child(4)"
            price = price_product(path,soup)+ " /1kg"
        elif (product == "chân gà" or product == "Chân Gà"):
            path = "#post-501 > div > figure:nth-child(9) > table > tbody > tr:nth-child(13) > td:nth-child(4)"
            price = price_product(path,soup)+ " /1kg"
        elif (product == "thịt gà công nghiệp"):
            path = "#post-501 > div > figure:nth-child(9) > table > tbody > tr:nth-child(14) > td:nth-child(4)"
            price = price_product(path,soup) + " /1kg"
        elif (product == "gà ta nguyên con"):
            path = "#post-501 > div > figure:nth-child(9) > table > tbody > tr:nth-child(15) > td:nth-child(4)"
            price = price_product(path,soup) + " /1kg"
        elif (product == "vàng"):
            url = "https://www.pnj.com.vn/blog/gia-vang/"
            r = requests.get(url)
            soup = BeautifulSoup(r.content, "html.parser")
            path = "#content-price > tr:nth-child(1) > td:nth-child(3) > span"
            price = price_product(path,soup) + "(1000đ/Chỉ)"
        else:
            price = "xin lỗi mặt hàng này tôi chưa cập nhật"

        dispatcher.utter_message(price)
        return []


class ActionAccesssmap(Action):
    def name(self):
        return "action_find_map"

    def run(self, dispatcher, tracker, domain):
        location = tracker.get_slot("location")
        driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        driver.get("https://www.google.com/maps/@9.779349,105.6189045,11z?hl=vi-VN")
        Place = driver.find_element(By.CLASS_NAME,"tactile-searchbox-input")
        Place.send_keys(location)
        Submit = driver.find_element(By.XPATH,"/html/body/div[3]/div[9]/div[3]/div[1]/div[1]/div[1]/div[2]/div[1]/button")
        Submit.click()
        sleep(2)
        directions = driver.find_element(By.XPATH,"/html/body/div[3]/div[9]/div[9]/div/div/div[1]/div[2]/div/div[1]/div/div/div[4]/div[1]/button")
        directions.click()
        sleep(3)
        find = driver.find_element(By.XPATH,"/html/body/div[3]/div[9]/div[3]/div[1]/div[2]/div/div[3]/div[1]/div[1]/div[2]/div[1]/div/input")
        find.send_keys("đông hà , đức linh , bình thuận")
        search = driver.find_element(By.XPATH,"/html/body/div[3]/div[9]/div[3]/div[1]/div[2]/div/div[3]/div[1]/div[1]/div[2]/button[1]")
        search.click()
        sleep(15)
        dispatcher.utter_message(text=f"tôi đã tìm một số con đường")
        return []



class ActionAccesstranpslate(Action):
    def name(self):
        return "action_transplate"

    def run(self, dispatcher, tracker, domain):
        translate = Translator()
        language = tracker.get_slot("language")
        result = translate.translate(language, src='en', dest='vi')
        a = "bản dịch: "  + result.text
        dispatcher.utter_message(a)
        return []



