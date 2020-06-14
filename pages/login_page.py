from .base_page import BasePage
from .locators import LoginPageLocators


class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_form()
        self.should_be_login_url()
        self.should_be_register_form()

    def should_be_login_form(self):
        assert self.is_element_present(*LoginPageLocators.LOGIN_FORM), "Login form not found"

    def should_be_login_url(self):
        assert "login" in self.browser.current_url, "'login' not in current url"

    def should_be_register_form(self):
        assert self.is_element_present(*LoginPageLocators.REGISTER_FORM), "Register form not found"

    def register_new_user(self, email, password):
        assert self.browser.find_element(*LoginPageLocators.REG), "Registration button not found"
        email_field = self.browser.find_element(*LoginPageLocators.EMAIL)
        pass1_field = self.browser.find_element(*LoginPageLocators.PASS1)
        pass2_field = self.browser.find_element(*LoginPageLocators.PASS2)
        registration = self.browser.find_element(*LoginPageLocators.REG)
        email_field.send_keys(email)
        pass1_field.send_keys(password)
        pass2_field.send_keys(password)
        registration.click()
