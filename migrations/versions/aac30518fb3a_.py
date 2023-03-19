"""empty message

Revision ID: aac30518fb3a
Revises: 777504633289
Create Date: 2023-03-18 20:34:56.278673

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'aac30518fb3a'
down_revision = '777504633289'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('Favorites',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('sims_name', sa.String(length=80), nullable=False),
    sa.Column('buy_url', sa.String(length=2000), nullable=False),
    sa.Column('sims_pic_url', sa.String(length=2000), nullable=False),
    sa.Column('price', sa.Float(), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('id')
    )
    op.drop_table('fav_room')
    op.drop_table('fav_object')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('fav_object',
    sa.Column('object_id', sa.INTEGER(), autoincrement=False, nullable=False),
    sa.Column('user_id', sa.INTEGER(), autoincrement=False, nullable=False),
    sa.ForeignKeyConstraint(['object_id'], ['object.id'], name='fav_object_object_id_fkey'),
    sa.ForeignKeyConstraint(['user_id'], ['user.id'], name='fav_object_user_id_fkey'),
    sa.PrimaryKeyConstraint('object_id', 'user_id', name='fav_object_pkey')
    )
    op.create_table('fav_room',
    sa.Column('room_id', sa.INTEGER(), autoincrement=False, nullable=False),
    sa.Column('user_id', sa.INTEGER(), autoincrement=False, nullable=False),
    sa.ForeignKeyConstraint(['room_id'], ['room.id'], name='fav_room_room_id_fkey'),
    sa.ForeignKeyConstraint(['user_id'], ['user.id'], name='fav_room_user_id_fkey'),
    sa.PrimaryKeyConstraint('room_id', 'user_id', name='fav_room_pkey')
    )
    op.drop_table('Favorites')
    # ### end Alembic commands ###
