while True:
    try:
        peso = float(input('¿Cuánto pesas? '))
        
        if peso <= 0:
            print('El peso debe ser un número positivo. Intenta de nuevo.')
            continue
        
        break
    except ValueError:
        print('Por favor, introduce un número válido para el peso.')

while True:
    decision = input('¿En kg (k) o en lb (l)? ').lower()
    
    if decision == 'k':
        peso = peso * 2.2046
        print(f'Tu peso en lb es {peso:.2f}')
        break
    elif decision == 'l':
        peso = peso * 0.4536
        print(f'Tu peso en kg es {peso:.2f}')
        break
    else:
        print('No seas terrorista y dame un valor correcto.')