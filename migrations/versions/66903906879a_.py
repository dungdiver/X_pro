"""empty message

Revision ID: 66903906879a
Revises: 9caece05ccac
Create Date: 2020-10-08 16:31:12.091067

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '66903906879a'
down_revision = '9caece05ccac'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('User', 'dem')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('User', sa.Column('dem', sa.NVARCHAR(), autoincrement=False, nullable=True))
    # ### end Alembic commands ###
