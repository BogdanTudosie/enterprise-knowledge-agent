"""initialize migrations

Revision ID: e0ec2fcc0503
Revises: 
Create Date: 2026-09-11 17:29:17.510387

"""
from collections.abc import Sequence

# revision identifiers, used by Alembic.
revision: str = 'e0ec2fcc0503'
down_revision: str | Sequence[str] | None = None
branch_labels: str | Sequence[str] | None = None
depends_on: str | Sequence[str] | None = None


def upgrade() -> None:
    """Upgrade schema."""
    pass


def downgrade() -> None:
    """Downgrade schema."""
    pass
