"""add content column to posts table

Revision ID: d94ccb16950c
Revises: bd15263e2e68
Create Date: 2022-05-29 22:17:27.831912

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'd94ccb16950c'
down_revision = 'bd15263e2e68'
branch_labels = None
depends_on = None


def upgrade():
    op.add_column('posts', sa.Column('content', sa.String(), nullable=False))
    pass


def downgrade():
    op.drop_column('posts', 'content')
    pass
