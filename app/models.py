# import third party
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin
from hashlib import md5
# Import sqlserver datatype
from sqlalchemy.dialects.mssql import \
    BIGINT, BINARY, BIT, CHAR, DATE, DATETIME, DATETIME2, \
    DATETIMEOFFSET, DECIMAL, FLOAT, IMAGE, INTEGER, MONEY, \
    NCHAR, NTEXT, NUMERIC, NVARCHAR, REAL, SMALLDATETIME, \
    SMALLINT, SMALLMONEY, SQL_VARIANT, TEXT, TIME, \
    TIMESTAMP, TINYINT, UNIQUEIDENTIFIER, VARBINARY, VARCHAR

# import local
from app import db, login

class User(UserMixin, db.Model):
    __tablename__ = 'User'
    __table_args__ = {"schema": "NhanSu"}
    id = db.Column(db.INTEGER,  primary_key=True)
    username = db.Column(db.VARCHAR(20), index=True, unique=True)
    email = db.Column(db.VARCHAR(120), index=True, unique=True)
    password_hash = db.Column(db.VARCHAR(128))
    is_admin = db.Column(db.Boolean(), default=False, nullable=False)

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


class CanBo(db.Model):
    __tablename__ = 'CanBo'
    __table_args__ = {"schema": "NhanSu"}
    id = db.Column(db.INTEGER,  primary_key=True)
    ho_dem = db.Column(db.NVARCHAR(30))
    ten = db.Column(db.NVARCHAR(15), index=True)
    ngay_sinh = db.Column(db.Date())
    gioi_tinh = db.Column(db.NCHAR(1), default='M')
    nhom_mau = db.Column(db.VARCHAR(10))
    dan_toc = db.Column(db.NVARCHAR(20))
    que = db.Column(db.NVARCHAR(100))
    dktt = db.Column(db.NVARCHAR(100))
    noi_o = db.Column(db.NVARCHAR(100))
    so_hieu = db.Column(db.VARCHAR(6))
    ngay_vao_cong_an = db.Column(db.Date())
    nganh_ngoai = db.Column(db.Boolean())
    trinh_do_chinh_tri = db.Column(db.NVARCHAR(30))
    trinh_do_ngoai_ngu = db.Column(db.NVARCHAR(30))
    trinh_do_tin_hoc = db.Column(db.NVARCHAR(30))
    trang_thai_cong_tac_id = db.Column(
        db.SMALLINT, db.ForeignKey('NhanSu.TrangThaiCongTac.id'))
    so_dien_thoai = db.relationship(
        'SoDienThoai', backref='chu_thue_bao', lazy='dynamic')


@ login.user_loader
def load_user(id):
    return User.query.get(int(id))


class TrangThaiCongTac(db.Model):
    __tablename__ = 'TrangThaiCongTac'
    __table_args__ = {"schema": "NhanSu"}
    id = db.Column(db.SMALLINT, primary_key=True)
    ten = db.Column(db.NVARCHAR(25))


class SoDienThoai(db.Model):
    __tablename__ = 'SoDienThoai'
    __table_args__ = {"schema": "NhanSu"}
    id = db.Column(db.INTEGER, primary_key=True)
    can_bo_id = db.Column(db.INTEGER, db.ForeignKey('NhanSu.CanBo.id'))
    so_dien_thoai = db.Column(db.VARCHAR(10))


class BoPhan(db.Model):
    __tablename__ = 'BoPhan'
    __table_args__ = {"schema": "NhanSu"}
    id = db.Column(db.SMALLINT, primary_key=True)
    ten = db.Column(db.NVARCHAR(50), nullable=False)
    ma = db.Column(db.VARCHAR(3))
    khoi = db.Column(db.VARCHAR(20))


class NhomViTri(db.Model):
    __tablename__ = 'NhomViTri'
    __table_args__ = {"schema": "NhanSu"}
    id = db.Column(db.SMALLINT, primary_key=True)
    ten = db.Column(db.NVARCHAR(250))


class ViTri(db.Model):
    __tablename__ = 'ViTri'
    __table_args__ = {"schema": "NhanSu"}
    id = db.Column(db.INTEGER, primary_key=True)
    can_bo_id = db.Column(db.INTEGER, db.ForeignKey(
        'NhanSu.CanBo.id'), nullable=False)
    bo_phan_id = db.Column(
        db.SMALLINT, db.ForeignKey('NhanSu.BoPhan.id'), nullable=False)
    cong_viec = db.Column(db.NVARCHAR(255))
    nhom_vi_tri_id = db.Column(
        db.SMALLINT, db.ForeignKey('NhanSu.NhomViTri.id'))
    ngay_bat_dau = db.Column(db.DATE())
    ngay_ket_thuc = db.Column(db.DATE())


