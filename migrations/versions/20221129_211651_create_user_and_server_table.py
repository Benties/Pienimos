"""create user and server table

Revision ID: 0fdca5ca5f88
Revises:
Create Date: 2022-11-29 21:16:51.188174

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '0fdca5ca5f88'
down_revision = None
branch_labels = None
depends_on = None

import os
environment = os.getenv("FLASK_ENV")
SCHEMA = os.environ.get("SCHEMA")

def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('users',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('first_name', sa.String(length=50), nullable=False),
    sa.Column('last_name', sa.String(length=50), nullable=False),
    sa.Column('email', sa.String(length=255), nullable=False),
    sa.Column('hashed_password', sa.String(length=255), nullable=False),
    sa.Column('phone_number', sa.String(), nullable=False),
    sa.Column('reward_point', sa.Integer(), nullable=True),
    sa.Column('created_at', sa.DateTime(), nullable=True),
    sa.Column('updated_at', sa.DateTime(), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('email')
    )
    if environment == "production":
        op.execute(f"ALTER TABLE users SET SCHEMA {SCHEMA};")
    op.create_table('address',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('user_id', sa.Integer(), nullable=False),
    sa.Column('address_type', sa.String(), nullable=False),
    sa.Column('street_address', sa.String(), nullable=False),
    sa.Column('suite_apt', sa.String(), nullable=True),
    sa.Column('city', sa.String(), nullable=False),
    sa.Column('state', sa.String(), nullable=False),
    sa.Column('zipcode', sa.String(), nullable=False),
    sa.Column('address_nickname', sa.String(length=50), nullable=True),
    sa.Column('deliver_instruction', sa.String(length=70), nullable=True),
    sa.ForeignKeyConstraint(['user_id'], ['users.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    if environment == "production":
        __table_args__ = {'schema': SCHEMA}
    op.create_table('orders',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.Column('created_at', sa.DateTime(), nullable=True),
    sa.Column('updatedAt', sa.DateTime(), nullable=True),
    sa.ForeignKeyConstraint(['user_id'], ['users.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    if environment == "production":
        __table_args__ = {'schema': SCHEMA}
    op.create_table('pies',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('quantity', sa.Integer(), nullable=False),
    sa.Column('order_id', sa.Integer(), nullable=True),
    sa.Column('menu_item', sa.Boolean(), nullable=True),
    sa.Column('name', sa.String(length=20), nullable=True),
    sa.Column('price', sa.Float(), nullable=False),
    sa.Column('bake', sa.String(), nullable=False),
    sa.Column('seasoning', sa.Boolean(), nullable=True),
    sa.Column('cut', sa.String(), nullable=False),
    sa.Column('size', sa.String(), nullable=False),
    sa.Column('style', sa.String(), nullable=False),
    sa.Column('cheese', sa.Integer(), nullable=True),
    sa.Column('robust_inspired_tomato_sauce', sa.Integer(), nullable=True),
    sa.Column('hearty_marinara_sauce', sa.Integer(), nullable=True),
    sa.Column('honey_bbq_sauce', sa.Integer(), nullable=True),
    sa.Column('garlic_parmesan_sauce', sa.Integer(), nullable=True),
    sa.Column('alfredo_sauce', sa.Integer(), nullable=True),
    sa.Column('ranch', sa.Integer(), nullable=True),
    sa.Column('ham', sa.Integer(), nullable=True),
    sa.Column('italian_sausage', sa.Integer(), nullable=True),
    sa.Column('beef', sa.Integer(), nullable=True),
    sa.Column('premium_chicken', sa.Integer(), nullable=True),
    sa.Column('bacon', sa.Integer(), nullable=True),
    sa.Column('salami', sa.Integer(), nullable=True),
    sa.Column('philly_steak', sa.Integer(), nullable=True),
    sa.Column('pepperoni', sa.Integer(), nullable=True),
    sa.Column('hot_buffalo_sauce', sa.Integer(), nullable=True),
    sa.Column('jalapeno_pepper', sa.Integer(), nullable=True),
    sa.Column('onion', sa.Integer(), nullable=True),
    sa.Column('banana_pepper', sa.Integer(), nullable=True),
    sa.Column('diced_tomato', sa.Integer(), nullable=True),
    sa.Column('black_olive', sa.Integer(), nullable=True),
    sa.Column('mushroom', sa.Integer(), nullable=True),
    sa.Column('pineapple', sa.Integer(), nullable=True),
    sa.Column('cheddar_cheese', sa.Integer(), nullable=True),
    sa.Column('green_pepper', sa.Integer(), nullable=True),
    sa.Column('spinach', sa.Integer(), nullable=True),
    sa.Column('roasted_red_pepper', sa.Integer(), nullable=True),
    sa.Column('feta_cheese', sa.Integer(), nullable=True),
    sa.Column('shredded_parmesan_asiago', sa.Integer(), nullable=True),
    sa.Column('american_cheese', sa.Integer(), nullable=True),
    sa.Column('shredded_provolone_cheese', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['order_id'], ['orders.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    if environment == "production":
        __table_args__ = {'schema': SCHEMA}
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('pies')
    op.drop_table('orders')
    op.drop_table('address')
    op.drop_table('users')
    # ### end Alembic commands ###