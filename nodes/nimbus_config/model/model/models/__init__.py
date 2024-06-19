from model import db

class DataModel(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    @staticmethod
    def init_model(kwargs):
        setattr(DataModel, "__tablename__", kwargs["tablename"])
        for k, v in kwargs.items():
            if k != "columns":
                setattr(DataModel, k, v)
            else:
                for col, cfg in v.items():
                    setattr(
                            DataModel, col, db.Column(
                            getattr(db, cfg["type"]),
                            index=cfg.get("index", False),
                            primary_key=cfg.get("primary_key", False),
                            unique=cfg.get("unique", False),
                            nullable=cfg.get("nullable", False),
                            default=cfg.get("default", None)
                        )
                    )
        return DataModel
    def __init__(self, **kwargs):
        for k, v in kwargs.items():
            setattr(self, k, v)
    def as_dict(self):
        return {k: v for k, v in self.__dict__.items() if k[0] != "_"}