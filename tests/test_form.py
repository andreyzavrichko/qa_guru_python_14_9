from test_data.user import User
from pages.form_page import RegistrationForm


def test_complete_todo():
    form_page = RegistrationForm()
    man = User(first_name='Alex',
               last_name='Smirnov',
               email='alex.smirnov@gmail.com',
               gender='Male',
               phone='5648798798',
               birthday='15 May,2014',
               subject='Computer Science',
               photo='img.png',
               hobbies='Sports',
               address='Moscow, Manoilov Street, 64',
               state='NCR',
               city='Gurgaon')
    form_page.open()
    form_page.register(man)
    form_page.should_exact_text(man)
