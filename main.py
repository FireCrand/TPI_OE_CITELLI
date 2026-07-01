# Trabajo Práctico Integrador

#Pesudo-código
print("Hola yo soy Chaty, tu asistente virtual!")
print("Elige una opción:\n1. Solicitar Semana de Vacaciones.\n2. Partes por enfermedad.\n3. Hablar con un humano.")

input(mensaje)

if mensaje == "1":
    enviar("Has elegido Solicitar semana de vacaciones ¿Qué semana deseas solicitar? (ingresa día/mes/año del inicio de la semana)")
elif mensaje == "2":
    enviar("¿Tienes la imagen o documento médico a mano?")
elif mensaje == "3":
    enviar("Un representante se comunicará contigo a la brevedad")
else:
    enviar("Por favor, elige una opción válida: 1, 2 ó 3")
