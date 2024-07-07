from test_data import user
from models.application import app


def test_text_box_form():
    app.left_panel.open_simple_registration_form()
    app.text_box_form.register_text_box(user.user_text_box)
    app.text_box_form.should_register_info(user.user_text_box)
