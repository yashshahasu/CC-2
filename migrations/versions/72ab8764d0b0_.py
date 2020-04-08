"""empty message

Revision ID: 72ab8764d0b0
Revises: 
Create Date: 2020-04-06 19:11:20.118192

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '72ab8764d0b0'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('accounts',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('account_no', sa.Integer(), nullable=False),
    sa.Column('account_type', sa.String(length=128), nullable=False),
    sa.Column('logs', sa.String(length=128), nullable=False),
    sa.Column('timestamp', sa.DateTime(), nullable=True),
    sa.Column('amount', sa.Integer(), nullable=False),
    sa.Column('user_id', sa.Integer(), nullable=False),
    sa.Column('isactive', sa.Boolean(), nullable=False),
    sa.ForeignKeyConstraint(['user_id'], ['users.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('otp',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('account_no', sa.Integer(), nullable=False),
    sa.Column('user_id', sa.Integer(), nullable=False),
    sa.Column('isactive', sa.Boolean(), nullable=False),
    sa.Column('timestamp', sa.DateTime(), nullable=True),
    sa.Column('role', sa.String(length=128), nullable=False),
    sa.Column('otp', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['user_id'], ['users.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('requests',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('status', sa.String(length=128), nullable=False),
    sa.Column('action', sa.String(length=128), nullable=False),
    sa.Column('role', sa.String(length=128), nullable=False),
    sa.Column('action_type', sa.String(length=128), nullable=False),
    sa.Column('user_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['user_id'], ['users.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.add_column('users', sa.Column('is_valid', sa.Boolean(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('users', 'is_valid')
    op.drop_table('requests')
    op.drop_table('otp')
    op.drop_table('accounts')
    # ### end Alembic commands ###
