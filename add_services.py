from app import create_app, db
from app.models import Service

app = create_app()

with app.app_context():
    # Создаем услуги
    service1 = Service(name="Service 1", price=100.0, duration=60)
    service2 = Service(name="Service 2", price=150.0, duration=90)
    service3 = Service(name="Service 3", price=200.0, duration=120)

    # Добавляем услуги в сессию
    db.session.add(service1)
    db.session.add(service2)
    db.session.add(service3)

    # Сохраняем изменения
    db.session.commit()

    print("Services added successfully!")
