# type: ignore
"""empty message

Revision ID: 3f5b2d199d38
Revises: 13ac4bb3abd2
Create Date: 2021-11-23 15:10:47.734122

"""
import sqlalchemy as sa

from alembic import op

# revision identifiers, used by Alembic.
revision = "3f5b2d199d38"
down_revision = "13ac4bb3abd2"
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column(
        "job", sa.Column("mode", sa.String(length=30), nullable=True)
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column("job", "mode")
    # ### end Alembic commands ###
