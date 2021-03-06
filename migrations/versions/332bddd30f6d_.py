"""empty message

Revision ID: 332bddd30f6d
Revises: 73546aa484ba
Create Date: 2020-10-11 09:49:28.426105

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '332bddd30f6d'
down_revision = '73546aa484ba'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('ChucDanhCongTac', sa.Column('user_id', sa.Integer(), nullable=True), schema='NhanSu')
    op.create_foreign_key(None, 'ChucDanhCongTac', 'User', ['user_id'], ['id'], source_schema='NhanSu', referent_schema='NhanSu')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'ChucDanhCongTac', schema='NhanSu', type_='foreignkey')
    op.drop_column('ChucDanhCongTac', 'user_id', schema='NhanSu')
    # ### end Alembic commands ###
