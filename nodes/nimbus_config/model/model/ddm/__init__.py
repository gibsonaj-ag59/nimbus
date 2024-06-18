from sqlalchemy import URL
import os

class DeviceDataManagement():
    def __init__(self, db, app):
        self.db_dialect_driver = os.environ.get("DB_DIALECT_DRIVER", "default")
        self.db_name = os.environ.get("DB_NAME", "default")
        self.db_user = os.environ.get("DB_USER", "default")
        self.db_pass = os.environ.get("DB_PASS", "default")
        self.db_host = os.environ.get("DB_HOST", "default")
        self.db_port = os.environ.get("DB_PORT", "default")
        self.db_uri = self.create_device_uri()
        self.config_device_app(db, app)
        
    def create_device_uri(self):
        db_uri = URL.create(
              self.db_dialect_driver,
              host=self.db_host,
              database=self.db_name,
              username=self.db_user,
              password=self.db_pass,
              port=self.db_port
            )
        return db_uri
    
    def config_device_app(self, db, app):
        app.config.update(SQLALCHEMY_DATABASE_URI=self.create_device_uri())
        db.init_app(app)
    
    @staticmethod
    def create_device_tables(db, app):
        with app.app_context():
            db.create_all()
            db.session.commit()
    
    @staticmethod
    def drop_device_tables(db, app):
        with app.app_context():
            db.drop_all()
            db.session.commit()
    
    @staticmethod
    def insert_test_data(app, db, obj):
        with app.app_context():
            db.session.add(obj)
            db.session.commit()
        