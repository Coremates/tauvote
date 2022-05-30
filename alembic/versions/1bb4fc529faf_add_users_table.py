"""add users table

Revision ID: 1bb4fc529faf
Revises: d94ccb16950c
Create Date: 2022-05-29 22:31:34.278570

"""
from cgitb import text
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '1bb4fc529faf'
down_revision = 'd94ccb16950c'
branch_labels = None
depends_on = None


def upgrade():
    op.create_table('users', 
                    sa.Column('id', sa.Integer(), nullable=False),
                    sa.Column('email', sa.String(), nullable=False),
                    sa.Column('password', sa.String(), nullable=False),
                    sa.Column('created_at', sa.TIMESTAMP(timezone=True),
                               server_default=sa.text('now()'), nullable=False),
                    sa.PrimaryKeyConstraint('id'),
                    sa.UniqueConstraint('email')
                    )
    pass


def downgrade():
    op.drop_table('users')
    pass
