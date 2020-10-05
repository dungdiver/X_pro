from app import db, login
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin
from hashlib import md5
from sqlalchemy.dialects.mssql import \
    BIGINT, BINARY, BIT, CHAR, DATE, DATETIME, DATETIME2, \
    DATETIMEOFFSET, DECIMAL, FLOAT, IMAGE, INTEGER, MONEY, \
    NCHAR, NTEXT, NUMERIC, NVARCHAR, REAL, SMALLDATETIME, \
    SMALLINT, SMALLMONEY, SQL_VARIANT, TEXT, TIME, \
    TIMESTAMP, TINYINT, UNIQUEIDENTIFIER, VARBINARY, VARCHAR


class User(UserMixin, db.Model):
    __tablename__ = 'User'
    id = db.Column(db.Integer, primary_key=True)
    ho_dem = db.Column(db.NVARCHAR(30))
    ten = db.Column(db.NVARCHAR(15), index=True)
    ngay_sinh = db.Column(db.Date())
    nam_gioi = db.Column(db.NCHAR(1), default=True)
    nhom_mau = db.Column(db.String(10))
    dan_toc = db.Column(db.NVARCHAR(20))
    que = db.Column(db.NVARCHAR(100))
    dktt = db.Column(db.NVARCHAR(100))
    noi_o = db.Column(db.NVARCHAR(100))
    so_hieu = db.Column(db.String(6))
    ngay_vao_cong_an = db.Column(db.Date())
    nganh_ngoai = db.Column(db.Boolean())
    trinh_do_chinh_tri = db.Column(db.NVARCHAR(30))
    trinh_do_ngoai_ngu = db.Column(db.NVARCHAR(30))
    trinh_do_tin_hoc = db.Column(db.NVARCHAR(30))
    trang_thai_user_id = db.Column(
        db.SMALLINT(), db.ForeignKey('TrangThaiUser.id'))
    username = db.Column(db.String(20), index=True, unique=True)
    email = db.Column(db.String(120), index=True, unique=True)
    password_hash = db.Column(db.String(128))
    so_dien_thoai = db.relationship(
        'SoDienThoai', backref='chu_thue_bao', lazy='dynamic')

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

    def avatar(self, size):
        digest = md5(self.email.lower().encode('utf-8')).hexdigest()
        return 'https://www.gravatar.com/avatar/{}?d=identicon&amp;s={}'.format(
            digest, size)

    def __repr__(self):
        return '<User {}>'.format(self.username)


class TrangThaiUser(db.Model):
    __tablename__ = 'TrangThaiUser'
    id = db.Column(db.SMALLINT(), primary_key=True)
    ten = db.Column(db.NVARCHAR(25))


class SoDienThoai(db.Model):
    __tablename__ = 'SoDienThoai'
    id = db.Column(db.SMALLINT(), primary_key=True)
    user_id = db.Column(db.Integer(), db.ForeignKey(User.id))
    so_dien_thoai = db.Column(db.NCHAR(10))


class BoPhan(db.Model):
    __tablename__ = 'BoPhan'
    id = db.Column(db.Integer, primary_key=True)
    ten = db.Column(db.NVARCHAR(50), nullable=False)
    ma = db.Column(db.String(3))
    khoi = db.Column(db.String(20))


@login.user_loader
def load_user(id):
    return User.query.get(int(id))
