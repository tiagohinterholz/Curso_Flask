"""empty message

Revision ID: ddbaa193402c
Revises: 64ef2447061f
Create Date: 2025-02-05 17:06:36.968249

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'ddbaa193402c'
down_revision = '64ef2447061f'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('professor_formacao',
    sa.Column('professor_id', sa.Integer(), nullable=False),
    sa.Column('formacao_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['formacao_id'], ['formacao.id'], ),
    sa.ForeignKeyConstraint(['professor_id'], ['professor.id'], ),
    sa.PrimaryKeyConstraint('professor_id', 'formacao_id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('professor_formacao')
    # ### end Alembic commands ###
