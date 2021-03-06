"""empty message

Revision ID: 35a56edf325f
Revises: 842f813570b7
Create Date: 2020-10-08 16:20:06.585576

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '35a56edf325f'
down_revision = '842f813570b7'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('parent')
    op.drop_table('child')
    op.add_column('User', sa.Column('is_admin', sa.Boolean(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('User', 'is_admin')
    op.create_table('child',
    sa.Column('id', sa.INTEGER(), autoincrement=True, nullable=False, mssql_identity_start=1, mssql_identity_increment=1),
    sa.Column('parent_id', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.ForeignKeyConstraint(['parent_id'], ['parent.id'], name='FK__child__parent_id__5BE2A6F2'),
    sa.PrimaryKeyConstraint('id', name='PK__child__3213E83F35FB58F8')
    )
    op.create_table('parent',
    sa.Column('id', sa.INTEGER(), autoincrement=True, nullable=False, mssql_identity_start=1, mssql_identity_increment=1),
    sa.PrimaryKeyConstraint('id', name='PK__parent__3213E83FD9B77474')
    )
    # ### end Alembic commands ###
