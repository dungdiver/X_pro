"""empty message

Revision ID: 912b84d6daeb
Revises: f69076518c9d
Create Date: 2020-10-13 09:18:59.623032

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '912b84d6daeb'
down_revision = 'f69076518c9d'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('GiayTo',
    sa.Column('id', sa.SMALLINT(), nullable=False),
    sa.Column('ten', sa.NVARCHAR(length=100), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    schema='NhanSu'
    )
    op.create_table('HinhThucKhenThuong',
    sa.Column('id', sa.SMALLINT(), nullable=False),
    sa.Column('ten', sa.NVARCHAR(length=100), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    schema='NhanSu'
    )
    op.create_table('KhenThuongTapThe',
    sa.Column('id', sa.INTEGER(), nullable=False),
    sa.Column('ten_tap_the', sa.NVARCHAR(), nullable=True),
    sa.Column('hinh_thuc_khen_thuong_id', sa.SMALLINT(), nullable=True),
    sa.Column('so_quyet_dinh', sa.NVARCHAR(length=50), nullable=True),
    sa.Column('ngay_quyet_dinh', sa.DATE(), nullable=True),
    sa.Column('don_vi_khen', sa.NVARCHAR(length=250), nullable=True),
    sa.Column('noi_dung', sa.NVARCHAR(length=250), nullable=True),
    sa.Column('so_tien', sa.INTEGER(), nullable=True),
    sa.Column('ghi_chu', sa.NVARCHAR(), nullable=True),
    sa.ForeignKeyConstraint(['hinh_thuc_khen_thuong_id'], ['NhanSu.HinhThucKhenThuong.id'], ),
    sa.PrimaryKeyConstraint('id'),
    schema='NhanSu'
    )
    op.create_table('GiayToCanBo',
    sa.Column('id', sa.INTEGER(), nullable=False),
    sa.Column('can_bo_id', sa.INTEGER(), nullable=True),
    sa.Column('giay_to_id', sa.SMALLINT(), nullable=True),
    sa.Column('so', sa.NVARCHAR(length=50), nullable=True),
    sa.Column('ngay_cap', sa.DATE(), nullable=True),
    sa.Column('tinh_trang', sa.NVARCHAR(length=30), nullable=True),
    sa.Column('loai_cap', sa.NVARCHAR(length=30), nullable=True),
    sa.Column('ngay_thu', sa.DATE(), nullable=True),
    sa.Column('ghi_chu', sa.NVARCHAR(), nullable=True),
    sa.ForeignKeyConstraint(['can_bo_id'], ['NhanSu.CanBo.id'], ),
    sa.ForeignKeyConstraint(['giay_to_id'], ['NhanSu.GiayTo.id'], ),
    sa.PrimaryKeyConstraint('id'),
    schema='NhanSu'
    )
    op.create_table('KhenThuongCaNhan',
    sa.Column('id', sa.INTEGER(), nullable=False),
    sa.Column('can_bo_id', sa.INTEGER(), nullable=True),
    sa.Column('hinh_thuc_khen_thuong_id', sa.SMALLINT(), nullable=True),
    sa.Column('so_quyet_dinh', sa.NVARCHAR(length=50), nullable=True),
    sa.Column('ngay_quyet_dinh', sa.DATE(), nullable=True),
    sa.Column('don_vi_khen', sa.NVARCHAR(length=250), nullable=True),
    sa.Column('noi_dung', sa.NVARCHAR(length=250), nullable=True),
    sa.Column('so_tien', sa.INTEGER(), nullable=True),
    sa.Column('ghi_chu', sa.NVARCHAR(), nullable=True),
    sa.ForeignKeyConstraint(['can_bo_id'], ['NhanSu.CanBo.id'], ),
    sa.ForeignKeyConstraint(['hinh_thuc_khen_thuong_id'], ['NhanSu.HinhThucKhenThuong.id'], ),
    sa.PrimaryKeyConstraint('id'),
    schema='NhanSu'
    )
    op.create_table('PltdCaNhanTheoNam',
    sa.Column('id', sa.INTEGER(), nullable=False),
    sa.Column('can_bo_id', sa.INTEGER(), nullable=True),
    sa.Column('nam', sa.SMALLINT(), nullable=True),
    sa.Column('phan_loai', sa.NVARCHAR(length=5), nullable=True),
    sa.Column('ghi_chu', sa.NVARCHAR(), nullable=True),
    sa.ForeignKeyConstraint(['can_bo_id'], ['NhanSu.CanBo.id'], ),
    sa.PrimaryKeyConstraint('id'),
    schema='NhanSu'
    )
    op.create_table('PltdCaNhanTheoThang',
    sa.Column('id', sa.INTEGER(), nullable=False),
    sa.Column('can_bo_id', sa.INTEGER(), nullable=True),
    sa.Column('thang', sa.DATE(), nullable=True),
    sa.Column('phan_loai', sa.NVARCHAR(length=5), nullable=True),
    sa.Column('ghi_chu', sa.NVARCHAR(), nullable=True),
    sa.ForeignKeyConstraint(['can_bo_id'], ['NhanSu.CanBo.id'], ),
    sa.PrimaryKeyConstraint('id'),
    schema='NhanSu'
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('PltdCaNhanTheoThang', schema='NhanSu')
    op.drop_table('PltdCaNhanTheoNam', schema='NhanSu')
    op.drop_table('KhenThuongCaNhan', schema='NhanSu')
    op.drop_table('GiayToCanBo', schema='NhanSu')
    op.drop_table('KhenThuongTapThe', schema='NhanSu')
    op.drop_table('HinhThucKhenThuong', schema='NhanSu')
    op.drop_table('GiayTo', schema='NhanSu')
    # ### end Alembic commands ###
