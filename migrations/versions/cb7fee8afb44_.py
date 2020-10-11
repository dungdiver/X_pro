"""empty message

Revision ID: cb7fee8afb44
Revises: c97930c86eb5
Create Date: 2020-10-09 15:18:38.105836

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'cb7fee8afb44'
down_revision = 'c97930c86eb5'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('BoPhan',
    sa.Column('id', sa.SMALLINT(), nullable=False),
    sa.Column('ten', sa.NVARCHAR(length=50), nullable=False),
    sa.Column('ma', sa.String(length=3), nullable=True),
    sa.Column('khoi', sa.String(length=20), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    schema='NhanSu'
    )
    op.create_table('ChucDanhCongTac',
    sa.Column('id', sa.SMALLINT(), nullable=False),
    sa.Column('ten', sa.NVARCHAR(length=100), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    schema='NhanSu'
    )
    op.create_table('ChucDanhNghiepVu',
    sa.Column('id', sa.SMALLINT(), nullable=False),
    sa.Column('ten', sa.NVARCHAR(length=100), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    schema='NhanSu'
    )
    op.create_table('TrangThaiUser',
    sa.Column('id', sa.SMALLINT(), nullable=False),
    sa.Column('ten', sa.NVARCHAR(length=25), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('User',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('ho_dem', sa.NVARCHAR(length=30), nullable=True),
    sa.Column('ten', sa.NVARCHAR(length=15), nullable=True),
    sa.Column('ngay_sinh', sa.Date(), nullable=True),
    sa.Column('nam_gioi', sa.NCHAR(length=1), nullable=True),
    sa.Column('nhom_mau', sa.String(length=10), nullable=True),
    sa.Column('dan_toc', sa.NVARCHAR(length=20), nullable=True),
    sa.Column('que', sa.NVARCHAR(length=100), nullable=True),
    sa.Column('dktt', sa.NVARCHAR(length=100), nullable=True),
    sa.Column('noi_o', sa.NVARCHAR(length=100), nullable=True),
    sa.Column('so_hieu', sa.String(length=6), nullable=True),
    sa.Column('ngay_vao_cong_an', sa.Date(), nullable=True),
    sa.Column('nganh_ngoai', sa.Boolean(), nullable=True),
    sa.Column('trinh_do_chinh_tri', sa.NVARCHAR(length=30), nullable=True),
    sa.Column('trinh_do_ngoai_ngu', sa.NVARCHAR(length=30), nullable=True),
    sa.Column('trinh_do_tin_hoc', sa.NVARCHAR(length=30), nullable=True),
    sa.Column('trang_thai_user_id', sa.SMALLINT(), nullable=True),
    sa.Column('username', sa.String(length=20), nullable=True),
    sa.Column('email', sa.String(length=120), nullable=True),
    sa.Column('password_hash', sa.String(length=128), nullable=True),
    sa.Column('is_admin', sa.Boolean(), nullable=False),
    sa.ForeignKeyConstraint(['trang_thai_user_id'], ['TrangThaiUser.id'], ),
    sa.PrimaryKeyConstraint('id'),
    schema='NhanSu'
    )
    op.create_index(op.f('ix_NhanSu_User_email'), 'User', ['email'], unique=True, schema='NhanSu')
    op.create_index(op.f('ix_NhanSu_User_ten'), 'User', ['ten'], unique=False, schema='NhanSu')
    op.create_index(op.f('ix_NhanSu_User_username'), 'User', ['username'], unique=True, schema='NhanSu')
    op.create_table('ChucDanhCongTacUser',
    sa.Column('id', sa.SMALLINT(), nullable=False),
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.Column('chuc_danh_cong_tac_id', sa.SMALLINT(), nullable=True),
    sa.Column('ngay_bat_dau', sa.DATE(), nullable=True),
    sa.ForeignKeyConstraint(['chuc_danh_cong_tac_id'], ['NhanSu.ChucDanhCongTac.id'], ),
    sa.ForeignKeyConstraint(['user_id'], ['NhanSu.User.id'], ),
    sa.PrimaryKeyConstraint('id'),
    schema='NhanSu'
    )
    op.create_table('ChucDanhNghiepVuUser',
    sa.Column('id', sa.SMALLINT(), nullable=False),
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.Column('chuc_danh_nghiep_vu_id', sa.SMALLINT(), nullable=True),
    sa.Column('ngay_bat_dau', sa.DATE(), nullable=True),
    sa.ForeignKeyConstraint(['chuc_danh_nghiep_vu_id'], ['NhanSu.ChucDanhNghiepVu.id'], ),
    sa.ForeignKeyConstraint(['user_id'], ['NhanSu.User.id'], ),
    sa.PrimaryKeyConstraint('id'),
    schema='NhanSu'
    )
    op.create_table('SoDienThoai',
    sa.Column('id', sa.SMALLINT(), nullable=False),
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.Column('so_dien_thoai', sa.NCHAR(length=10), nullable=True),
    sa.ForeignKeyConstraint(['user_id'], ['NhanSu.User.id'], ),
    sa.PrimaryKeyConstraint('id'),
    schema='NhanSu'
    )
    op.create_table('ViTri',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('user_id', sa.Integer(), nullable=False),
    sa.Column('bo_phan_id', sa.SMALLINT(), nullable=False),
    sa.Column('cong_viec', sa.NVARCHAR(length=255), nullable=True),
    sa.Column('ngay_bat_dau', sa.DATE(), nullable=True),
    sa.Column('ngay_ket_thuc', sa.DATE(), nullable=True),
    sa.ForeignKeyConstraint(['bo_phan_id'], ['NhanSu.BoPhan.id'], ),
    sa.ForeignKeyConstraint(['user_id'], ['NhanSu.User.id'], ),
    sa.PrimaryKeyConstraint('id'),
    schema='NhanSu'
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('ViTri', schema='NhanSu')
    op.drop_table('SoDienThoai', schema='NhanSu')
    op.drop_table('ChucDanhNghiepVuUser', schema='NhanSu')
    op.drop_table('ChucDanhCongTacUser', schema='NhanSu')
    op.drop_index(op.f('ix_NhanSu_User_username'), table_name='User', schema='NhanSu')
    op.drop_index(op.f('ix_NhanSu_User_ten'), table_name='User', schema='NhanSu')
    op.drop_index(op.f('ix_NhanSu_User_email'), table_name='User', schema='NhanSu')
    op.drop_table('User', schema='NhanSu')
    op.drop_table('TrangThaiUser')
    op.drop_table('ChucDanhNghiepVu', schema='NhanSu')
    op.drop_table('ChucDanhCongTac', schema='NhanSu')
    op.drop_table('BoPhan', schema='NhanSu')
    # ### end Alembic commands ###
