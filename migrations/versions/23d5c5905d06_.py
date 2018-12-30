"""empty message

Revision ID: 23d5c5905d06
Revises: 07129a2d8d68
Create Date: 2018-12-30 15:09:16.108483

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '23d5c5905d06'
down_revision = '07129a2d8d68'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('crtp',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('manufacturer', sa.String(length=255, collation='NOCASE'), nullable=False),
    sa.Column('model_number', sa.String(length=255, collation='NOCASE'), nullable=True),
    sa.Column('name', sa.String(length=255, collation='NOCASE'), nullable=True),
    sa.Column('nbg_code', sa.String(length=255, collation='NOCASE'), nullable=True),
    sa.Column('x_ray', sa.String(length=255, collation='NOCASE'), nullable=True),
    sa.Column('ra', sa.String(length=255, collation='NOCASE'), nullable=True),
    sa.Column('la', sa.String(length=255, collation='NOCASE'), nullable=True),
    sa.Column('rv', sa.String(length=255, collation='NOCASE'), nullable=True),
    sa.Column('lv', sa.String(length=255, collation='NOCASE'), nullable=True),
    sa.Column('detach', sa.String(length=255, collation='NOCASE'), nullable=True),
    sa.Column('n_bol', sa.String(length=255, collation='NOCASE'), nullable=True),
    sa.Column('n_eri', sa.String(length=255, collation='NOCASE'), nullable=True),
    sa.Column('m_bol', sa.String(length=255, collation='NOCASE'), nullable=True),
    sa.Column('m_eri', sa.String(length=255, collation='NOCASE'), nullable=True),
    sa.Column('eri_behaviour', sa.String(length=255, collation='NOCASE'), nullable=True),
    sa.Column('longevity', sa.String(length=255, collation='NOCASE'), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('crtp')
    # ### end Alembic commands ###
