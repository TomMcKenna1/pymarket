class PriceHistory:
    def __init__(self):
        pass

    @classmethod
    def from_list(
        cls,
        timestamp: list[int],
        high: list[float],
        low: list[float],
        open: list[float],
        close: list[float],
    ) -> "PriceHistory":
        return
