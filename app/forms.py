from flask_wtf import Form
from wtforms import TextField, BooleanField, PasswordField, SubmitField, SelectField, TextAreaField
from wtforms.validators import Required
from flaskckeditor import CKEditor

class LoginForm(Form):
    username = TextField('Username', validators=[Required()])
    password = PasswordField('Password', validators=[Required()])
    remember_me = BooleanField('记住我', default=False)
    submit = SubmitField("登录")

class EditForm(Form, CKEditor):
    title = TextField('title', validators=[Required()])
    categories = SelectField('categories', choices=[('pm', '产品'),('data', '数据'),('book', '图书')], validators=[Required()])
    ckeditor_demo = TextAreaField('输入文章内容')
    submit = SubmitField("发布")
