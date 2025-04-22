"""new_test

Revision ID: a8a0a08c0afc
Revises: a7b132a5e666
Create Date: 2025-04-10 14:05:22.880468

"""

from typing import Sequence, Union

# revision identifiers, used by Alembic.
revision: str = "a8a0a08c0afc"
down_revision: Union[str, None] = "a7b132a5e666"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    pass


def downgrade() -> None:
    """Downgrade schema."""
    pass
