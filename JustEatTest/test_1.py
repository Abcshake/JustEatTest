import unittest
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ExpectedCondition
import re 

class Just_East_Test(unittest.TestCase):
    def test_A(self):
        
        postalCode = "AR51 1AA"
        location = r"C:\Users\Owner\source\repos\JustEatTest\JustEatTest\chromedriver.exe"
        driver = webdriver.Chrome(location)
        driver.get('http://www.just-eat.co.uk/')
        wait = WebDriverWait(driver,60)

        #Finds Postal code address box and enters Postal code
        postalCodeEntry = wait.until(ExpectedCondition.element_to_be_clickable((By.XPATH,"//input[@data-test-id='address-box-input']")))
        postalCodeEntry.send_keys(postalCode)

        #Clicks submit
        submitButton = wait.until(ExpectedCondition.element_to_be_clickable((By.XPATH,"//button[@data-test-id='find-restaurants-button']")))
        submitButton.click()

        #Verifies that user is navigated to an url with an areavode
        self.assertEqual(True,wait.until(ExpectedCondition.url_contains("https://www.just-eat.co.uk/area/")))

        #Finds location header and verifies that location header included the Postal code entered
        locationHeader =  wait.until(ExpectedCondition.presence_of_element_located((By.XPATH,"//h1[@class='c-dishSearch-locationHeader-title']")))
        self.assertEqual(True,wait.until(ExpectedCondition.text_to_be_present_in_element((By.XPATH,"//h1[@class='c-dishSearch-locationHeader-title']"), postalCode)))

        #Find search count header on top listed restaurants and verifies that search count included open restaurants
        searchCount =  wait.until(ExpectedCondition.presence_of_element_located((By.XPATH,"//h1[@class='c-dishSearch-contentHeader']")))
        self.assertEqual(True,wait.until(ExpectedCondition.text_to_be_present_in_element((By.XPATH,"//h1[@class='c-dishSearch-contentHeader']/span[2]"), "open restaurants")))

if __name__ == '__main__':
    unittest.main()
