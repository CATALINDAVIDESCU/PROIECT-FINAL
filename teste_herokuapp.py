import unittest
from unittest import TestCase

from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager



def send_keys(param):
    pass


class HerokuappTest(TestCase):
    def setUp(self):
        self.chrome = webdriver.Chrome(ChromeDriverManager().install())
        self.chrome.get('https://the-internet.herokuapp.com/')
        self.chrome.maximize_window()
        self.chrome.implicitly_wait(3)

    def tearDown(self):
        self.chrome.quit()

    def test_url(self):
        actual = self.chrome.current_url
        expected = 'https://the-internet.herokuapp.com/'
        self.assertEqual(expected, actual, 'Url incorect')

    def test_addremovelinktxt_url(self):
        self.chrome.find_element(By.LINK_TEXT, 'Add/Remove Elements').click()
        actual = self.chrome.current_url
        expected = 'https://the-internet.herokuapp.com/add_remove_elements/'
        self.assertEqual(expected, actual, 'Url incorect')

    def test_header_addremoveelement(self):
        self.chrome.find_element(By.LINK_TEXT, 'Add/Remove Elements').click()
        actual= self.chrome.find_element(By.CSS_SELECTOR, 'h3').text
        expected = 'Add/Remove Elements'
        self.assertEqual(expected, actual, "text incorect")

    def test_press_addelementbutton(self):
        self.chrome.find_element(By.LINK_TEXT,'Add/Remove Elements').click()
        self.chrome.find_element(By.CSS_SELECTOR,'button').click()
        actual = self.chrome.find_element(By.ID,"elements").text
        expected ='Delete'

    def test_press_deletebutton(self):
        self.chrome.find_element(By.LINK_TEXT, 'Add/Remove Elements').click()
        self.chrome.find_element(By.CSS_SELECTOR, 'button').click()
        self.chrome.find_element(By.CSS_SELECTOR,'.added-manually').click()
        actual= 'https://the-internet.herokuapp.com/add_remove_elements/'
        expected= "Delete button removed"

    def test_find_hidenelement(self):
        self.chrome.find_element(By.LINK_TEXT,'Dynamic Loading').click()
        self.chrome.find_element(By.LINK_TEXT,'Example 1: Element on page that is hidden').click()
        self.chrome.find_element(By.XPATH,'//button[contains(text(),"Start")]').click()
        expected=self.chrome.current_url
        actual='https://the-internet.herokuapp.com/dynamic_loading/1'
        self.assertTrue('Hello World')

    def test_enablebutton(self):
        self.chrome.find_element(By.XPATH,"//a[normalize-space()='Dynamic Controls']").click()
        self.chrome.find_element(By.XPATH,"//button[normalize-space()='Enable']").click()
        self.assertTrue("It's enabled")

    def test_geolocation(self):
        self.chrome.find_element(By.CSS_SELECTOR,"a[href='/geolocation']").click()
        self.chrome.find_element(By.XPATH,"//button[@onclick='getLocation()']").click()
        actual='https://the-internet.herokuapp.com/geolocation'
        expected=self.chrome.current_url
        self.assertTrue('Latitude 47.1584596,Longitude27.6014634 ')

    def test_httpstatuscode(self):
        self.chrome.find_element(By.CSS_SELECTOR,"a[href='/status_codes']").click()
        self.chrome.find_element(By.XPATH,"//a[normalize-space()='404']").click()
        acual='https://the-internet.herokuapp.com/status_codes/404'
        self.assertTrue('This page returned a 404 status code.')

    def test_findimage(self):
        self.chrome.find_element(By.XPATH,"//a[normalize-space()='Shifting Content']").click()
        self.chrome.find_element(By.CSS_SELECTOR,"a[href='/shifting_content/image']").click()
        actual=self.chrome.current_url
        expected='https://the-internet.herokuapp.com/shifting_content/image'
        self.assertTrue('Shifting Content: Image')

    def test_returntohomepage(self):
        self.chrome.find_element(By.XPATH,"//a[normalize-space()='Shifting Content']").click()
        self.chrome.find_element(By.LINK_TEXT,"Example 1: Menu Element").click()
        self.chrome.find_element(By.XPATH,"//a[normalize-space()='Home']").click()
        actual=self.chrome.current_url
        expected='https://the-internet.herokuapp.com/shifting_content/menu'
        self.assertTrue('am revenit pe prima pagina')

    def test_fileupload(self):
        self.chrome.find_element(By.LINK_TEXT,'File Upload').click()
        self.chrome.find_element(By.ID,"file-submit").click()
        actual=self.chrome.current_url
        expected='https://the-internet.herokuapp.com/upload'
        self.assertEqual(expected,actual,'internal server error')

