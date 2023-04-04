import unittest
from time import sleep
from unittest import TestCase
from webbrowser import Error

from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.select import Select



def send_keys(param):
    pass




class EmagTest(TestCase):
    def setUp(self):
        self.chrome = webdriver.Chrome(ChromeDriverManager().install())
        self.chrome.get('https://www.emag.ro/')
        self.chrome.maximize_window()

    def tearDown(self):
        self.chrome.quit()

    def test_url(self):
        actual = self.chrome.current_url
        expected = 'https://www.emag.ro/'
        self.assertEqual(expected, actual, 'Url incorect')

    def test_geniuslinktext_url(self):
        self.chrome.find_element(By.LINK_TEXT, 'Genius').click()
        actual = self.chrome.current_url
        expected = 'https://www.emag.ro/genius?ref=hdr_genius'
        self.assertEqual(expected, actual, 'Url incorect')

    def test_butonuldelogare(self):
        self.chrome.find_element(By.ID,'my_account').click()
        self.chrome.find_element(By.ID,"user_login_email").send_keys('razvan22@gmail.com')
        expected='https://auth.emag.ro/user/validate-mfa'
        self.assertTrue('Se pare ca nu ai un cont emag')

    def test_logarecugoogle(self):
        self.chrome.find_element(By.ID, 'my_account').click()
        self.chrome.find_element(By.NAME, 'social_init_google').click()
        self.chrome.find_element(By.NAME,'identifier').send_keys('catalindavidescu46@gmail.com')
        actual='https://auth.emag.ro/user/login'
        self.assertTrue('introdu parola contului tau emag')

    def test_baradecautare(self):
        self.chrome.find_element(By.NAME,'query').click()
        self.chrome.find_element(By.NAME,'query').send_keys('acer nitro 5')
        actual=self.chrome.current_url
        expected='https://www.emag.ro/laptop-gaming-acer-nitro-5-an515-57-cu-procesor-intelr-coretm-i7-11800h-pana-la-4-60-ghz-15-6-full-hd-ips-144hz-16gb-512gb-ssd-nvidiar-geforce-rtxtm-3050ti-4gb-no-os-black-nh-qesex-008/pd/DZ5RGLMBM/?X-Search-Id=6fb1a35eb49696313dc4&X-Product-Id=102001327&X-Search-Page=1&X-Search-Position=3&X-Section=search&X-MB=0&X-Search-Action=view'
        self.assertTrue('Am gasit 216 rezultate')

    def test_emagajutorclienti(self):
        self.chrome.find_element(By.XPATH,"//a[normalize-space()='eMAG Help']").click()
        self.chrome.find_element(By.XPATH,"//input[@autocomplete='off']").click()
        self.chrome.find_element(By.XPATH, "//input[@autocomplete='off']").send_keys('cont nou')
        actual=self.chrome.current_url
        expected='https://www.emag.ro/help/search/?q=cont%20nou'
        self.assertTrue('Salut cu ce te putem ajuta?')

    def test_cosdecumparaturi(self):
        self.chrome.find_element(By.ID,'searchboxTrigger').send_keys('Televizor Samsung LED 65AU7092')
        self.chrome.find_element(By.XPATH," //i[@class='em em-search']").click()
        self.chrome.find_element(By.XPATH," //a[contains(text(),'Televizor Samsung LED 65AU7092, 163 cm, Smart, 4K ')]").click()
        self.chrome.find_element(By.XPATH,"//button[contains(text(),'Adauga in Cos')]").click()
        self.chrome.find_element(By.ID, 'my_cart').click()
        actual='https://www.emag.ro/cart/products?ref=cart'
        self.assertTrue('Cost produse: 2.749,90 Lei')

    def test_modalitatideplata(self):
        self.chrome.find_element(By.ID, 'my_cart').click()
        self.chrome.find_element(By.CSS_SELECTOR," a[href='/help/modalitati-de-plata']").click()
        self.chrome.find_element(By.XPATH," //p[normalize-space()='Card bancar']").click()
        actual=self.chrome.current_url
        expected='https://www.emag.ro/help/modalitati-de-plata#pay-with-credit-card'
        self.assertEqual(actual,expected,'card bancar')

    def test_oferteemag(self):
        self.chrome.find_element(By.CSS_SELECTOR,"a[title='Ofertele eMAG']").click()
        self.chrome.find_element(By.XPATH,"//section[2]//div[1]//div[1]//div[1]//a[1]//div[1]//div[1]//img[1]").click()
        self.chrome.find_element(By.XPATH," //a[normalize-space()='Imprimante si scannere']").click()
        self.chrome.find_element(By.XPATH,"/html[1]/body[1]/div[3]/div[2]/div[1]/section[1]/div[1]/div[5]/div[2]/div[5]/div[14]/div[1]/div[1]/div[3]/div[1]/h2[1]/a[1]")
        self.assertTrue('-28%')


    def test_revenirelapaginaanterioara(self):
        self.chrome.find_element(By.LINK_TEXT,"Canapea extensibila cu lada depozitare Medeea Modella, gri/negru, 215 x 80 x 80 cm").click()
        self.chrome.find_element(By.XPATH,"//body/div[3]/nav[2]/div[1]/div[1]/div[1]/a[1]/img[1]") .click()
        acual='https://www.emag.ro/canapea-extensibila-cu-lada-depozitare-medeea-modella-gri-negru-215-x-80-x-80-cm'
        expected=self.chrome.current_url
        self.assertTrue('prima pagina')

    def test_stergedinfavorite(self):
        self.chrome.find_element(By.XPATH,"//div[@class='container']//div//div[1]//div[1]//div[1]//div[2]//div[1]//div[1]//div[3]//div[1]//h2[1]//a[1]").click()
        self.chrome.find_element(By.CSS_SELECTOR,"div.main-container-outer:nth-child(15) div.main-container-inner:nth-child(5)").click()
        self.chrome.find_element(By.XPATH,"//span[normalize-space()='Favorite']").click()
        actual=self.chrome.current_url
        expected=('https://www.emag.ro/favorites?ref=ua_favorites')
        self.assertEqual(actual,expected,'operatia nu se poate face fara logare')

    def test_logarefacebook(self):
        self.chrome.find_element(By.CSS_SELECTOR,"a[id='my_account'] span[class='visible-lg-inline visible-xl-inline']").click()
        self.chrome.find_element(By.XPATH,"(//button[normalize-space()='Facebook'])[1]").click()
        self.chrome.find_element(By.ID,"email").send_keys('cuminede18@yahoo.com')
        self.chrome.find_element(By.ID,'pass').send_keys('Mayradarin@2023')
        self.assertTrue('cont Davidescu Catalin')

    