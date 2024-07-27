"""Renaming sca and gca columns

Revision ID: e905b6e77770
Revises: 83540b6c4efc
Create Date: 2024-07-27 09:40:56.166437

"""
from typing import Sequence, Union

from alembic import op


# revision identifiers, used by Alembic.
revision: str = 'e905b6e77770'
down_revision: Union[str, None] = '83540b6c4efc'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    with op.batch_alter_table('player_stats') as batch_op:
        batch_op.alter_column('sca', new_column_name='shot_creating_actions')
        batch_op.alter_column('gca', new_column_name='goal_creating_actions')


def downgrade() -> None:
    with op.batch_alter_table('player_stats') as batch_op:
        batch_op.alter_column('shot_creating_actions', new_column_name='sca')
        batch_op.alter_column('goal_creating_actions', new_column_name='gca')
