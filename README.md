# Python secure notes
Aplicación CLI para gestionar notas encriptadas usando Python.

## Características

- CRUD completo de notas
- Tests con pytest
- Encriptación de contenido (Proximamente)
- CLI mejorada (Proximamente)

## Instalación

git clone https://github.com/javi-kl/python-secure-notes.git
cd python-secure-notes
pip install -r requirements.txt


### Ejecutar programa
python3 -m src.python_secure_notes.main


### Ejecutar tests
**Ejecutar todos los tests**
    pytest

**Solo tests de un archivo**
    pytest test_archivo.py
    pytest test_opciones.py
    pytest test_recolector.py
    
**Parar en el primer fallo**
    pytest -x


## Tecnologías

- Python 3.10+
- pytest