class ChucDanhCongTac(db.Model):
    __tablename__ = 'ChucDanhCongTac'
    __table_args__ = {"schema": "NhanSu"}
    id = db.Column(db.SMALLINT, primary_key=True)
    ten = db.Column(db.NVARCHAR(100))


class ChucDanhCongTacCanBo(db.Model):
    __tablename__ = 'ChucDanhCongTacCanBo'
    __table_args__ = {"schema": "NhanSu"}
    id = db.Column(db.INTEGER, primary_key=True)
    can_bo_id = db.Column(db.INTEGER, db.ForeignKey('NhanSu.CanBo.id'))
    chuc_danh_cong_tac_id = db.Column(
        db.SMALLINT, db.ForeignKey('NhanSu.ChucDanhCongTac.id'))
    ngay_bat_dau = db.Column(db.DATE())


class ChucDanhNghiepVu(db.Model):
    __tablename__ = 'ChucDanhNghiepVu'
    __table_args__ = {"schema": "NhanSu"}
    id = db.Column(db.SMALLINT, primary_key=True)
    ten = db.Column(db.NVARCHAR(100))


class ChucDanhNghiepVuCanBo(db.Model):
    __tablename__ = 'ChucDanhNghiepVuCanBo'
    __table_args__ = {"schema": "NhanSu"}
    id = db.Column(db.INTEGER, primary_key=True)
    can_bo_id = db.Column(db.INTEGER, db.ForeignKey('NhanSu.CanBo.id'))
    chuc_danh_nghiep_vu_id = db.Column(
        db.SMALLINT, db.ForeignKey('NhanSu.ChucDanhNghiepVu.id'))
    ngay_bat_dau = db.Column(db.DATE())


class ChucDanhTuPhap(db.Model):
    __tablename__ = 'ChucDanhTuPhap'
    __table_args__ = {"schema": "NhanSu"}
    id = db.Column(db.SMALLINT, primary_key=True)
    ten = db.Column(db.NVARCHAR(100))


class ChucDanhTuPhapCanBo(db.Model):
    __tablename__ = 'ChucDanhTuPhapCanBo'
    __table_args__ = {"schema": "NhanSu"}
    id = db.Column(db.INTEGER, primary_key=True)
    can_bo_id = db.Column(db.INTEGER, db.ForeignKey('NhanSu.CanBo.id'))
    chuc_danh_tu_phap_id = db.Column(
        db.SMALLINT, db.ForeignKey('NhanSu.ChucDanhTuPhap.id'))
    ngay_bat_dau = db.Column(db.DATE())
    ngay_ket_thuc = db.Column(db.DATE())


class CapBac(db.Model):
    __tablename__ = 'CapBac'
    __table_args__ = {"schema": "NhanSu"}
    id = db.Column(db.SMALLINT, primary_key=True)
    ten = db.Column(db.NVARCHAR(100))


class CapBacCanBo(db.Model):
    __tablename__ = 'CapBacCanBo'
    __table_args__ = {"schema": "NhanSu"}
    id = db.Column(db.INTEGER, primary_key=True)
    can_bo_id = db.Column(db.INTEGER, db.ForeignKey('NhanSu.CanBo.id'))
    cap_bac_id = db.Column(
        db.SMALLINT, db.ForeignKey('NhanSu.CapBac.id'))
    ngay_bat_dau = db.Column(db.DATE())


class HeSoLuongCanBo(db.Model):
    __tablename__ = 'HeSoLuongCanBo'
    __table_args__ = {"schema": "NhanSu"}
    id = db.Column(db.INTEGER, primary_key=True)
    can_bo_id = db.Column(db.INTEGER, db.ForeignKey('NhanSu.CanBo.id'))
    he_so = db.Column(db.DECIMAL(4, 2))
    ngay_bat_dau = db.Column(db.DATE())


class GiayTo(db.Model):
    __tablename__ = 'GiayTo'
    __table_args__ = {"schema": "NhanSu"}
    id = db.Column(db.SMALLINT, primary_key=True)
    ten = db.Column(db.NVARCHAR(100))


class GiayToCanBo(db.Model):
    __tablename__ = 'GiayToCanBo'
    __table_args__ = {"schema": "NhanSu"}
    id = db.Column(db.INTEGER, primary_key=True)
    can_bo_id = db.Column(db.INTEGER, db.ForeignKey('NhanSu.CanBo.id'))
    giay_to_id = db.Column(
        db.SMALLINT, db.ForeignKey('NhanSu.GiayTo.id'))
    so = db.Column(db.NVARCHAR(50))
    ngay_cap = db.Column(db.DATE)
    loai_cap = db.Column(db.NVARCHAR(30))
    tinh_trang = db.Column(db.NVARCHAR(30))
    loai_cap = db.Column(db.NVARCHAR(30))
    ngay_thu = db.Column(db.DATE)
    ghi_chu = db.Column(db.NVARCHAR)


