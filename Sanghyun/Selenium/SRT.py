from selenium import webdriver
# from html_table_parser import parser_functions as parser
# from bs4 import BeautifulSoup
# import pandas as pd
# from urllib.request import urlopen
from bs4 import BeautifulSoup as bs


from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(ChromeDriverManager().install())
#
# driver.get('https://etk.srail.kr/cmc/01/selectLoginForm.do?pageId=TK0701000000')

url = "http://www.naver.com" # http://www.naver.com 같은거
html = urlopen(url)
source = html.read()
html.close()

soup = bs(source, "html5lib") # BeautifulSoup 객체생성





#
# while(True):
#     print("After Login, Do you go to the page with the seat you want? (y/n)")
#     a = input()
#     if(a == 'y' or a == 'Y'):
#         break
#
# driver.implicitly_wait(1)
# doc = driver.page_source
# soup = BeautifulSoup(doc, 'html.parser')
# temp = soup.find_all('table')
# p = parser.make2d(temp[0])
# print(p[0][0])
# print("No." + "\t" + p[1][2] + "\t" + p[1][3] + "\t" + p[1][4] + "\t : 호실")
# count = 1
# select = []
# for i in range(2, len(p)):
#     if(p[i][5] == "매진"):
#         print(str(count) + "\t" + p[i][2] + "\t" +
#               p[i][3] + "\t" + p[i][4] + "\t : 특실")
#         select.append([i, 1, False])
#         count += 1
#     if(p[i][6] == "매진"):
#         print(str(count) + "\t" + p[i][2] + "\t" + p[i]
#               [3] + "\t" + p[i][4] + "\t : 일반실")  # i 1 == 2
#         select.append([i, 2, False])
#         count += 1
#
# print("\nInput Num you want.(ex: 1,4)")
# a = input()
# aa = a.split(",")
#
# for i in aa:
#     select[int(i)-1][2] = True
# #
# while(True):
#     driver.refresh()
#     driver.implicitly_wait(2)
#     for i in select:
#         if(i[2] == True):
#             txt = ""
#             if (i[1] == 1):
#                 txt = driver.find_element_by_xpath(
#                     "//*[@id=\"result-form\"]/fieldset/div[6]/table/tbody/tr["+str(i[0]-1)+"]/td[6]/a/span").text
#                 a = driver.find_element_by_xpath(
#                     "//*[@id=\"result-form\"]/fieldset/div[6]/table/tbody/tr["+str(i[0]-1)+"]/td[6]/a")
#             elif (i[1] == 2):
#                 txt = driver.find_element_by_xpath(
#                     "//*[@id=\"result-form\"]/fieldset/div[6]/table/tbody/tr["+str(i[0]-1)+"]/td[7]/a/span").text
#                 a = driver.find_element_by_xpath(
#                     "//*[@id=\"result-form\"]/fieldset/div[6]/table/tbody/tr[" + str(i[0]-1) + "]/td[7]/a")
#
#             if(txt == "예약하기"):
#                 a.click()
#                 break
