"""Tables

Revision ID: a157a3eda315
Revises: 3b4abea5eaf6
Create Date: 2023-09-08 14:38:51.431044

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'a157a3eda315'
down_revision: Union[str, None] = '3b4abea5eaf6'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('relationships',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('type_of_relationship', sa.String(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_relationships_type_of_relationship'), 'relationships', ['type_of_relationship'], unique=False)
    op.create_table('users',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('first_name', sa.String(), nullable=True),
    sa.Column('last_name', sa.String(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('people',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('first_name', sa.String(), nullable=True),
    sa.Column('last_name', sa.String(), nullable=True),
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['user_id'], ['users.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('connections',
    sa.Column('individual1_id', sa.Integer(), nullable=False),
    sa.Column('individual2_id', sa.Integer(), nullable=False),
    sa.Column('relationship_id', sa.Integer(), nullable=False),
    sa.Column('users_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['individual1_id'], ['people.id'], ),
    sa.ForeignKeyConstraint(['individual2_id'], ['people.id'], ),
    sa.ForeignKeyConstraint(['relationship_id'], ['relationships.id'], ),
    sa.ForeignKeyConstraint(['users_id'], ['users.id'], ),
    sa.PrimaryKeyConstraint('relationship_id', 'users_id')
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('connections')
    op.drop_table('people')
    op.drop_table('users')
    op.drop_index(op.f('ix_relationships_type_of_relationship'), table_name='relationships')
    op.drop_table('relationships')
    # ### end Alembic commands ###
