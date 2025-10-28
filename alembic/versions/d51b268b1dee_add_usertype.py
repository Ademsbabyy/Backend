"""add usertype

Revision ID: d51b268b1dee
Revises: 
Create Date: 2025-10-27 11:38:50.175047

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'd51b268b1dee'
down_revision: Union[str, Sequence[str], None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None

def upgrade() -> None:
    """Upgrade schema."""
    op.execute("""
        ALTER TABLE users
        ADD COLUMN gender varchar(100)
""")
    pass
def downgrade() -> None:
    """Downgrade schema."""
    op.execute("""
        ALTER TABLE users
        DROP COLUMN gender
""")
    pass