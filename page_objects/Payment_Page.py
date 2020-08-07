from .Base_Page import Base_Page
from utils.Wrapit import Wrapit
import conf.locators_conf as locators

class Payment_Page(Base_Page):
    FORM_EMAIL_ID = locators.FORM_EMAIL_ID
    FORM_ACCOUNT_NUMBER = locators.FORM_ACCOUNT_NUMBER
    FORM_EXPIRY_DATE =  locators.FORM_EXPIRY_DATE
    FORM_CVV = locators.FORM_CVV
    FORM_ZIP_CODE = locators.FORM_ZIP_CODE
    FORM_REMEMBER_ME = locators.FORM_REMEMBER_ME
    FORM_MOBILE = locators.FORM_MOBILE
    FORM_SUBMIT = locators.FORM_SUBMIT
    EMAIL_ID = locators.EMAIL_ID
    ACCOUNT_NUMBER = locators.ACCOUNT_NUMBER
    EXPIRY_DATE = locators.EXPIRY_DATE
    CVV = locators.CVV
    ZIP_CODE = locators.ZIP_CODE
    REMEMBER_ME = locators.REMEMBER_ME
    MOBILE = locators.MOBILE

    def start(self):
        "Switching to payment iframe"
        self.switch_frame("iframe")

    def click_pay_button(self):
        "Click to the pay button"
        result_flag = self.click_element(self.CART_PAY_BUTTON)
        if result_flag:
            self.switch_page("checkout")
        self.conditional_write(result_flag,
        positive="Clicked on the Pay with card button",
        negative="Could not click on the Pay with card button")

        return result_flag

    @Wrapit._exceptionHandler
    def set_email(self):
        "Set the email on the form"
        result_flag = self.set_text(self.FORM_EMAIL_ID, self.EMAIL_ID)
        self.conditional_write(result_flag,
            positive='Set the email to: {}'.format(self.EMAIL_ID),
            negative='Failed to set the email in the form',
            level='debug')

        return result_flag

    @Wrapit._exceptionHandler
    def set_account_number(self):
        "Set the account number on the form"
        result_flag = self.set_text(self.FORM_ACCOUNT_NUMBER, self.ACCOUNT_NUMBER)
        self.conditional_write(result_flag,
            positive='Set the account number to: {}'.format(self.ACCOUNT_NUMBER),
            negative='Failed to set the account number in the form',
            level='debug')

        return result_flag

    @Wrapit._exceptionHandler
    def set_expiry_date(self):
        "Set the expiry date on the form"
        result_flag = self.set_text(self.FORM_EXPIRY_DATE, self.EXPIRY_DATE)
        self.conditional_write(result_flag,
            positive='Set the expiry date to: {}'.format(self.EXPIRY_DATE),
            negative='Failed to set the expiry date in the form',
            level='debug')

        return result_flag

    @Wrapit._exceptionHandler
    def set_cvv(self):
        "Set the cvv on the form"
        result_flag = self.set_text(self.FORM_CVV, self.CVV)
        self.conditional_write(result_flag,
            positive='Set the cvv to: {}'.format(self.CVV),
            negative='Failed to set the cvv in the form',
            level='debug')

        return result_flag

    @Wrapit._exceptionHandler
    def set_zip_code(self):
        "Set the zip code on the form"
        result_flag = self.set_text(self.FORM_ZIP_CODE, self.ZIP_CODE)
        self.conditional_write(result_flag,
            positive='Set the zip code to: {}'.format(self.ZIP_CODE),
            negative='Failed to set the zip code in the form',
            level='debug')

        return result_flag

    @Wrapit._exceptionHandler
    def set_mobile(self):
        "Set the mobile number on the form"
        result_flag = self.set_text(self.FORM_MOBILE, self.MOBILE)
        self.conditional_write(result_flag,
            positive='Set the mobile number to: {}'.format(self.MOBILE),
            negative='Failed to set the mobile number in the form',
            level='debug')

        return result_flag

    @Wrapit._exceptionHandler
    def click_submit_button(self):
        "Click the pay button"
        result_flag = self.click_element(self.FORM_SUBMIT)
        self.conditional_write(result_flag,
        positive="Clicked on the submit button",
        negative="Could not click on the submit button")
        return result_flag
