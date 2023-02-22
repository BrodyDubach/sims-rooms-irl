"""empty message

Revision ID: babf6cfdd9a6
Revises: 
Create Date: 2023-02-21 21:05:12.807791

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'babf6cfdd9a6'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('meta',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=80), nullable=False),
    sa.Column('style', sa.String(length=80), nullable=False),
    sa.Column('room_type', sa.String(length=80), nullable=False),
    sa.Column('object_type', sa.String(length=80), nullable=False),
    sa.Column('age_group', sa.String(length=80), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('object',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('sims_name', sa.String(length=80), nullable=False),
    sa.Column('name', sa.String(length=80), nullable=False),
    sa.Column('buy_url', sa.String(length=500), nullable=False),
    sa.Column('sims_pic_url', sa.String(length=500), nullable=False),
    sa.Column('real_pic_url', sa.String(length=500), nullable=False),
    sa.Column('price', sa.Integer(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('room',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=80), nullable=False),
    sa.Column('pic_url', sa.String(length=500), nullable=False),
    sa.Column('price', sa.Integer(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('user',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('email', sa.String(length=120), nullable=False),
    sa.Column('password', sa.String(length=80), nullable=False),
    sa.Column('is_active', sa.Boolean(), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('email')
    )
    op.create_table('fav_object',
    sa.Column('object_id', sa.Integer(), nullable=False),
    sa.Column('user_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['object_id'], ['object.id'], ),
    sa.ForeignKeyConstraint(['user_id'], ['user.id'], ),
    sa.PrimaryKeyConstraint('object_id', 'user_id')
    )
    op.create_table('fav_room',
    sa.Column('room_id', sa.Integer(), nullable=False),
    sa.Column('user_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['room_id'], ['room.id'], ),
    sa.ForeignKeyConstraint(['user_id'], ['user.id'], ),
    sa.PrimaryKeyConstraint('room_id', 'user_id')
    )
    op.create_table('meta_object',
    sa.Column('object_id', sa.Integer(), nullable=False),
    sa.Column('meta_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['meta_id'], ['meta.id'], ),
    sa.ForeignKeyConstraint(['object_id'], ['object.id'], ),
    sa.PrimaryKeyConstraint('object_id', 'meta_id')
    )
    op.create_table('meta_room',
    sa.Column('meta_id', sa.Integer(), nullable=False),
    sa.Column('room_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['meta_id'], ['meta.id'], ),
    sa.ForeignKeyConstraint(['room_id'], ['room.id'], ),
    sa.PrimaryKeyConstraint('meta_id', 'room_id')
    )
    op.create_table('object_room',
    sa.Column('object_id', sa.Integer(), nullable=False),
    sa.Column('room_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['object_id'], ['object.id'], ),
    sa.ForeignKeyConstraint(['room_id'], ['room.id'], ),
    sa.PrimaryKeyConstraint('object_id', 'room_id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('object_room')
    op.drop_table('meta_room')
    op.drop_table('meta_object')
    op.drop_table('fav_room')
    op.drop_table('fav_object')
    op.drop_table('user')
    op.drop_table('room')
    op.drop_table('object')
    op.drop_table('meta')
    # ### end Alembic commands ###