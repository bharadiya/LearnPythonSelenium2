from selenium.webdriver.common.by import By
from selenium import  webdriver

class Loginpage:
    # constructor to initialize all the weblocators of particular page and also to pass instance of driver
    def __init__(self,driver):
        self.driver=driver
        self.username_textbox_id="email"
        self.password_textbox_xpath="//input[@id='pass']"
        self.loginButton_button_xpath="//button[@name='login']"
        # self.createNewAccountButton_button_xpath="<xpath>"
        # self.forgotPasswordButton_button_xpath="<xpath>"

    # Here every weblocator has method , if 5 locators on page, then 5 methods
    def enterUserName(self,driver,username):
        self.driver.find_element(By.ID,self.username_textbox_id).sendkeys(username)

    def enterPassword(self,driver,password):
        self.driver.find_element(By.XPATH,self.password_textbox_xpath).sendkeys(password)

    def clickLoginButton(self,driver):
        self.driver.find_element(By.XPATH,self.loginButton_button_xpath).click()

    # def clickCreateNewAccountButton(self):
    #     self.driver.find_element(By.XPATH,self.createNewAccountButton_button_xpath).click()
    #
    # def clickForgotPasswordButton(self):
    #     self.driver.find_element(By.XPATH,self.forgotPasswordButton_button_xpath).click()
