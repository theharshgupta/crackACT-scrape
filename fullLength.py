import math 
import pdfkit
import time
import re
import urllib2
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select

driver = webdriver.Chrome()

with open("alist6.txt") as f:
	for line in f:
		m = re.search('/d/(.+?)/vi', str(line)).group(1)
		if m:	
			print str(m)
			link = "https://drive.google.com/uc?export=download&id=" + str(m)
			driver.get(l)

