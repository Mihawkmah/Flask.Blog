from flask_wtf import Form
from wtforms import TextField, BooleanField, PasswordField, SubmitField
from wtforms.validators import Required

class LoginForm(Form):
    username = TextField('用户名', validators=[Required()])
    password = PasswordField('密码', validators=[Required()])
    remember_me = BooleanField('记住我', default=False)
    submit = SubmitField("登录")
