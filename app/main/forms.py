from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField, TextAreaField
from wtforms.validators import ValidationError, DataRequired, Email, EqualTo, Length
from app.models import User


class EditProfileForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    hodem= StringField('Họ đệm',validators=[DataRequired()])
    ten = StringField('Tên')
    namgioi = BooleanField('Nam giới', validators=[DataRequired()])
    nhommau = StringField('Nhóm máu')
    dantoc = StringField('Dân tộc')
    submit = SubmitField('Xác nhận')

    def __init__(self, original_username, *args, **kwargs):
        super(EditProfileForm, self).__init__(*args, **kwargs)
        self.original_username = original_username

    def validate_username(self, username):
        if username.data != self.original_username:
            user = User.query.filter_by(username=self.username.data).first()
            if user is not None:
                raise ValidationError('Vui lòng nhập tên đăng nhập khác')
