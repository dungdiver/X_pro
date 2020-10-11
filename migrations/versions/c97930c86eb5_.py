"""empty message

Revision ID: c97930c86eb5
Revises: 2be247b104de
Create Date: 2020-10-09 14:34:25.538388

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'c97930c86eb5'
down_revision = '2be247b104de'
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
    schema='nhansu'
    )
    op.create_table('ChucDanhCongTac',
    sa.Column('id', sa.SMALLINT(), nullable=False),
    sa.Column('ten', sa.NVARCHAR(length=100), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    schema='nhansu'
    )
    op.create_table('ChucDanhNghiepVu',
    sa.Column('id', sa.SMALLINT(), nullable=False),
    sa.Column('ten', sa.NVARCHAR(length=100), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    schema='nhansu'
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
    schema='nhansu'
    )
    op.create_index(op.f('ix_nhansu_User_email'), 'User', ['email'], unique=True, schema='nhansu')
    op.create_index(op.f('ix_nhansu_User_ten'), 'User', ['ten'], unique=False, schema='nhansu')
    op.create_index(op.f('ix_nhansu_User_username'), 'User', ['username'], unique=True, schema='nhansu')
    op.create_table('ChucDanhCongTacUser',
    sa.Column('id', sa.SMALLINT(), nullable=False),
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.Column('chuc_danh_cong_tac_id', sa.SMALLINT(), nullable=True),
    sa.Column('ngay_bat_dau', sa.DATE(), nullable=True),
    sa.ForeignKeyConstraint(['chuc_danh_cong_tac_id'], ['nhansu.ChucDanhCongTac.id'], ),
    sa.ForeignKeyConstraint(['user_id'], ['nhansu.User.id'], ),
    sa.PrimaryKeyConstraint('id'),
    schema='nhansu'
    )
    op.create_table('ChucDanhNghiepVuUser',
    sa.Column('id', sa.SMALLINT(), nullable=False),
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.Column('chuc_danh_nghiep_vu_id', sa.SMALLINT(), nullable=True),
    sa.Column('ngay_bat_dau', sa.DATE(), nullable=True),
    sa.ForeignKeyConstraint(['chuc_danh_nghiep_vu_id'], ['nhansu.ChucDanhNghiepVu.id'], ),
    sa.ForeignKeyConstraint(['user_id'], ['nhansu.User.id'], ),
    sa.PrimaryKeyConstraint('id'),
    schema='nhansu'
    )
    op.create_table('SoDienThoai',
    sa.Column('id', sa.SMALLINT(), nullable=False),
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.Column('so_dien_thoai', sa.NCHAR(length=10), nullable=True),
    sa.ForeignKeyConstraint(['user_id'], ['nhansu.User.id'], ),
    sa.PrimaryKeyConstraint('id'),
    schema='nhansu'
    )
    op.create_table('ViTri',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('user_id', sa.Integer(), nullable=False),
    sa.Column('bo_phan_id', sa.SMALLINT(), nullable=False),
    sa.Column('cong_viec', sa.NVARCHAR(length=255), nullable=True),
    sa.Column('ngay_bat_dau', sa.DATE(), nullable=True),
    sa.Column('ngay_ket_thuc', sa.DATE(), nullable=True),
    sa.ForeignKeyConstraint(['bo_phan_id'], ['nhansu.BoPhan.id'], ),
    sa.ForeignKeyConstraint(['user_id'], ['nhansu.User.id'], ),
    sa.PrimaryKeyConstraint('id'),
    schema='nhansu'
    )
    op.drop_table('BoPhan')
    op.drop_table('ChucDanhNghiepVu')
    op.drop_table('ChucDanhCongTacUser')
    op.drop_table('SoDienThoai')
    op.drop_table('ViTri')
    op.drop_table('ChucDanhCongTac')
    op.drop_table('ChucDanhNghiepVuUser')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('ChucDanhNghiepVuUser',
    sa.Column('id', sa.SMALLINT(), autoincrement=True, nullable=False, mssql_identity_start=1, mssql_identity_increment=1),
    sa.Column('user_id', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('chuc_danh_nghiep_vu_id', sa.SMALLINT(), autoincrement=False, nullable=True),
    sa.Column('ngay_bat_dau', sa.DATE(), autoincrement=False, nullable=True),
    sa.ForeignKeyConstraint(['chuc_danh_nghiep_vu_id'], ['ChucDanhNghiepVu.id'], name='FK__ChucDanhN__chuc___571DF1D5'),
    sa.ForeignKeyConstraint(['user_id'], ['nhansu.User.id'], name='FK__ChucDanhN__user___5812160E'),
    sa.PrimaryKeyConstraint('id', name='PK__ChucDanh__3213E83F467ECA3B')
    )
    op.create_table('ChucDanhCongTac',
    sa.Column('id', sa.SMALLINT(), autoincrement=True, nullable=False, mssql_identity_start=1, mssql_identity_increment=1),
    sa.Column('ten', sa.NVARCHAR(length=100), autoincrement=False, nullable=True),
    sa.PrimaryKeyConstraint('id', name='PK__ChucDanh__3213E83F6438590F')
    )
    op.create_table('ViTri',
    sa.Column('id', sa.INTEGER(), autoincrement=True, nullable=False, mssql_identity_start=1, mssql_identity_increment=1),
    sa.Column('user_id', sa.INTEGER(), autoincrement=False, nullable=False),
    sa.Column('bo_phan_id', sa.SMALLINT(), autoincrement=False, nullable=False),
    sa.Column('cong_viec', sa.NVARCHAR(length=255), autoincrement=False, nullable=True),
    sa.Column('ngay_bat_dau', sa.DATE(), autoincrement=False, nullable=True),
    sa.Column('ngay_ket_thuc', sa.DATE(), autoincrement=False, nullable=True),
    sa.ForeignKeyConstraint(['bo_phan_id'], ['BoPhan.id'], name='FK__ViTri__bo_phan_i__5DCAEF64'),
    sa.ForeignKeyConstraint(['user_id'], ['nhansu.User.id'], name='FK__ViTri__user_id__5EBF139D'),
    sa.PrimaryKeyConstraint('id', name='PK__ViTri__3213E83FFA7F9022')
    )
    op.create_table('SoDienThoai',
    sa.Column('id', sa.SMALLINT(), autoincrement=True, nullable=False, mssql_identity_start=1, mssql_identity_increment=1),
    sa.Column('user_id', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('so_dien_thoai', sa.NCHAR(length=10), autoincrement=False, nullable=True),
    sa.ForeignKeyConstraint(['user_id'], ['nhansu.User.id'], name='FK__SoDienTho__user___5AEE82B9'),
    sa.PrimaryKeyConstraint('id', name='PK__SoDienTh__3213E83F31D011AD')
    )
    op.create_table('ChucDanhCongTacUser',
    sa.Column('id', sa.SMALLINT(), autoincrement=True, nullable=False, mssql_identity_start=1, mssql_identity_increment=1),
    sa.Column('user_id', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('chuc_danh_cong_tac_id', sa.SMALLINT(), autoincrement=False, nullable=True),
    sa.Column('ngay_bat_dau', sa.DATE(), autoincrement=False, nullable=True),
    sa.ForeignKeyConstraint(['chuc_danh_cong_tac_id'], ['ChucDanhCongTac.id'], name='FK__ChucDanhC__chuc___534D60F1'),
    sa.ForeignKeyConstraint(['user_id'], ['nhansu.User.id'], name='FK__ChucDanhC__user___5441852A'),
    sa.PrimaryKeyConstraint('id', name='PK__ChucDanh__3213E83F8C8ABA94')
    )
    op.create_table('ChucDanhNghiepVu',
    sa.Column('id', sa.SMALLINT(), autoincrement=True, nullable=False, mssql_identity_start=1, mssql_identity_increment=1),
    sa.Column('ten', sa.NVARCHAR(length=100), autoincrement=False, nullable=True),
    sa.PrimaryKeyConstraint('id', name='PK__ChucDanh__3213E83F04F57BB6')
    )
    op.create_table('BoPhan',
    sa.Column('id', sa.SMALLINT(), autoincrement=True, nullable=False, mssql_identity_start=1, mssql_identity_increment=1),
    sa.Column('ten', sa.NVARCHAR(length=50), autoincrement=False, nullable=False),
    sa.Column('ma', sa.VARCHAR(length=3, collation='SQL_Latin1_General_CP1_CI_AS'), autoincrement=False, nullable=True),
    sa.Column('khoi', sa.VARCHAR(length=20, collation='SQL_Latin1_General_CP1_CI_AS'), autoincrement=False, nullable=True),
    sa.PrimaryKeyConstraint('id', name='PK__BoPhan__3213E83F93E28526')
    )
    op.drop_table('ViTri', schema='nhansu')
    op.drop_table('SoDienThoai', schema='nhansu')
    op.drop_table('ChucDanhNghiepVuUser', schema='nhansu')
    op.drop_table('ChucDanhCongTacUser', schema='nhansu')
    op.drop_index(op.f('ix_nhansu_User_username'), table_name='User', schema='nhansu')
    op.drop_index(op.f('ix_nhansu_User_ten'), table_name='User', schema='nhansu')
    op.drop_index(op.f('ix_nhansu_User_email'), table_name='User', schema='nhansu')
    op.drop_table('User', schema='nhansu')
    op.drop_table('ChucDanhNghiepVu', schema='nhansu')
    op.drop_table('ChucDanhCongTac', schema='nhansu')
    op.drop_table('BoPhan', schema='nhansu')
    # ### end Alembic commands ###
