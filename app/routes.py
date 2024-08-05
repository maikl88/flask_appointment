from flask import Blueprint, render_template, redirect, url_for, request, flash
from flask_login import login_user, logout_user, login_required, current_user
from app.forms import BookingForm
from app.models import Appointment, Service, User, db
from datetime import datetime

bp = Blueprint('routes', __name__)

@bp.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        user = User.query.filter_by(username=username).first()
        if user and user.check_password(password):  # Используем метод проверки пароля
            login_user(user)
            return redirect(url_for('routes.index'))
        flash('Invalid username or password')
    return render_template('login.html')

@bp.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('routes.login'))

@bp.route('/', methods=['GET', 'POST'])
def index():
    form = BookingForm()
    if form.validate_on_submit():
        appointment_date_str = form.date.data
        appointment_time_str = form.time.data

        # Преобразование строковых значений в объекты date и time
        appointment_date = datetime.strptime(appointment_date_str, '%Y-%m-%d').date()
        appointment_time = datetime.strptime(appointment_time_str, '%H:%M').time()

        existing_appointment = Appointment.query.filter_by(date=appointment_date, time=appointment_time).first()
        
        if existing_appointment:
            flash('The selected time slot is already booked. Please choose another time.', 'danger')
        else:
            new_appointment = Appointment(
                client_name=form.client_name.data,
                date=appointment_date,
                time=appointment_time
            )
            services = Service.query.filter(Service.id.in_(form.service.data)).all()
            new_appointment.services = services
            db.session.add(new_appointment)
            db.session.commit()
            flash('Your appointment has been booked!', 'success')
            return redirect(url_for('routes.index'))
    
    return render_template('index.html', form=form)

@bp.route('/appointments')
@login_required
def appointments():
    if current_user.role.name != 'admin':
        flash('You do not have permission to view this page.')
        return redirect(url_for('routes.index'))
    
    appointments = Appointment.query.all()  # Извлекаем все назначения из базы данных
    return render_template('appointments.html', appointments=appointments)

@bp.route('/get_booked_slots/<date>', methods=['GET'])
def get_booked_slots(date):
    booked_slots = Appointment.query.filter_by(date=date).all()
    booked_times = [appointment.time.strftime('%H:%M') for appointment in booked_slots]
    return {'booked_times': booked_times}