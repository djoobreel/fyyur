"""empty message

Revision ID: 2a2c29f2579a
Revises: 990f990bdcf1
Create Date: 2022-06-11 14:29:10.956540

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '2a2c29f2579a'
down_revision = '990f990bdcf1'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('Venue', 'image_link')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('Venue', sa.Column('image_link', sa.VARCHAR(length=500), autoincrement=False, nullable=True))
    # ### end Alembic commands ###
