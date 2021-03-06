"""empty message

Revision ID: 241184c0a524
Revises: 915fc55bc21f
Create Date: 2020-10-05 09:52:36.579162

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '241184c0a524'
down_revision = '915fc55bc21f'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('User', sa.Column('dan_toc', sa.NVARCHAR(length=20), nullable=True))
    op.drop_column('User', 'dantoc')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('User', sa.Column('dantoc', sa.NVARCHAR(length=20), autoincrement=False, nullable=True))
    op.drop_column('User', 'dan_toc')
    # ### end Alembic commands ###
