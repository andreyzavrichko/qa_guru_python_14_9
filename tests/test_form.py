from models.application import app


def test_complete_todo():
    app.left_panel.open()
    app.left_panel.type_first_name('Alex')
    app.left_panel.type_last_name('Smirnov')
    app.left_panel.type_email('alex.smirnov@gmail.com')
    app.left_panel.click_gender()
    app.left_panel.type_phone('5648798798')
    app.left_panel.type_birthday()
    app.left_panel.type_subjects('Computer Science')
    app.left_panel.click_hobbies()
    app.left_panel.upload_photo('img.png')
    app.left_panel.type_address('Moscow, Manoilov Street, 64')
    app.left_panel.type_state('NCR')
    app.left_panel.type_city('Gurgaon')
    app.left_panel.press_submit()
    app.left_panel.should_text('Thanks for submitting the form')
    app.left_panel.should_exact_text('Alex Smirnov',
                                     'alex.smirnov@gmail.com',
                                     'Male',
                                     '5648798798',
                                     '15 May,2014',
                                     'Computer Science',
                                     'Sports',
                                     'img.png',
                                     'Moscow, Manoilov Street, 64',
                                     'NCR Gurgaon')
