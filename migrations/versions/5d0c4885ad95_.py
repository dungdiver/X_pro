"""empty message

Revision ID: 5d0c4885ad95
Revises: e67a451a5e49
Create Date: 2020-10-12 17:10:01.571409

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '5d0c4885ad95'
down_revision = 'e67a451a5e49'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('cats',
    sa.Column('name', sa.String(length=100), nullable=True),
    sa.Column('price', sa.Integer(), nullable=True),
    sa.Column('breed', sa.String(length=100), nullable=True),
    sa.Column('id', sa.Integer(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('dogs',
    sa.Column('name', sa.String(length=100), nullable=True),
    sa.Column('price', sa.Integer(), nullable=True),
    sa.Column('breed', sa.String(length=100), nullable=True),
    sa.Column('id', sa.Integer(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('dogs')
    op.drop_table('cats')
    # ### end Alembic commands ###
