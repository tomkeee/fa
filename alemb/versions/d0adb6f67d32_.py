from alembic import op
import sqlalchemy as sa

revision = 'd0adb6f67d32'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    op.create_table('data',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('data', sa.LargeBinary(length=128), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )

def downgrade():
    op.drop_table('data')
