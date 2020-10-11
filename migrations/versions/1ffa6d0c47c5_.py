"""empty message

Revision ID: 1ffa6d0c47c5
Revises: 45529921ba5a
Create Date: 2020-10-09 13:42:51.289478

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '1ffa6d0c47c5'
down_revision = '45529921ba5a'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('ChucDanhCongTac',
    sa.Column('id', sa.SMALLINT(), nullable=False),
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.Column('Dm_Chuc_Danh_Cong_Tac_id', sa.Integer(), nullable=True),
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
