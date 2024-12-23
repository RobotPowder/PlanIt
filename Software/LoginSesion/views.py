from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import login
from django.contrib.auth.hashers import make_password

def signup(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password1 = request.POST.get('password1')
        password2 = request.POST.get('password2')

        # Validar que las contraseñas coincidan
        if password1 != password2:
            return render(request, 'signup.html', {
                'error': 'Las contraseñas no coinciden.',
            })

        # Validar si el correo ya existe
        if User.objects.filter(email=email).exists():
            return render(request, 'signup.html', {
                'error': 'Este correo ya está registrado.',
            })

        # Crear el usuario si todo está bien
        user = User.objects.create(
            username=username,
            email=email,
            password=make_password(password1)  # Guardar la contraseña encriptada
        )
        login(request, user)  # Inicia sesión automáticamente
        return redirect('inicio')  # REDIRIGIR A LA PÁGINA PRINCIP

    return render(request, 'signup.html')
