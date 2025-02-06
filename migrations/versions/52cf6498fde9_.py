"""empty message

Revision ID: 52cf6498fde9
Revises: a65e59b962be
Create Date: 2025-02-03 17:29:30.229757

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '52cf6498fde9'
down_revision = 'a65e59b962be'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('curso', schema=None) as batch_op:
        batch_op.add_column(sa.Column('formacao_id', sa.Integer(), nullable=True))
        batch_op.create_foreign_key(None, 'formacao', ['formacao_id'], ['id'])

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('curso', schema=None) as batch_op:
        batch_op.drop_constraint(None, type_='foreignkey')
        batch_op.drop_column('formacao_id')

    # ### end Alembic commands ###
