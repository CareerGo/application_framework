'''
########################################################################################

                            Selenium AutoFill Template

    Version:            N/A  
    Author:             Chiver Wan 
    Functionality:      Template for all companies after Logging in

########################################################################################
'''
import pytest
import time
import json
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys
# Deals with selection 
from selenium.webdriver.support.ui import Select    
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities


class AutoFill(object):
    def __init__(self, usr_info, job_instance):
        self.init_selenium() 
        self.job_instance = job_instance 
        self.usr_info = usr_info         
        self.url = job_instance["url_key"]  
    
    def init_selenium(self):
        self.driver = webdriver.Chrome()
        self.vars = {}

    # For Debug Use : see all selection options
    def getSelections(self): 
        pass
        
    # For Debug Use : see all upload options
    def getUploads(self): 
        pass

    # For Debug Use : see all text input options
    def getTexts(self): 
        pass

    # Main Functionality: fill the form 
    def fill(self):
        pass 
        self.driver.quit()

def main(): 
    usrInfo = dict() 
    jobInst = {
        "url_key": "https://www.hudsonrivertrading.com/careers/job/?gh_jid=75806"
    }
    tmp = AutoFill(usrInfo, jobInst) 
    tmp.getTexts() 


if __name__ == '__main__': 
    main() 