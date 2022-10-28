"""Adds overall_load field (not-negative default = 0) to annotators table

Revision ID: bda0eac5ce64
Revises: d30649e367e0
Create Date: 2021-11-22 15:04:13.771490

"""
import sqlalchemy as sa

from alembic import op

# revision identifiers, used by Alembic.
revision = "bda0eac5ce64"
down_revision = "d30649e367e0"
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column(
        "annotators",
        sa.Column(
            "overall_load",
            sa.INTEGER(),
            server_default="0",
            nullable=False,
        ),  # server_default='0' ensures that it will insert 0 instead of NULLs
    )
    op.create_check_constraint(
        "not_negative_overall_load", "annotators", "overall_load >= 0"
    )  # Add this constraint manually - not autogenerated by alembic
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column("annotators", "overall_load")
    # ### end Alembic commands ###
