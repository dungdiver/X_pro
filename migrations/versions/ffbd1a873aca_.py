"""empty message

Revision ID: ffbd1a873aca
Revises: 1ffa6d0c47c5
Create Date: 2020-10-09 13:48:01.969528

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'ffbd1a873aca'
down_revision = '1ffa6d0c47c5'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('ChucDanhCongTac',
    sa.Column('id', sa.SMALLINT(), nullable=False),
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.Column('Dm_Chuc_Danh_Cong_Tac_id', sa.SMALLINT(), nullable=True),
    sa.Column('ngay_bat_dau', sa.DATE(), nullable=True),
    sa.ForeignKeyConstraint(['Dm_Chuc_Danh_Cong_Tac_id'], ['Dm_ChucDanhCongTac.id'], ),
    sa.ForeignKeyConstraint(['user_id'], ['User.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('ChucDanhCongTac')
    # ### end Alembic commands ###
