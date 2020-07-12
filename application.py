
'''
########################################################################################

                            Application Framework

    Version:            v1.0
    Author:             Chiver Wan 
    Functionality:      Top level code that decides the application process: 
                        1. To signup or 
                        2. To login and fill page

########################################################################################
'''

# Dynamic Load Modules 
import importlib

class Application(object):
    def __init__(self, usr_info, company_instance, job_instance):
        self.usr_info = usr_info 
        self.company_instance = company_instance
        self.job_instance = job_instance
        self.company_id = company_instance["id"] 

    '''
    If the company needs to signup an account, 
    return True, else False 
    '''
    def control(self, usr_info, company_instance):
        if company_instance["requires_signup"]: 
            if self.company_id in usr_info["signed_up_companies"]: 
                self.assign_process(False) 
            else: 
                self.assign_process(True) 
        else: 
            self.assign_process(False) 

    '''
    Execute Application Process Based on Script
    '''
    def assign_process(self, need_signup): 
        if need_signup: 
            # signup 
            signup_module = importlib.import_module(self.company_id + "_signup")
            signup_module.SignUp(self.usr_info, self.job_instances).signup()  
        else: 
            # apply 
            # Import corresponding selenium script 
            fill_module = importlib.import_module(self.company_id + "_fill")
            fill_module.AutoFill(self.usr_info, self.job_instances).fill() 


'''
def main():
    testUrl = "https://www.hudsonrivertrading.com/careers/job/?gh_jid=75806"
    usrInfo = {
        "firstname": "Lucas",
        "lastname": "Liu",
        "email": "ll@gmail.com",
        "phone": "4128723333"
    }
    application = Application()

if __name__ == '__main__': 
    main() 
'''
