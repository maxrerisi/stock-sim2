from SEED_FILE import SEED_CASH
from get_date import get_date


class Portfolio:
    def __init__(self) -> None:
        self.cash_in = SEED_CASH
        self.init_time = get_date()
        self.current_cash = SEED_CASH
        self.max_cash = -1
        self.holdings = {}
        self.check_max()

    def check_max(self):
        if self.current_cash > self.max_cash["cash"]:
            self.max_cash = {"cash": self.current_cash, "date": get_date()}

    def to_json(self):
        self.check_max()
        return {}
