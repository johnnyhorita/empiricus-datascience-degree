# Generated by Selenium IDE
import pytest
import time
import json
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

class TestDddddd():
  def setup_method(self, method):
    self.driver = webdriver.Chrome()
    self.vars = {}
  
  def teardown_method(self, method):
    self.driver.quit()
  
  def test_dddddd(self):
    self.driver.get("http://estatisticas.cetip.com.br/astec/series_v05/paginas/lum_web_v05_template_informacoes_di.asp?str_Modulo=completo&int_Idioma=1&int_Titulo=6&int_NivelBD=2")
    self.driver.set_window_size(1552, 849)
    self.driver.find_element(By.ID, "divContainerIframeBmf").click()
    self.driver.find_element(By.NAME, "DT_DIA_DE").send_keys("01")
    self.driver.find_element(By.NAME, "DT_MES_DE").send_keys("06")
    self.driver.find_element(By.NAME, "DT_ANO_DE").send_keys("2021")
    self.driver.find_element(By.NAME, "DT_DIA_ATE").send_keys("30")
    self.driver.find_element(By.NAME, "DT_MES_ATE").send_keys("06")
    self.driver.find_element(By.NAME, "chk_M1").click()
    self.driver.find_element(By.NAME, "chk_M2").click()
    self.driver.find_element(By.CSS_SELECTOR, ".row:nth-child(5) > .large-12").click()
    self.driver.find_element(By.NAME, "chk_M3").click()
    self.driver.find_element(By.NAME, "chk_M4").click()
    self.driver.find_element(By.NAME, "chk_M5").click()
    self.driver.find_element(By.NAME, "chk_M6").click()
    self.driver.find_element(By.CSS_SELECTOR, ".button:nth-child(2)").click()
  
