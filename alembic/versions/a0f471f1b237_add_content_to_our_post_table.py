"""add content to our post table

Revision ID: a0f471f1b237
Revises: e4a8f070eca1
Create Date: 2023-09-07 17:31:10.477477

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'a0f471f1b237'
down_revision: Union[str, None] = 'e4a8f070eca1'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.add_column('posts', sa.Column('content', sa.String(), nullable=False))
    pass


def downgrade() -> None:
    op.drop_column('posts', 'content')
    pass

