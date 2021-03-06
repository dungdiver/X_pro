"""empty message

Revision ID: 2fb37819afb5
Revises: 3ce2982d9618
Create Date: 2020-10-09 07:22:52.970953

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '2fb37819afb5'
down_revision = '3ce2982d9618'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('Dm_chuc_danh_cong_tac',
    sa.Column('id', sa.SMALLINT(), nullable=False),
    sa.Column('ten', sa.NVARCHAR(length=100), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('Dm_chuc_danh_cong_tac')
    # ### end Alembic commands ###
