import sqlalchemy

def upgrade(migrate_engine):
    meta = sqlalchemy.MetaData()
    meta.bind = migrate_engine

    image_properties = sqlalchemy.Table('image_properties', meta, autoload=True)
    required = sqlalchemy.Column('required', sqlalchemy.Boolean, default=True)

    image_properties.create_column(required)

def downgrade(migrate_engine):
    meta = sqlalchemy.MetaData()
    meta.bind = migrate_engine

    image_properties = sqlalchemy.Table('image_properties', meta, autoload=True)
    image_properties.columns['required'].drop()

