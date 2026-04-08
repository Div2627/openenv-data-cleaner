import pandas as pd
from models import Action, Observation, Reward

class DataCleaningEnv:
    def __init__(self):
        self.reset()

    def reset(self, task_id="easy"):
        if task_id == "easy":
            self.df = pd.DataFrame({"ID": [1, 1, 2], "Name": ["Alice", "Alice", "Bob"]})
        elif task_id == "medium":
            self.df = pd.DataFrame({"Date": ["2023/01/01", "01-02-2023"], "Val": [10, None]})
        else:
            self.df = pd.DataFrame({"Phone": ["91-123", "123", None], "User": ["A", "B", "C"]})
        return self.state()

    def state(self) -> Observation:
        return Observation(
            data_preview=self.df.to_string(),
            row_count=len(self.df),
            is_dirty=self.df.duplicated().any() or self.df.isnull().any().any()
        )

    def step(self, action: Action):
        if action.command == "drop_duplicates":
            self.df = self.df.drop_duplicates()
        elif action.command == "fill_na":
            self.df = self.df.fillna("Unknown")
            
        reward_val = 1.0 if not self.state().is_dirty else 0.0
        done = (action.command == "submit")
        return self.state(), Reward(value=reward_val, reason="Action executed"), done, {}
