from selenium import webdriver
from selenium.webdriver.common.keys import Keys

class ShoppingOnInternet():
    def __init__(self):
        self.browser = input( '어떤 브라우저를 선택하시겠습니까?')

    def get_brower(self):
        while True:
            if self.browser in "c":
                self.driver = webdriver.Chrome('chromedriver.exe')
                break
            else:
                self.brwser = input("다시 입력해주세요")
            continue

        

    #로그인 정보
    def login_tohomepage(self):
        #로그인 정보 입력
        id = 'Hyun6467'
        pw = '1Q2W3E!!'
        xpaths = {'id':"//input[@name='id']", 'pw': "//input[@name='pwd']" }

        self.driver.find_element_by_class_name("link__usermenu").click()
            
        # 2. 로그인 정보 넣기
        self.driver.find_element_by_xpath(xpaths['id']).send_keys(id)
        self.driver.find_element_by_xpath(xpaths['pw']).send_keys(pw)

        # 3. 로그인 버튼 클릭릭
        self.driver.find_element_by_class_name("button_login").click()


    #g마켓 브라우져 넣기
    def invoke_brower(self):                
        url = "http://www.gmarket.co.kr"
        self.driver.get(url)
        self.driver.save_screenshot('1_brower_on.png')
        
        self.driver.find_element_by_xpath("/html/body/div/div[2]/div/div/div/div/div[2]/div[3]/ul/li[1]/a")

        try:
            print('> try ~ except')
        except "G마켓 - 쇼핑을 다 담다." not in self.driver.title:
            f = open('exception.txt', 'rw')
            f.write('Not exect title in driver.title\n')
            f.close()

    
    def buy_goods(self):
        self.driver.find_element_by_name("keyword").clear()
        self.driver.find_element_by_name("keyword").send_keys(u"대통령의 말하기")
        self.driver.find_element_by_css_selector("button.button__search").click()
        self.driver.implicitly_wait(3)

        # 2. 검색 결과 중 상품 선택
        self.driver.find_element_by_css_selector("span.text__item").click()

    # def tear_down(self):
    #     opened_window_list = self.driver.window_handles

    #     # 열려있는 모든 window 로그아웃
    #     index = len(opened_window_list)

    #     self.driver.switch_to_window(self.driver.window_handles[index-1])
    #     index = index -1
    #     self.driver.find_element_by_xpath("//span{@class='myinfo']/a").click()
    #     self.driver.close()
        
if __name__ == "__main__":
        shopping = ShoppingOnInternet()
        shopping.get_brower()
        shopping.invoke_brower()
        shopping.login_tohomepage()
        shopping.buy_goods()
        shopping.tear_down()






