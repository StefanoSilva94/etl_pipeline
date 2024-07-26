from pydantic import BaseModel
from datetime import date


class PlayerStats(BaseModel):
    player: str
    position: str
    age: int
    minutes: int
    goals: int
    assists: int
    pens_made: int
    pens_att: int
    shots: int
    shots_on_target: int
    cards_yellow: int
    cards_red: int
    touches: int
    tackles: int
    interceptions: int
    blocks: int
    xg: float
    npxg: float
    xg_assist: float
    sca: float
    gca: float
    passes: int
    passes_pct: float
    progressive_passes: int
    carries: int
    progressive_carries: int
    take_ons: int
    take_ons_won: int
    team: str
    opponent: str
    home_away: str
    date: date
    competition: str
    goal_involvements: int
    xg_involvements: int