class HinhThucKhenThuong(db.Model):
    __tablename__ = 'HinhThucKhenThuong'
    __table_args__ = {"schema": "NhanSu"}
    id = db.Column(db.SMALLINT, primary_key=True)
    ten = db.Column(db.NVARCHAR(100))


class KhenThuongCaNhan(db.Model):
    __tablename__ = 'KhenThuongCaNhan'
    __table_args__ = {"schema": "NhanSu"}
    id = db.Column(db.INTEGER, primary_key=True)
    can_bo_id = db.Column(db.INTEGER, db.ForeignKey('NhanSu.CanBo.id'))
    hinh_thuc_khen_thuong_id = db.Column(
        db.SMALLINT, db.ForeignKey('NhanSu.HinhThucKhenThuong.id'))
    so_quyet_dinh = db.Column(db.NVARCHAR(50))
    ngay_quyet_dinh = db.Column(db.DATE)
    don_vi_khen = db.Column(db.NVARCHAR(250))
    noi_dung = db.Column(db.NVARCHAR(250))
    so_tien = db.Column(db.INTEGER)
    ghi_chu = db.Column(db.NVARCHAR)


class KhenThuongTapThe(db.Model):
    __tablename__ = 'KhenThuongTapThe'
    __table_args__ = {"schema": "NhanSu"}
    id = db.Column(db.INTEGER, primary_key=True)
    ten_tap_the = db.Column(db.NVARCHAR)
    hinh_thuc_khen_thuong_id = db.Column(
        db.SMALLINT, db.ForeignKey('NhanSu.HinhThucKhenThuong.id'))
    so_quyet_dinh = db.Column(db.NVARCHAR(50))
    ngay_quyet_dinh = db.Column(db.DATE)
    don_vi_khen = db.Column(db.NVARCHAR(250))
    noi_dung = db.Column(db.NVARCHAR(250))
    so_tien = db.Column(db.INTEGER)
    ghi_chu = db.Column(db.NVARCHAR)


class PltdCaNhanTheoThang(db.Model):
    __tablename__ = 'PltdCaNhanTheoThang'
    __table_args__ = {"schema": "NhanSu"}
    id = db.Column(db.INTEGER, primary_key=True)
    can_bo_id = db.Column(db.INTEGER, db.ForeignKey('NhanSu.CanBo.id'))
    thang = db.Column(db.DATE)
    phan_loai = db.Column(db.NVARCHAR(5))
    ghi_chu = db.Column(db.NVARCHAR)


class PltdCaNhanTheoNam(db.Model):
    __tablename__ = 'PltdCaNhanTheoNam'
    __table_args__ = {"schema": "NhanSu"}
    id = db.Column(db.INTEGER, primary_key=True)
    can_bo_id = db.Column(db.INTEGER, db.ForeignKey('NhanSu.CanBo.id'))
    nam = db.Column(db.SMALLINT)
    phan_loai = db.Column(db.NVARCHAR(5))
    ghi_chu = db.Column(db.NVARCHAR)


class PlcbTheoNam(db.Model):
    __tablename__ = 'PlcbTheoNam'
    __table_args__ = {"schema": "NhanSu"}
    id = db.Column(db.INTEGER, primary_key=True)
    can_bo_id = db.Column(db.INTEGER, db.ForeignKey('NhanSu.CanBo.id'))
    nam = db.Column(db.SMALLINT)
    phan_loai = db.Column(db.NVARCHAR(50))
    ghi_chu = db.Column(db.NVARCHAR)


class PltdTapThe(db.Model):
    __tablename__ = 'PltdTapThe'
    __table_args__ = {"schema": "NhanSu"}
    id = db.Column(db.INTEGER, primary_key=True)
    nam = db.Column(db.SMALLINT)
    phan_loai = db.Column(db.NVARCHAR(100))
    ghi_chu = db.Column(db.NVARCHAR)


class DangDoanThe(db.Model):
    __tablename__ = 'DangDoanThe'
    __table_args__ = {"schema": "NhanSu"}
    id = db.Column(db.INTEGER, primary_key=True)
    can_bo_id = db.Column(db.INTEGER, db.ForeignKey('NhanSu.CanBo.id'))
    ngay_vao_dang_lan_dau = db.Column(db.DATE)
    ngay_vao_dang_chinh_thuc = db.Column(db.DATE)


