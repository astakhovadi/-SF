

import pytest
from telnetlib import EC
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


@pytest.fixture(autouse=True)
def testing():
   pytest.driver = webdriver.Chrome(executable_path=r'D:/skillfactory/chromedriver.exe')
   pytest.driver.implicitly_wait(10) #неявное ожидание
   # Переходим на страницу авторизации
   pytest.driver.get('http://petfriends1.herokuapp.com/login')

   yield

   pytest.driver.quit()



def test_my_pets():
   # Вводим email
   pytest.driver.find_element_by_id('email').send_keys('<valid_email>')
   # Вводим пароль
   pytest.driver.find_element_by_id('pass').send_keys('<valid_pass>')
   # Нажимаем на кнопку входа в аккаунт
   pytest.driver.find_element_by_css_selector('button[type="submit"]').click()
   # Проверяем, что мы оказались на главной странице пользователя
   assert pytest.driver.find_element_by_tag_name('h1').text == "PetFriends"

   images = pytest.driver.find_elements_by_css_selector('.card-deck .card-img-top')#Смотрим инфо фото
   names = pytest.driver.find_elements_by_css_selector('.card-deck .card-title')#Смотрим инфо имен
   descriptions = pytest.driver.find_elements_by_css_selector('.card-deck .card-text')#Смотрим инфо видов и возрастов

   for i in range(len(names)):
      #Проверяем наличие фото
      pytest.driver.implicitly_wait(10)  # неявное ожидание
      assert images[i].get_attribute('src') != ''
      # Проверяем наличие имени
      pytest.driver.implicitly_wait(10) # неявное ожидание
      assert names[i].text != ''
      # Проверяем наличие возраста и вида
      pytest.driver.implicitly_wait(10)  # неявное ожидание
      assert descriptions[i].text != ''
      assert ', ' in descriptions[i]
      parts = descriptions[i].text.split(", ")
      assert len(parts[0]) > 0
      assert len(parts[1]) > 0

   # Ожидаем появление поля со статистикой
   element = WebDriverWait(pytest.driver, 10).until(
      EC.presence_of_element_located((By.CSS_SELECTOR, ".\\.col-sm-4.left")))

  # Сохраняем в переменную ststistic элементы статистики
   statistic = pytest.driver.find_elements_by_css_selector(".\\.col-sm-4.left")


   # Получаем количество питомцев из данных статистики
   number = statistic[0].text.split('\n')
   number = number[1].split(' ')
   number = int(number[1])


   assert number > (len(images)-1)/2  #Проверяем, что кол-во фотографий = числу кол-ва питомцев из статистики (Задание 25.3.2)
   assert names == number   # Проверяем, что имен = числу питомцев (Задание 25.3.1)
   assert descriptions == number  # Проверяем, что у каждого питомца есть возраст и вид (Задание 25.3.3)

