"""empty message

Revision ID: 7696580fc0e9
Revises: 9c288305c147
Create Date: 2019-09-25 17:38:12.369379

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '7696580fc0e9'
down_revision = '9c288305c147'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('users', sa.Column('admin', sa.Boolean(), nullable=True))
    op.execute('UPDATE users SET admin=False')
    op.alter_column('users', 'admin', nullable=False)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('users', 'admin')
    # ### end Alembic commands ###