class KiLuat(db.Model):
    __tablename__ = 'KiLuat'
    __table_args__ = {"schema": "NhanSu"}
    id = db.Column(db.INTEGER, primary_key=True)
    can_bo_id = db.Column(db.INTEGER, db.ForeignKey('NhanSu.CanBo.id'))
    hinh_thuc = db.Column(db.NVARCHAR)
    so_quyet_dinh = db.Column(db.NVARCHAR(50))
    ngay_quyet_dinh = db.Column(db.DATE)
    noi_dung = db.Column(db.NVARCHAR(250))
    ghi_chu = db.Column(db.NVARCHAR)

class QuiHoach(db.Model):
    __tablename__ = 'QuiHoach'
    __table_args__ = {"schema": "NhanSu"}
    id = db.Column(db.INTEGER, primary_key=True)
    can_bo_id = db.Column(db.INTEGER, db.ForeignKey('NhanSu.CanBo.id'))
    chuc_danh_cong_tac_id = db.Column(
        db.SMALLINT, db.ForeignKey('NhanSu.ChucDanhCongTac.id'))
    ngay_bat_dau = db.Column(db.DATE)

class TrinhDoNghiepVu(db.Model):
    __tablename__ = 'TrinhDoNghiepVu'
    __table_args__ = {"schema": "NhanSu"}
    id = db.Column(db.SMALLINT, primary_key=True)
    ten = db.Column(db.NVARCHAR(20))

class CoSoDaoTao(db.Model):
    __tablename__ = 'CoSoDaoTao'
    __table_args__ = {"schema": "NhanSu"}
    id = db.Column(db.SMALLINT, primary_key=True)
    ten = db.Column(db.NVARCHAR(100))

class TrinhDoNghiepVuCanBo(db.Model):
    __tablename__ = 'TrinhDoNghiepVuCanBo'
    __table_args__ = {"schema": "NhanSu"}
    id = db.Column(db.SMALLINT, primary_key=True)
    can_bo_id = db.Column(db.INTEGER, db.ForeignKey('NhanSu.CanBo.id'))
    trinh_do_nghiep_vu_id = db.Column(
        db.SMALLINT, db.ForeignKey('NhanSu.TrinhDoNghiepVu.id'))
    co_so_dao_tao_id = db.Column(db.SMALLINT, db.ForeignKey('NhanSu.CoSoDaoTao.id'))
    chuyen_nganh = db.Column(db.NVARCHAR(50))
    ngay_bat_dau = db.Column(db.DATE())
    ngay_ket_thuc = db.Column(db.DATE())
    ket_qua = db.Column(db.NVARCHAR(50))
    ghi_chu = db.Column(db.NVARCHAR)

class LopDaoTao(db.Model):
    __tablename__ = 'LopDaoTao'
    __table_args__ = {"schema": "NhanSu"}
    id = db.Column(db.SMALLINT, primary_key=True)
    ten = db.Column(db.NVARCHAR(100))

class DaoTaoNganHan(db.Model):
    __tablename__ = 'DaoTaoNganHan'
    __table_args__ = {"schema": "NhanSu"}
    id = db.Column(db.SMALLINT, primary_key=True)
    can_bo_id = db.Column(db.INTEGER, db.ForeignKey('NhanSu.CanBo.id'))
    co_so_dao_tao_id = db.Column(db.SMALLINT, db.ForeignKey('NhanSu.CoSoDaoTao.id'))
    lop_dao_tao_id = db.Column(db.SMALLINT, db.ForeignKey('NhanSu.LopDaoTao.id'))
    ngay_bat_dau = db.Column(db.DATE())
    ngay_ket_thuc = db.Column(db.DATE())
    ket_qua = db.Column(db.NVARCHAR(50))
    ghi_chu = db.Column(db.NVARCHAR)

class DaoTaoDaiHan(db.Model):
    __tablename__ = 'DaoTaoDaiHan'
    __table_args__ = {"schema": "NhanSu"}
    id = db.Column(db.SMALLINT, primary_key=True)
    can_bo_id = db.Column(db.INTEGER, db.ForeignKey('NhanSu.CanBo.id'))
    co_so_dao_tao_id = db.Column(db.SMALLINT, db.ForeignKey('NhanSu.CoSoDaoTao.id'))
    trinh_do_nghiep_vu_id = db.Column(
        db.SMALLINT, db.ForeignKey('NhanSu.TrinhDoNghiepVu.id'))
    ngay_bat_dau = db.Column(db.DATE())
    ngay_ket_thuc = db.Column(db.DATE())
    ket_qua = db.Column(db.NVARCHAR(50))
    ghi_chu = db.Column(db.NVARCHAR)