from time import sleep
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import sys


def main():

    path=r"geckodriver.exe"
    ID="id"
    PASS="pass"
    subject_code="so2s01"


    #tutorial=1


    
    driver = webdriver.Firefox()
    driver.get("https://www38.polyu.edu.hk/eStudent/login.jsf")
     
    input_box = driver.find_element_by_xpath("""//*[@id="login-form"]/table/tbody/tr[2]/td[4]/input[1]""")
    input_box.send_keys(ID)
    
    input_box_password = driver.find_element_by_xpath("""//*[@id="login-form"]/table/tbody/tr[3]/td[3]/input""")
    input_box_password.send_keys(PASS)

    enter_button = driver.find_element_by_xpath("""//*[@id="login-button"]""")
    enter_button.click()

    subject_reg = driver.find_element_by_xpath("""//*[@id="home-left-panel"]/ul/li[3]/ul/li[3]/a""")
    subject_reg.click()

    try:
        scroll_button = driver.find_element_by_xpath("""//*[@id="mainForm:yearSemDropDown"]""")
        scroll_button.click()
        scroll_button.send_keys(Keys.DOWN + Keys.ENTER)
    except:
        pass

    GO_button = driver.find_element_by_xpath("""//*[@id="mainForm:nextButton"]""")
    GO_button.click()

    search_bar = driver.find_element_by_xpath("""//*[@id="mainForm:basicSearchSubjectCode"]""")
    search_bar.send_keys(subject_code)

    search_GO = driver.find_element_by_xpath("""//*[@id="mainForm:basicSearchButton"]""")
    search_GO.click()

    while(1):
        try:
            REPEAT=1
            while(REPEAT==1):

                
                while(1):
                    vac = driver.find_element_by_xpath("""//*[@id="mainForm:basicSearchTable:0:basicSearchSubjectGroup_"]""").text
                    if("(0)" in vac):
                        driver.get("https://www38.polyu.edu.hk/eStudent/secure/my-subject-registration/subject-register-select-subject.jsf")
                        sleep(1)
                    else:
                        break

                add_button = driver.find_element_by_xpath("""//*[@id="mainForm:basicSearchTable:0:basicSearchAddSubjectButton_"]""")
                add_button.click()
                sleep(1)
                while(1):
                    novac=1
                    LAB001 = driver.find_element_by_xpath("""//*[@id="mainForm:ComponentTable:0:selectCompVacancies_"]""").text
                    print(LAB001)
                    if LAB001!="0":
                        driver.find_element_by_xpath("""//*[@id="mainForm:ComponentTable:0:selectCompSelected_"]""").click()
                        break
                    
                    LAB002 = driver.find_element_by_xpath("""//*[@id="mainForm:ComponentTable:1:selectCompVacancies_"]""").text
                    if LAB002!="0":
                        driver.find_element_by_xpath("""//*[@id="mainForm:ComponentTable:1:selectCompSelected_"]""").click()
                        break
                        
                    LAB003 = driver.find_element_by_xpath("""//*[@id="mainForm:ComponentTable:2:selectCompVacancies_"]""").text
                    if LAB003!="0":
                        driver.find_element_by_xpath("""//*[@id="mainForm:ComponentTable:2:selectCompSelected_"]""").click()
                        break
                        
                    LAB004 = driver.find_element_by_xpath("""//*[@id="mainForm:ComponentTable:3:selectCompVacancies_"]""").text
                    if LAB004!="0":
                        driver.find_element_by_xpath("""//*[@id="mainForm:ComponentTable:3:selectCompSelected_"]""").click()
                        break
                    novac=0
                    break
                if(novac==1):

                    lec_box = driver.find_element_by_xpath("""//*[@id="mainForm:ComponentTable:4:selectCompSelected_"]""")
                    lec_box.click()

                    tut_box = driver.find_element_by_xpath("""//*[@id="mainForm:ComponentTable:"""+str(tutorial)+""":selectCompSelected_"]""")
                    tut_box.click()

                    add_to_cart = driver.find_element_by_xpath("""//*[@id="mainForm:selectButton"]""")
                    add_to_cart.click()
                        
                    preview = driver.find_element_by_xpath("""//*[@id="mainForm:confirmButton"]""")
                    preview.click()

                    confirm = driver.find_element_by_xpath("""//*[@id="mainForm:confirmButton"]""")
                    #confirm.click()

                    if("ERROR" in driver.page_source):
                        REPEAT=1
                        sleep(2)
                    else:
                        REPEAT=0
                        print("registration successful!")
                        break
                else:
                    driver.get("https://www38.polyu.edu.hk/eStudent/secure/my-subject-registration/subject-register-select-subject.jsf")
        except:
            continue
        
        
    
    
main()
