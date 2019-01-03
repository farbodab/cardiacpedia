"""empty message

Revision ID: 645291d3c88d
Revises: 
Create Date: 2019-01-03 03:34:39.426667

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '645291d3c88d'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('crtd',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('manufacturer', sa.String(length=255, collation='NOCASE'), nullable=False),
    sa.Column('model_number', sa.String(length=255, collation='NOCASE'), nullable=True),
    sa.Column('name', sa.String(length=255, collation='NOCASE'), nullable=True),
    sa.Column('nbg_code', sa.String(length=255, collation='NOCASE'), nullable=True),
    sa.Column('x_ray', sa.String(length=255, collation='NOCASE'), nullable=True),
    sa.Column('serial', sa.String(length=255, collation='NOCASE'), nullable=True),
    sa.Column('ra', sa.String(length=255, collation='NOCASE'), nullable=True),
    sa.Column('rv', sa.String(length=255, collation='NOCASE'), nullable=True),
    sa.Column('lv', sa.String(length=255, collation='NOCASE'), nullable=True),
    sa.Column('hv', sa.String(length=255, collation='NOCASE'), nullable=True),
    sa.Column('detach', sa.String(length=255, collation='NOCASE'), nullable=True),
    sa.Column('wave', sa.String(length=255, collation='NOCASE'), nullable=True),
    sa.Column('replacement', sa.String(length=255, collation='NOCASE'), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
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
    op.create_table('hv',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('manufacturer', sa.String(length=255, collation='NOCASE'), nullable=False),
    sa.Column('model_number', sa.String(length=255, collation='NOCASE'), nullable=True),
    sa.Column('name', sa.String(length=255, collation='NOCASE'), nullable=True),
    sa.Column('serial', sa.String(length=255, collation='NOCASE'), nullable=True),
    sa.Column('sense', sa.String(length=255, collation='NOCASE'), nullable=True),
    sa.Column('high', sa.String(length=255, collation='NOCASE'), nullable=True),
    sa.Column('sensing', sa.String(length=255, collation='NOCASE'), nullable=True),
    sa.Column('lead', sa.String(length=255, collation='NOCASE'), nullable=True),
    sa.Column('placement', sa.String(length=255, collation='NOCASE'), nullable=True),
    sa.Column('fixation', sa.String(length=255, collation='NOCASE'), nullable=True),
    sa.Column('insulation', sa.String(length=255, collation='NOCASE'), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('icd',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('manufacturer', sa.String(length=255, collation='NOCASE'), nullable=False),
    sa.Column('model_number', sa.String(length=255, collation='NOCASE'), nullable=True),
    sa.Column('name', sa.String(length=255, collation='NOCASE'), nullable=True),
    sa.Column('nbg_code', sa.String(length=255, collation='NOCASE'), nullable=True),
    sa.Column('x_ray', sa.String(length=255, collation='NOCASE'), nullable=True),
    sa.Column('serial', sa.String(length=255, collation='NOCASE'), nullable=True),
    sa.Column('ra', sa.String(length=255, collation='NOCASE'), nullable=True),
    sa.Column('rv', sa.String(length=255, collation='NOCASE'), nullable=True),
    sa.Column('hv', sa.String(length=255, collation='NOCASE'), nullable=True),
    sa.Column('detach', sa.String(length=255, collation='NOCASE'), nullable=True),
    sa.Column('wave', sa.String(length=255, collation='NOCASE'), nullable=True),
    sa.Column('replacement', sa.String(length=255, collation='NOCASE'), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('ipg',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('manufacturer', sa.String(length=255, collation='NOCASE'), nullable=False),
    sa.Column('model_number', sa.String(length=255, collation='NOCASE'), nullable=True),
    sa.Column('name', sa.String(length=255, collation='NOCASE'), nullable=True),
    sa.Column('nbg_code', sa.String(length=255, collation='NOCASE'), nullable=True),
    sa.Column('x_ray', sa.String(length=255, collation='NOCASE'), nullable=True),
    sa.Column('ra', sa.String(length=255, collation='NOCASE'), nullable=True),
    sa.Column('rv', sa.String(length=255, collation='NOCASE'), nullable=True),
    sa.Column('detach', sa.String(length=255, collation='NOCASE'), nullable=True),
    sa.Column('n_bos', sa.String(length=255, collation='NOCASE'), nullable=True),
    sa.Column('n_rrt', sa.String(length=255, collation='NOCASE'), nullable=True),
    sa.Column('m_bos', sa.String(length=255, collation='NOCASE'), nullable=True),
    sa.Column('m_rrt', sa.String(length=255, collation='NOCASE'), nullable=True),
    sa.Column('rrt_behaviour', sa.String(length=255, collation='NOCASE'), nullable=True),
    sa.Column('rrt_longevity', sa.String(length=255, collation='NOCASE'), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('lv',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('manufacturer', sa.String(length=255, collation='NOCASE'), nullable=False),
    sa.Column('model_number', sa.String(length=255, collation='NOCASE'), nullable=True),
    sa.Column('name', sa.String(length=255, collation='NOCASE'), nullable=True),
    sa.Column('serial', sa.String(length=255, collation='NOCASE'), nullable=True),
    sa.Column('sense', sa.String(length=255, collation='NOCASE'), nullable=True),
    sa.Column('polarity', sa.String(length=255, collation='NOCASE'), nullable=True),
    sa.Column('fixation', sa.String(length=255, collation='NOCASE'), nullable=True),
    sa.Column('placement', sa.String(length=255, collation='NOCASE'), nullable=True),
    sa.Column('insulation', sa.String(length=255, collation='NOCASE'), nullable=True),
    sa.Column('location', sa.String(length=255, collation='NOCASE'), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('roles',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=50), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('name')
    )
    op.create_table('users',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('is_active', sa.Boolean(), server_default='1', nullable=False),
    sa.Column('email', sa.String(length=255, collation='NOCASE'), nullable=False),
    sa.Column('email_confirmed_at', sa.DateTime(), nullable=True),
    sa.Column('password', sa.String(length=255), server_default='', nullable=False),
    sa.Column('first_name', sa.String(length=100, collation='NOCASE'), server_default='', nullable=False),
    sa.Column('last_name', sa.String(length=100, collation='NOCASE'), server_default='', nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('email')
    )
    op.create_table('user_roles',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.Column('role_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['role_id'], ['roles.id'], ondelete='CASCADE'),
    sa.ForeignKeyConstraint(['user_id'], ['users.id'], ondelete='CASCADE'),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('user_roles')
    op.drop_table('users')
    op.drop_table('roles')
    op.drop_table('lv')
    op.drop_table('ipg')
    op.drop_table('icd')
    op.drop_table('hv')
    op.drop_table('crtp')
    op.drop_table('crtd')
    # ### end Alembic commands ###