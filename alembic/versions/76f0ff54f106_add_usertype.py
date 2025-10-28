"""add usertype

Revision ID: 76f0ff54f106
Revises: d51b268b1dee
Create Date: 2025-10-27 11:47:57.633252

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '76f0ff54f106'
down_revision: Union[str, Sequence[str], None] = 'd51b268b1dee'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None

def upgrade() -> None:
    """Upgrade schema."""
    op.execute("""
        ALTER TABLE users
        ADD COLUMN userType varchar(100)
""")
    pass
def downgrade() -> None:
    """Downgrade schema."""
    op.execute("""
        ALTER TABLE users
        DROP COLUMN userType
""")
    pass