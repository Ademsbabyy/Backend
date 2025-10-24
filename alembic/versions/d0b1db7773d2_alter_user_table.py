# """alter user table

# Revision ID: d0b1db7773d2
# Revises: 
# Create Date: 2025-10-23 11:18:18.827567

# """
# from typing import Sequence, Union

# from alembic import op
# import sqlalchemy as sa


# # revision identifiers, used by Alembic.
# revision: str = 'd0b1db7773d2'
# down_revision: Union[str, Sequence[str], None] = None
# branch_labels: Union[str, Sequence[str], None] = None
# depends_on: Union[str, Sequence[str], None] = None


# def upgrade() -> None:
#     op.execute("""
#     ALTER TABLE users
#     ADD COLUMN userType varchar(100)

#     """)
#     pass


# def downgrade() -> None:
#     """Downgrade schema."""

#     op.execute("""
#     ALTER TABLE users
#     DROP COLUMN userType

#     """)

#     pass




# #  alembic revision -m "alter user table"










"""alter user table
Revision ID: 771c7a2adace
Revises:
Create Date: 2025-10-23 11:22:28.549330
"""
from typing import Sequence, Union
from alembic import op
import sqlalchemy as sa
# revision identifiers, used by Alembic.
revision: str = '771c7a2adace'
down_revision: Union[str, Sequence[str], None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None
def upgrade() -> None:
    """Upgrade schema."""
    op.execute("""
    ALTER TABLE users
    ADD COLUMN userType varchar(100) DEFAULT 'student'
""")
    pass
def downgrade() -> None:
    """Downgrade schema."""
    op.execute("""
    ALTER TABLE users
    DROP COLUMN userType
""")
    pass