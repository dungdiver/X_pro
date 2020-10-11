"""empty message

Revision ID: 73546aa484ba
Revises: 75da0c6251b2
Create Date: 2020-10-11 09:19:42.426545

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '73546aa484ba'
down_revision = '75da0c6251b2'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('TrangThaiCongTac',
    sa.Column('id', sa.SMALLINT(), nullable=False),
    sa.Column('ten', sa.NVARCHAR(length=25), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    schema='NhanSu'
    )
    op.drop_table('TrangThaiUser', schema='NhanSu')
    op.add_column('User', sa.Column('trang_thai_cong_tac_id', sa.SMALLINT(), nullable=True), schema='NhanSu')
    op.create_foreign_key(None, 'User', 'TrangThaiCongTac', ['trang_thai_cong_tac_id'], ['id'], source_schema='NhanSu', referent_schema='NhanSu')
    op.drop_column('User', 'trang_thai_user_id', schema='NhanSu')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('User', sa.Column('trang_thai_user_id', sa.SMALLINT(), autoincrement=False, nullable=True), schema='NhanSu')
    op.drop_constraint(None, 'User', schema='NhanSu', type_='foreignkey')
    op.drop_column('User', 'trang_thai_cong_tac_id', schema='NhanSu')
    op.create_table('TrangThaiUser',
    sa.Column('id', sa.SMALLINT(), autoincrement=True, nullable=False, mssql_identity_start=1, mssql_identity_increment=1),
    sa.Column('ten', sa.NVARCHAR(length=25), autoincrement=False, nullable=True),
    sa.PrimaryKeyConstraint('id', name='PK__TrangTha__3213E83F2A7935EA'),
    schema='NhanSu'
    )
    op.drop_table('TrangThaiCongTac', schema='NhanSu')
    # ### end Alembic commands ###