from pathlib import Path

from selene import browser, have

from test_data.user import User


class RegistrationForm:
    def open(self):
        browser.open('automation-practice-form/')

    def type_first_name(self, first_name):
        browser.element('#firstName').type(first_name)

    def type_last_name(self, last_name):
        browser.element('#lastName').type(last_name)

    def type_email(self, email):
        browser.element('#userEmail').type(email)

    def type_birthday(self):
        browser.element('#dateOfBirthInput').click()
        browser.element('.react-datepicker__month-select').click()
        browser.element('.react-datepicker__month-select').element('[value="4"]').click()
        browser.element('.react-datepicker__year-select').click()
        browser.element('.react-datepicker__year-select').element('[value="2014"]').click()
        browser.element('.react-datepicker__day--015').click()

    def click_gender(self):
        browser.element('[value=Male]+label').click()

    def type_phone(self, phone):
        browser.element('#userNumber').type(phone)

    def type_subjects(self, subjects):
        browser.element('#subjectsInput').type(subjects).press_enter()

    def click_hobbies(self):
        browser.element('[for=hobbies-checkbox-1]').click()

    def upload_photo(self, photo):
        browser.element('#uploadPicture').send_keys(str(Path(__file__).parent.parent.joinpath(f'resources/{photo}')))

    def type_address(self, address):
        browser.element('#currentAddress').type(address)

    def type_state(self, state):
        browser.element('#react-select-3-input').type(state).press_enter()

    def type_city(self, city):
        browser.element('#react-select-4-input').type(city).press_enter()

    def press_submit(self):
        browser.element('#submit').click()

    def should_text(self, text):
        browser.element("#example-modal-sizes-title-lg").should(have.text(text))

    def should_exact_text(self, user: User):
        browser.element('.table').all('td').even.should(have.exact_texts(
            f'{user.first_name} {user.last_name}',
            f'{user.email}',
            f'{user.gender}',
            f'{user.phone}',
            f'{user.birthday}',
            f'{user.subject}',
            f'{user.hobbies}',
            f'{user.photo}',
            f'{user.address}',
            f'{user.state} {user.city}'))

    def register(self, user: User):
        self.type_first_name(user.first_name)
        self.type_last_name(user.last_name)
        self.type_email(user.email)
        self.click_gender()
        self.type_phone(user.phone)
        self.type_birthday()
        self.type_subjects(user.subject)
        self.click_hobbies()
        self.upload_photo(user.photo)
        self.type_address(user.address)
        self.type_state(user.state)
        self.type_city(user.city)
        self.press_submit()
