"""empty message

Revision ID: 55d2144d2eaa
Revises: 6d15f652e283
Create Date: 2020-10-09 16:52:48.222580

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '55d2144d2eaa'
down_revision = '6d15f652e283'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('User',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('ho_dem', sa.NVARCHAR(length=30), nullable=True),
    sa.Column('ten', sa.NVARCHAR(length=15), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    schema='NhanSu'
    )
    op.create_index(op.f('ix_NhanSu_User_ten'), 'User', ['ten'], unique=False, schema='NhanSu')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_NhanSu_User_ten'), table_name='User', schema='NhanSu')
    op.drop_table('User', schema='NhanSu')
    # ### end Alembic commands ###