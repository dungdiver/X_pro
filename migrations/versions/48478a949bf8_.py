"""empty message

Revision ID: 48478a949bf8
Revises: 3bb932cad882
Create Date: 2020-10-11 10:22:29.796490

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mssql

# revision identifiers, used by Alembic.
revision = '48478a949bf8'
down_revision = '3bb932cad882'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('CapBac',
    sa.Column('id', sa.SMALLINT(), nullable=False),
    sa.Column('ten', sa.NVARCHAR(length=100), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    schema='NhanSu'
    )
    op.create_table('CapBacUser',
    sa.Column('id', sa.INTEGER(), nullable=False),
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.Column('cap_bac_id', sa.SMALLINT(), nullable=True),
    sa.Column('ngay_bat_dau', sa.DATE(), nullable=True),
    sa.ForeignKeyConstraint(['cap_bac_id'], ['NhanSu.CapBac.id'], ),
    sa.ForeignKeyConstraint(['user_id'], ['NhanSu.User.id'], ),
    sa.PrimaryKeyConstraint('id'),
    schema='NhanSu'
    )
    op.drop_table('sysdiagrams')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('sysdiagrams',
    sa.Column('name', sa.NVARCHAR(length=128), autoincrement=False, nullable=False),
    sa.Column('principal_id', sa.INTEGER(), autoincrement=False, nullable=False),
    sa.Column('diagram_id', sa.INTEGER(), autoincrement=True, nullable=False, mssql_identity_start=1, mssql_identity_increment=1),
    sa.Column('version', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('definition', mssql.VARBINARY(), autoincrement=False, nullable=True),
    sa.PrimaryKeyConstraint('diagram_id', name='PK__sysdiagr__C2B05B61A44117A9')
    )
    op.drop_table('CapBacUser', schema='NhanSu')
    op.drop_table('CapBac', schema='NhanSu')
    # ### end Alembic commands ###