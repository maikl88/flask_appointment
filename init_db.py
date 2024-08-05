from app import create_app, db
from app.models import User, Role

app = create_app()

with app.app_context():
    # Создание всех таблиц
    db.create_all()

    # Проверка, если роли уже существуют
    if not Role.query.filter_by(name='admin').first():
        admin_role = Role(name='admin')
        db.session.add(admin_role)

    if not Role.query.filter_by(name='user').first():
        user_role = Role(name='user')
        db.session.add(user_role)

    db.session.commit()

    # Проверка, если пользователь администратор уже существует
    if not User.query.filter_by(username='admin').first():
        admin_user = User(username='admin', role=admin_role)
        admin_user.set_password('admin')  # Использование метода set_password для установки пароля
        db.session.add(admin_user)
        db.session.commit()
