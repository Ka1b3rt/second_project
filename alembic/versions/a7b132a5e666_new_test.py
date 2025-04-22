"""new_test

Revision ID: a7b132a5e666
Revises: 7f4d2fe219f6
Create Date: 2025-04-10 14:04:38.747270

"""

from typing import Sequence, Union

# revision identifiers, used by Alembic.
revision: str = "a7b132a5e666"
down_revision: Union[str, None] = "7f4d2fe219f6"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    pass


def downgrade() -> None:
    """Downgrade schema."""
    pass
