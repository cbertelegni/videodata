video-data
==========

## Intalación


1. Se recomienda el uso de [virtualenv] — Instalarlo.

2. Crear un entorno virtual y activarlo:

```bash
virtualenv ~/.python-envs/videodata
. ~/.python-envs/videodata/bin/activate
```

3. Obtener el código fuente:

```bash
git clone https://github.com/cbertelegni/video-data.git videodata
cd videodata
```

4. Instalar las dependencias:

```bash
pip install -r requirements.txt
```

   (Si está en Ubuntu, es probable que también deba instalar `python-dev` antes de instalar las depdencias.)

5. Inicializar la DB:

```bash
python manage.py syncdb
python manage.py migrate --all
```
    
6. Iniciar el servidor de desarrollo

```bash
python manage.py runserver_plus
```

