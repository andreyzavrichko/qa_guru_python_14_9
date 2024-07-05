from pages.form_page import RegistrationForm


def test_complete_todo():
    registration_form = RegistrationForm()
    registration_form.open()
    registration_form.type_first_name('Alex')
    registration_form.type_last_name('Smirnov')
    registration_form.type_email('alex.smirnov@gmail.com')
    registration_form.click_gender()
    registration_form.type_phone('5648798798')
    registration_form.type_birthday()
    registration_form.type_subjects('co')
    registration_form.click_hobbies()
    registration_form.upload_photo('img.png')
    registration_form.type_address('Moscow, Manoilov Street, 64')
    registration_form.type_state('NCR')
    registration_form.type_city('Gurgaon')
    registration_form.press_submit()
    registration_form.should_text('Thanks for submitting the form')
    registration_form.should_exact_text('Alex Smirnov',
                                        'alex.smirnov@gmail.com',
                                        'Male',
                                        '5648798798',
                                        '15 May,2014',
                                        'Computer Science',
                                        'Sports',
                                        'img.png',
                                        'Moscow, Manoilov Street, 64',
                                        'NCR Gurgaon')
