import os
import requests


def quiz_conectividad():
  print('--- EXAMEN 1: Conectividad y Red ---')
  try:
    response = requests.get('https://httpbin.org/get', timeout=5)
    if response.status_code == 200:
      print(
          f'[ÉXITO] Conexión externa establecida. Código HTTP:'
          f' {response.status_code}'
      )
    else:
      print(f'[ADVERTENCIA] Código de respuesta inesperado: {response.status_code}')
  except Exception as e:
    print(f'[FALLO] Error de red: {e}')


def quiz_memoria_secretos():
  print('\n--- EXAMEN 2: Memoria y Variables Secretas ---')
  token = os.environ.get('FB_ACCESS_TOKEN')
  if token:
    print(
        f'[ÉXITO] Secreto FB_ACCESS_TOKEN detectado. Longitud del token:'
        f' {len(token)} caracteres.'
    )
  else:
    print('[ALERTA] El secreto FB_ACCESS_TOKEN no está disponible.')


def quiz_reporte_interno():
  print('\n--- EXAMEN 3: Auditoría y Reporte Interno ---')
  archivos_locales = os.listdir('.')
  print(f'[ÉXITO] Archivos en la raíz del búnker: {archivos_locales}')
  if 'README.md' in archivos_locales:
    with open('README.md', 'r', encoding='utf-8') as f:
      lineas = f.readlines()
    print(f'[ÉXITO] Archivo README.md auditado: {len(lineas)} líneas leídas.')


if __name__ == '__main__':
  print('=== INICIANDO EXAMEN COMPLETO DEL FANTASMA DIGITAL ===')
  quiz_conectividad()
  quiz_memoria_secretos()
  quiz_reporte_interno()
  print('=== EXAMEN FINALIZADO CON ÉXITO ===')