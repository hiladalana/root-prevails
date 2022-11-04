class TokenParser:
    def __init__(self, config_file=None):
        self.tokens = {}
        self.config_file = config_file

    def parser(self, _list):
        self.tokens = dict(
            (c + 1, t)
            for c, (_, t) in enumerate(
                filter(lambda n: n[0].startswith("DATA_ENTRY"), sorted(_list))
            )
        )
        return self.tokens
