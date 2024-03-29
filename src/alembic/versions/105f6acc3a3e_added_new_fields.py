"""Added new fields

Revision ID: 105f6acc3a3e
Revises: fece42ba3db3
Create Date: 2024-03-23 10:54:12.945653

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '105f6acc3a3e'
down_revision: Union[str, None] = 'fece42ba3db3'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('contacts', sa.Column('favorite', sa.Boolean(), nullable=True))
    op.add_column('contacts', sa.Column('created_at', sa.DateTime(), nullable=True))
    op.add_column('contacts', sa.Column('updated_at', sa.DateTime(), nullable=True))
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('contacts', 'updated_at')
    op.drop_column('contacts', 'created_at')
    op.drop_column('contacts', 'favorite')
    # ### end Alembic commands ###
