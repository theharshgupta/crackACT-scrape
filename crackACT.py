import pdfkit
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
from PIL import Image

config = pdfkit.configuration(wkhtmltopdf="C:\\Program Files\\wkhtmltopdf\\bin\\wkhtmltopdf.exe")

options = {
    'page-size': 'a4'
    }

# For english ACT tests that are not uploaded as PDF on crackACT 
driver = webdriver.Chrome()
i=0
# Since there are approx. 88 tests on crackACT website
for x in xrange(301,389):
    pdfkit.from_url('http://www.crackact.com/act/english/test' + str(x) + '.html', str(x-300) + 'Passage.pdf' , configuration=config, options=options)
    driver.get('http://www.crackact.com/act/english/test' + str(x) + '.html')
    driver.find_element_by_xpath("//input[@value='SUBMIT']").submit()
    driver.full_screen()
    driver.save_screenshot('C:\\Users\\hmgca\\Desktop\\ACT\\Books\\EnglishcrackACTANSWERS\\' + 'Answer'+ str(x-300) + '.png')
