"""empty message

Revision ID: e69ab590d22a
Revises: 5d0c4885ad95
Create Date: 2020-10-13 07:26:06.298486

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mssql

# revision identifiers, used by Alembic.
revision = 'e69ab590d22a'
down_revision = '5d0c4885ad95'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('CanBo',
    sa.Column('id', sa.INTEGER(), nullable=False),
    sa.Column('ho_dem', sa.NVARCHAR(length=30), nullable=True),
    sa.Column('ten', sa.NVARCHAR(length=15), nullable=True),
    sa.Column('ngay_sinh', sa.Date(), nullable=True),
    sa.Column('gioi_tinh', sa.NCHAR(length=1), nullable=True),
    sa.Column('nhom_mau', sa.VARCHAR(length=10), nullable=True),
    sa.Column('dan_toc', sa.NVARCHAR(length=20), nullable=True),
    sa.Column('que', sa.NVARCHAR(length=100), nullable=True),
    sa.Column('dktt', sa.NVARCHAR(length=100), nullable=True),
    sa.Column('noi_o', sa.NVARCHAR(length=100), nullable=True),
    sa.Column('so_hieu', sa.VARCHAR(length=6), nullable=True),
    sa.Column('ngay_vao_cong_an', sa.Date(), nullable=True),
    sa.Column('nganh_ngoai', sa.Boolean(), nullable=True),
    sa.Column('trinh_do_chinh_tri', sa.NVARCHAR(length=30), nullable=True),
    sa.Column('trinh_do_ngoai_ngu', sa.NVARCHAR(length=30), nullable=True),
    sa.Column('trinh_do_tin_hoc', sa.NVARCHAR(length=30), nullable=True),
    sa.Column('trang_thai_cong_tac_id', sa.SMALLINT(), nullable=True),
    sa.ForeignKeyConstraint(['trang_thai_cong_tac_id'], ['NhanSu.TrangThaiCongTac.id'], ),
    sa.PrimaryKeyConstraint('id'),
    schema='NhanSu'
    )
    op.create_index(op.f('ix_NhanSu_CanBo_ten'), 'CanBo', ['ten'], unique=False, schema='NhanSu')
    op.create_table('CapBacCanBo',
    sa.Column('id', sa.INTEGER(), nullable=False),
    sa.Column('can_bo_id', sa.Integer(), nullable=True),
    sa.Column('cap_bac_id', sa.SMALLINT(), nullable=True),
    sa.Column('ngay_bat_dau', sa.DATE(), nullable=True),
    sa.ForeignKeyConstraint(['can_bo_id'], ['NhanSu.CanBo.id'], ),
    sa.ForeignKeyConstraint(['cap_bac_id'], ['NhanSu.CapBac.id'], ),
    sa.PrimaryKeyConstraint('id'),
    schema='NhanSu'
    )
    op.create_table('ChucDanhCongTacCanBo',
    sa.Column('id', sa.SMALLINT(), nullable=False),
    sa.Column('can_bo_id', sa.Integer(), nullable=True),
    sa.Column('chuc_danh_cong_tac_id', sa.SMALLINT(), nullable=True),
    sa.Column('ngay_bat_dau', sa.DATE(), nullable=True),
    sa.ForeignKeyConstraint(['can_bo_id'], ['NhanSu.CanBo.id'], ),
    sa.ForeignKeyConstraint(['chuc_danh_cong_tac_id'], ['NhanSu.ChucDanhCongTac.id'], ),
    sa.PrimaryKeyConstraint('id'),
    schema='NhanSu'
    )
    op.create_table('ChucDanhNghiepVuCanBo',
    sa.Column('id', sa.SMALLINT(), nullable=False),
    sa.Column('can_bo_id', sa.Integer(), nullable=True),
    sa.Column('chuc_danh_nghiep_vu_id', sa.SMALLINT(), nullable=True),
    sa.Column('ngay_bat_dau', sa.DATE(), nullable=True),
    sa.ForeignKeyConstraint(['can_bo_id'], ['NhanSu.CanBo.id'], ),
    sa.ForeignKeyConstraint(['chuc_danh_nghiep_vu_id'], ['NhanSu.ChucDanhNghiepVu.id'], ),
    sa.PrimaryKeyConstraint('id'),
    schema='NhanSu'
    )
    op.create_table('ChucDanhTuPhapCanBo',
    sa.Column('id', sa.SMALLINT(), nullable=False),
    sa.Column('can_bo_id', sa.Integer(), nullable=True),
    sa.Column('chuc_danh_tu_phap_id', sa.SMALLINT(), nullable=True),
    sa.Column('ngay_bat_dau', sa.DATE(), nullable=True),
    sa.Column('ngay_ket_thuc', sa.DATE(), nullable=True),
    sa.ForeignKeyConstraint(['can_bo_id'], ['NhanSu.CanBo.id'], ),
    sa.ForeignKeyConstraint(['chuc_danh_tu_phap_id'], ['NhanSu.ChucDanhTuPhap.id'], ),
    sa.PrimaryKeyConstraint('id'),
    schema='NhanSu'
    )
    op.create_table('HeSoLuongCanBo',
    sa.Column('id', sa.INTEGER(), nullable=False),
    sa.Column('can_bo_id', sa.Integer(), nullable=True),
    sa.Column('he_so', sa.DECIMAL(precision=4, scale=2), nullable=True),
    sa.Column('ngay_bat_dau', sa.DATE(), nullable=True),
    sa.ForeignKeyConstraint(['can_bo_id'], ['NhanSu.CanBo.id'], ),
    sa.PrimaryKeyConstraint('id'),
    schema='NhanSu'
    )
    op.drop_table('ChucDanhCongTacUser', schema='NhanSu')
    op.drop_table('CapBacUser', schema='NhanSu')
    op.drop_table('ChucDanhNghiepVuUser', schema='NhanSu')
    op.drop_table('ChucDanhTuPhapUser', schema='NhanSu')
    op.drop_table('HeSoLuongUser', schema='NhanSu')
    op.add_column('SoDienThoai', sa.Column('can_bo_id', sa.Integer(), nullable=True), schema='NhanSu')
    op.drop_constraint('FK__SoDienTho__user___44CA3770', 'SoDienThoai', schema='NhanSu', type_='foreignkey')
    op.create_foreign_key(None, 'SoDienThoai', 'CanBo', ['can_bo_id'], ['id'], source_schema='NhanSu', referent_schema='NhanSu')
    op.drop_column('SoDienThoai', 'user_id', schema='NhanSu')
    op.drop_index('ix_NhanSu_User_ten', table_name='User', schema='NhanSu')
    op.drop_constraint('FK__User__trang_thai__2FCF1A8A', 'User', schema='NhanSu', type_='foreignkey')
    op.drop_column('User', 'so_hieu', schema='NhanSu')
    op.drop_column('User', 'nganh_ngoai', schema='NhanSu')
    op.drop_column('User', 'ngay_vao_cong_an', schema='NhanSu')
    op.drop_column('User', 'trinh_do_tin_hoc', schema='NhanSu')
    op.drop_column('User', 'trang_thai_cong_tac_id', schema='NhanSu')
    op.drop_column('User', 'ho_dem', schema='NhanSu')
    op.drop_column('User', 'dktt', schema='NhanSu')
    op.drop_column('User', 'dan_toc', schema='NhanSu')
    op.drop_column('User', 'ngay_sinh', schema='NhanSu')
    op.drop_column('User', 'ten', schema='NhanSu')
    op.drop_column('User', 'trinh_do_ngoai_ngu', schema='NhanSu')
    op.drop_column('User', 'trinh_do_chinh_tri', schema='NhanSu')
    op.drop_column('User', 'gioi_tinh', schema='NhanSu')
    op.drop_column('User', 'nhom_mau', schema='NhanSu')
    op.drop_column('User', 'que', schema='NhanSu')
    op.drop_column('User', 'noi_o', schema='NhanSu')
    op.add_column('ViTri', sa.Column('can_bo_id', sa.Integer(), nullable=False), schema='NhanSu')
    op.drop_constraint('FK__ViTri__user_id__489AC854', 'ViTri', schema='NhanSu', type_='foreignkey')
    op.create_foreign_key(None, 'ViTri', 'CanBo', ['can_bo_id'], ['id'], source_schema='NhanSu', referent_schema='NhanSu')
    op.drop_column('ViTri', 'user_id', schema='NhanSu')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('ViTri', sa.Column('user_id', sa.INTEGER(), autoincrement=False, nullable=False), schema='NhanSu')
    op.drop_constraint(None, 'ViTri', schema='NhanSu', type_='foreignkey')
    op.create_foreign_key('FK__ViTri__user_id__489AC854', 'ViTri', 'User', ['user_id'], ['id'], source_schema='NhanSu', referent_schema='NhanSu')
    op.drop_column('ViTri', 'can_bo_id', schema='NhanSu')
    op.add_column('User', sa.Column('noi_o', sa.NVARCHAR(length=100), autoincrement=False, nullable=True), schema='NhanSu')
    op.add_column('User', sa.Column('que', sa.NVARCHAR(length=100), autoincrement=False, nullable=True), schema='NhanSu')
    op.add_column('User', sa.Column('nhom_mau', sa.VARCHAR(length=10, collation='SQL_Latin1_General_CP1_CI_AS'), autoincrement=False, nullable=True), schema='NhanSu')
    op.add_column('User', sa.Column('gioi_tinh', sa.NCHAR(length=1), autoincrement=False, nullable=True), schema='NhanSu')
    op.add_column('User', sa.Column('trinh_do_chinh_tri', sa.NVARCHAR(length=30), autoincrement=False, nullable=True), schema='NhanSu')
    op.add_column('User', sa.Column('trinh_do_ngoai_ngu', sa.NVARCHAR(length=30), autoincrement=False, nullable=True), schema='NhanSu')
    op.add_column('User', sa.Column('ten', sa.NVARCHAR(length=15), autoincrement=False, nullable=True), schema='NhanSu')
    op.add_column('User', sa.Column('ngay_sinh', sa.DATE(), autoincrement=False, nullable=True), schema='NhanSu')
    op.add_column('User', sa.Column('dan_toc', sa.NVARCHAR(length=20), autoincrement=False, nullable=True), schema='NhanSu')
    op.add_column('User', sa.Column('dktt', sa.NVARCHAR(length=100), autoincrement=False, nullable=True), schema='NhanSu')
    op.add_column('User', sa.Column('ho_dem', sa.NVARCHAR(length=30), autoincrement=False, nullable=True), schema='NhanSu')
    op.add_column('User', sa.Column('trang_thai_cong_tac_id', sa.SMALLINT(), autoincrement=False, nullable=True), schema='NhanSu')
    op.add_column('User', sa.Column('trinh_do_tin_hoc', sa.NVARCHAR(length=30), autoincrement=False, nullable=True), schema='NhanSu')
    op.add_column('User', sa.Column('ngay_vao_cong_an', sa.DATE(), autoincrement=False, nullable=True), schema='NhanSu')
    op.add_column('User', sa.Column('nganh_ngoai', mssql.BIT(), autoincrement=False, nullable=True), schema='NhanSu')
    op.add_column('User', sa.Column('so_hieu', sa.VARCHAR(length=6, collation='SQL_Latin1_General_CP1_CI_AS'), autoincrement=False, nullable=True), schema='NhanSu')
    op.create_foreign_key('FK__User__trang_thai__2FCF1A8A', 'User', 'TrangThaiCongTac', ['trang_thai_cong_tac_id'], ['id'], source_schema='NhanSu', referent_schema='NhanSu')
    op.create_index('ix_NhanSu_User_ten', 'User', ['ten'], unique=False, schema='NhanSu')
    op.add_column('SoDienThoai', sa.Column('user_id', sa.INTEGER(), autoincrement=False, nullable=True), schema='NhanSu')
    op.drop_constraint(None, 'SoDienThoai', schema='NhanSu', type_='foreignkey')
    op.create_foreign_key('FK__SoDienTho__user___44CA3770', 'SoDienThoai', 'User', ['user_id'], ['id'], source_schema='NhanSu', referent_schema='NhanSu')
    op.drop_column('SoDienThoai', 'can_bo_id', schema='NhanSu')
    op.create_table('HeSoLuongUser',
    sa.Column('id', sa.INTEGER(), autoincrement=True, nullable=False, mssql_identity_start=1, mssql_identity_increment=1),
    sa.Column('user_id', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('he_so', sa.DECIMAL(precision=4, scale=2), autoincrement=False, nullable=True),
    sa.Column('ngay_bat_dau', sa.DATE(), autoincrement=False, nullable=True),
    sa.ForeignKeyConstraint(['user_id'], ['NhanSu.User.id'], name='FK__HeSoLuong__user___41EDCAC5'),
    sa.PrimaryKeyConstraint('id', name='PK__HeSoLuon__3213E83F3D9EB5CD'),
    schema='NhanSu'
    )
    op.create_table('ChucDanhTuPhapUser',
    sa.Column('id', sa.SMALLINT(), autoincrement=True, nullable=False, mssql_identity_start=1, mssql_identity_increment=1),
    sa.Column('user_id', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('chuc_danh_tu_phap_id', sa.SMALLINT(), autoincrement=False, nullable=True),
    sa.Column('ngay_bat_dau', sa.DATE(), autoincrement=False, nullable=True),
    sa.Column('ngay_ket_thuc', sa.DATE(), autoincrement=False, nullable=True),
    sa.ForeignKeyConstraint(['chuc_danh_tu_phap_id'], ['NhanSu.ChucDanhTuPhap.id'], name='FK__ChucDanhT__chuc___3E1D39E1'),
    sa.ForeignKeyConstraint(['user_id'], ['NhanSu.User.id'], name='FK__ChucDanhT__user___3F115E1A'),
    sa.PrimaryKeyConstraint('id', name='PK__ChucDanh__3213E83F44920B68'),
    schema='NhanSu'
    )
    op.create_table('ChucDanhNghiepVuUser',
    sa.Column('id', sa.SMALLINT(), autoincrement=True, nullable=False, mssql_identity_start=1, mssql_identity_increment=1),
    sa.Column('user_id', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('chuc_danh_nghiep_vu_id', sa.SMALLINT(), autoincrement=False, nullable=True),
    sa.Column('ngay_bat_dau', sa.DATE(), autoincrement=False, nullable=True),
    sa.ForeignKeyConstraint(['chuc_danh_nghiep_vu_id'], ['NhanSu.ChucDanhNghiepVu.id'], name='FK__ChucDanhN__chuc___3A4CA8FD'),
    sa.ForeignKeyConstraint(['user_id'], ['NhanSu.User.id'], name='FK__ChucDanhN__user___3B40CD36'),
    sa.PrimaryKeyConstraint('id', name='PK__ChucDanh__3213E83F66F9C81E'),
    schema='NhanSu'
    )
    op.create_table('CapBacUser',
    sa.Column('id', sa.INTEGER(), autoincrement=True, nullable=False, mssql_identity_start=1, mssql_identity_increment=1),
    sa.Column('user_id', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('cap_bac_id', sa.SMALLINT(), autoincrement=False, nullable=True),
    sa.Column('ngay_bat_dau', sa.DATE(), autoincrement=False, nullable=True),
    sa.ForeignKeyConstraint(['cap_bac_id'], ['NhanSu.CapBac.id'], name='FK__CapBacUse__cap_b__32AB8735'),
    sa.ForeignKeyConstraint(['user_id'], ['NhanSu.User.id'], name='FK__CapBacUse__user___339FAB6E'),
    sa.PrimaryKeyConstraint('id', name='PK__CapBacUs__3213E83F71EF910A'),
    schema='NhanSu'
    )
    op.create_table('ChucDanhCongTacUser',
    sa.Column('id', sa.SMALLINT(), autoincrement=True, nullable=False, mssql_identity_start=1, mssql_identity_increment=1),
    sa.Column('user_id', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('chuc_danh_cong_tac_id', sa.SMALLINT(), autoincrement=False, nullable=True),
    sa.Column('ngay_bat_dau', sa.DATE(), autoincrement=False, nullable=True),
    sa.ForeignKeyConstraint(['chuc_danh_cong_tac_id'], ['NhanSu.ChucDanhCongTac.id'], name='FK__ChucDanhC__chuc___367C1819'),
    sa.ForeignKeyConstraint(['user_id'], ['NhanSu.User.id'], name='FK__ChucDanhC__user___37703C52'),
    sa.PrimaryKeyConstraint('id', name='PK__ChucDanh__3213E83FB6B44B67'),
    schema='NhanSu'
    )
    op.drop_table('HeSoLuongCanBo', schema='NhanSu')
    op.drop_table('ChucDanhTuPhapCanBo', schema='NhanSu')
    op.drop_table('ChucDanhNghiepVuCanBo', schema='NhanSu')
    op.drop_table('ChucDanhCongTacCanBo', schema='NhanSu')
    op.drop_table('CapBacCanBo', schema='NhanSu')
    op.drop_index(op.f('ix_NhanSu_CanBo_ten'), table_name='CanBo', schema='NhanSu')
    op.drop_table('CanBo', schema='NhanSu')
    # ### end Alembic commands ###
