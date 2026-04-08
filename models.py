from pydantic import BaseModel
from typing import List, Optional, Dict

class Action(BaseModel):
    command: str  # e.g., "drop_duplicates", "fill_na", "submit"

class Observation(BaseModel):
    data_preview: str
    row_count: int
    is_dirty: bool

class Reward(BaseModel):
    value: float
    reason: str
