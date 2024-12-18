"""empty message

Revision ID: c0f6aa0c1a61
Revises: 
Create Date: 2024-12-05 05:45:55.494965

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'c0f6aa0c1a61'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('biography',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('image_url', sa.String(length=500), nullable=True),
    sa.Column('name', sa.String(length=500), nullable=False),
    sa.Column('price', sa.Float(), nullable=False),
    sa.Column('stocks', sa.Integer(), nullable=False),
    sa.Column('author', sa.String(length=50), nullable=False),
    sa.Column('quantity', sa.Integer(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('novel',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('image_url', sa.String(length=500), nullable=True),
    sa.Column('name', sa.String(length=500), nullable=False),
    sa.Column('price', sa.Float(), nullable=False),
    sa.Column('stocks', sa.Integer(), nullable=False),
    sa.Column('author', sa.String(length=50), nullable=False),
    sa.Column('quantity', sa.Integer(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('science',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('image_url', sa.String(length=500), nullable=True),
    sa.Column('name', sa.String(length=500), nullable=False),
    sa.Column('price', sa.Float(), nullable=False),
    sa.Column('stocks', sa.Integer(), nullable=False),
    sa.Column('author', sa.String(length=50), nullable=False),
    sa.Column('quantity', sa.Integer(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('textbook',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('image_url', sa.String(length=500), nullable=True),
    sa.Column('name', sa.String(length=500), nullable=False),
    sa.Column('price', sa.Float(), nullable=False),
    sa.Column('stocks', sa.Integer(), nullable=False),
    sa.Column('author', sa.String(length=50), nullable=False),
    sa.Column('quantity', sa.Integer(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('user',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('username', sa.String(length=500), nullable=False),
    sa.Column('password', sa.String(length=500), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('username')
    )
    op.create_table('basket',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('user_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['user_id'], ['user.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('basket_biography',
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.Column('product_id', sa.Integer(), nullable=False),
    sa.Column('product_name', sa.String(length=50), nullable=False),
    sa.Column('price', sa.Float(), nullable=False),
    sa.Column('quantity', sa.Integer(), nullable=False),
    sa.Column('image_url', sa.String(length=500), nullable=True),
    sa.Column('stocks', sa.Integer(), nullable=True),
    sa.Column('author', sa.String(length=50), nullable=False),
    sa.ForeignKeyConstraint(['product_id'], ['biography.id'], ),
    sa.ForeignKeyConstraint(['user_id'], ['user.id'], ondelete='CASCADE')
    )
    op.create_table('basket_novel',
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.Column('product_id', sa.Integer(), nullable=False),
    sa.Column('product_name', sa.String(length=50), nullable=False),
    sa.Column('price', sa.Float(), nullable=False),
    sa.Column('quantity', sa.Integer(), nullable=False),
    sa.Column('image_url', sa.String(length=500), nullable=True),
    sa.Column('stocks', sa.Integer(), nullable=True),
    sa.Column('author', sa.String(length=50), nullable=False),
    sa.ForeignKeyConstraint(['product_id'], ['novel.id'], ),
    sa.ForeignKeyConstraint(['user_id'], ['user.id'], ondelete='CASCADE')
    )
    op.create_table('basket_science',
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.Column('product_id', sa.Integer(), nullable=False),
    sa.Column('product_name', sa.String(length=50), nullable=False),
    sa.Column('price', sa.Float(), nullable=False),
    sa.Column('quantity', sa.Integer(), nullable=False),
    sa.Column('image_url', sa.String(length=500), nullable=True),
    sa.Column('stocks', sa.Integer(), nullable=True),
    sa.Column('author', sa.String(length=50), nullable=False),
    sa.ForeignKeyConstraint(['product_id'], ['science.id'], ),
    sa.ForeignKeyConstraint(['user_id'], ['user.id'], ondelete='CASCADE')
    )
    op.create_table('basket_textbook',
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.Column('product_id', sa.Integer(), nullable=False),
    sa.Column('product_name', sa.String(length=50), nullable=False),
    sa.Column('price', sa.Float(), nullable=False),
    sa.Column('quantity', sa.Integer(), nullable=False),
    sa.Column('image_url', sa.String(length=500), nullable=True),
    sa.Column('stocks', sa.Integer(), nullable=True),
    sa.Column('author', sa.String(length=50), nullable=False),
    sa.ForeignKeyConstraint(['product_id'], ['textbook.id'], ),
    sa.ForeignKeyConstraint(['user_id'], ['user.id'], ondelete='CASCADE')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('basket_textbook')
    op.drop_table('basket_science')
    op.drop_table('basket_novel')
    op.drop_table('basket_biography')
    op.drop_table('basket')
    op.drop_table('user')
    op.drop_table('textbook')
    op.drop_table('science')
    op.drop_table('novel')
    op.drop_table('biography')
    # ### end Alembic commands ###
