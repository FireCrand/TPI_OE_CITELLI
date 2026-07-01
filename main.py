# Trabajo Práctico Integrador

#Pesudo-código
print("Hola yo soy Chaty, tu asistente virtual!")
print("Elige una opción:\n1. Solicitar Semana de Vacaciones.\n2. Partes por enfermedad.\n3. Hablar con un humano.")

input(mensaje)

if mensaje == "1":
    enviar("Has elegido información de productos. ¿Quieres ver catálogo o precios?")
elif mensaje == "2":
    enviar("Soporte técnico: ¿Tu problema es con hardware o software?")
else:
    enviar("Por favor, elige una opción válida: 1 o 2")
