from app import create_app, db

app = create_app()

with app.app_context():
    meta = db.metadata
    for table in reversed(meta.sorted_tables):
        print(f'Clearing table {table}')
        db.session.execute(table.delete())
    db.session.commit()
    print("Database cleared!")
