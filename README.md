# Proyecto Urban Grocers 
Pruebas automatizadas para la api de Urban Grocers, especificamente la sección de creación de kits de comida.

## Necesario para ejecutar las pruebas:
Requisitos Previos:

- Instalar librerias pytest y requests:
  > > pip3 install pytest  
  > > pip3 install requests

## Para ejecutar las pruebas:
1. Clona el repositorio.
2. Instala las dependencias necesarias.
3. Ejecuta las pruebas con el comando `pytest create_kit_name_kit_test.py`.

## Archivos:
- `configuration.py`: Contiene las configuraciones de la URL base y los endpoints.
- `data.py`: Proporciona los cuerpos de las solicitudes POST.
- `sender_stand_request.py`: Maneja el envío de las solicitudes a la API.
- `create_kit_name_kit_test.py`: Contiene las pruebas automatizadas utilizando pytest.
- `README.md`: Descripción del proyecto.
- `.gitignore`: Archivos y carpetas a ignorar por git.

## Dependencias usadas:
- `requests`
- `pytest`

## Fuente de documentación utilizada:
apiDoc: https://cnt-c4158072-4164-4dfa-88cf-24ea729c8678.containerhub.tripleten-services.com/docs/
