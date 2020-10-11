"""empty message

Revision ID: e296be8d41df
Revises: 006000f74e99
Create Date: 2020-10-09 14:00:46.012292

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'e296be8d41df'
down_revision = '006000f74e99'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('ChucDanhCongTac',
    sa.Column('id', sa.SMALLINT(), nullable=False),
    sa.Column('ten', sa.NVARCHAR(length=100), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('ChucDanhCongTacUser',
    sa.Column('id', sa.SMALLINT(), nullable=False),
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.Column('Chuc_Danh_Cong_Tac_id', sa.SMALLINT(), nullable=True),
    sa.Column('ngay_bat_dau', sa.DATE(), nullable=True),
    sa.ForeignKeyConstraint(['Chuc_Danh_Cong_Tac_id'], ['ChucDanhCongTac.id'], ),
    sa.ForeignKeyConstraint(['user_id'], ['User.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('ChucDanhCongTacUser')
    op.drop_table('ChucDanhCongTac')
    # ### end Alembic commands ###