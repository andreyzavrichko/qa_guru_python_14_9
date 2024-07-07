from selene import browser, have

from test_data.user import UserTextBox


class TextBoxForm:
    def open(self):
        browser.open('text-box/')

    def type_full_name(self, full_name):
        browser.element('#userName').type(full_name)

    def type_email(self, email):
        browser.element('#userEmail').type(email)

    def type_current_address(self, current_address):
        browser.element('#currentAddress').type(current_address)

    def type_permanent_address(self, permanent_address):
        browser.element('#permanentAddress').type(permanent_address)

    def submit_form(self):
        browser.element('#submit').click()

    def register_text_box(self, user: UserTextBox):
        self.type_full_name(user.name)
        self.type_email(user.email)
        self.type_current_address(user.current_address)
        self.type_permanent_address(user.permanent_address)
        self.submit_form()
        return self

    def should_register_info(self, user: UserTextBox):
        browser.element('#output').should(have.exact_text(f'Name:{user.name}\n'
                                                          f'Email:{user.email}\n'
                                                          f'Current Address :{user.current_address}\n'
                                                          f'Permananet Address :{user.permanent_address}'))
