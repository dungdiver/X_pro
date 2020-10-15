"""empty message

Revision ID: dcc24aff888f
Revises: 7946497b3a52
Create Date: 2020-10-13 10:58:06.455352

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'dcc24aff888f'
down_revision = '7946497b3a52'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('CoSoDaoTao',
    sa.Column('id', sa.SMALLINT(), nullable=False),
    sa.Column('ten', sa.NVARCHAR(length=100), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    schema='NhanSu'
    )
    op.create_table('TrinhDoNghiepVu',
    sa.Column('id', sa.SMALLINT(), nullable=False),
    sa.Column('ten', sa.NVARCHAR(length=20), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    schema='NhanSu'
    )
    op.create_table('TrinhDoNghiepVuCanBo',
    sa.Column('id', sa.SMALLINT(), nullable=False),
    sa.Column('can_bo_id', sa.INTEGER(), nullable=True),
    sa.Column('trinh_do_nghiep_vu_id', sa.SMALLINT(), nullable=True),
    sa.Column('co_so_dao_tao_id', sa.SMALLINT(), nullable=True),
    sa.Column('chuyen_nganh', sa.NVARCHAR(length=50), nullable=True),
    sa.Column('ngay_bat_dau', sa.DATE(), nullable=True),
    sa.Column('ngay_ket_thuc', sa.DATE(), nullable=True),
    sa.Column('ket_qua', sa.NVARCHAR(length=50), nullable=True),
    sa.Column('ghi_chu', sa.NVARCHAR(), nullable=True),
    sa.ForeignKeyConstraint(['can_bo_id'], ['NhanSu.CanBo.id'], ),
    sa.ForeignKeyConstraint(['co_so_dao_tao_id'], ['NhanSu.CoSoDaoTao.id'], ),
    sa.ForeignKeyConstraint(['trinh_do_nghiep_vu_id'], ['NhanSu.TrinhDoNghiepVu.id'], ),
    sa.PrimaryKeyConstraint('id'),
    schema='NhanSu'
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('TrinhDoNghiepVuCanBo', schema='NhanSu')
    op.drop_table('TrinhDoNghiepVu', schema='NhanSu')
    op.drop_table('CoSoDaoTao', schema='NhanSu')
    # ### end Alembic commands ###