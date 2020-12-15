"""empty message

Revision ID: 400fe7229ba3
Revises: c3000867dcd5
Create Date: 2020-12-15 20:57:44.441724

"""
from alembic import op
import sqlalchemy as sa
from feather_simple_api.extensions.flask_sqlalchemy.guid_type import GUID

# revision identifiers, used by Alembic.
revision = "400fe7229ba3"
down_revision = "c3000867dcd5"
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table(
        "questionnaires",
        sa.Column(
            "id", GUID(), server_default=sa.text("gen_random_uuid()"), nullable=False
        ),
        sa.Column("user", GUID(), nullable=False),
        sa.Column("email", sa.String(length=120), nullable=False),
        sa.Column("firstname", sa.String(length=120), nullable=True),
        sa.Column("address", sa.String(length=255), nullable=True),
        sa.Column("occupation", sa.String(length=255), nullable=True),
        sa.Column("has_child", sa.Boolean(), nullable=True),
        sa.Column("child_num", sa.Integer(), nullable=True),
        sa.Column("created", sa.DateTime(), nullable=True),
        sa.ForeignKeyConstraint(
            ["user"],
            ["users.id"],
        ),
        sa.PrimaryKeyConstraint("id"),
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table("questionnaires")
    # ### end Alembic commands ###