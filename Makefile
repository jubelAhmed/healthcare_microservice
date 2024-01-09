main:
	cd healthcare && python3 manage.py runserver 8001

appointment:
	cd appointment_service && python3 manage.py runserver 8003

auth:
	cd auth_service && python3 manage.py runserver 8002

prescription:
	cd prescription_service && python3 manage.py runserver 8005

payment_service:
	cd prescription_service && python3 manage.py runserver 8004