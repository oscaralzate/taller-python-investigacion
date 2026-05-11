Pregunta 1: El Staging Area (Area de preparacion)
El staging area (o indice) es una zona intermedia entre tu carpeta de trabajo y el
repositorio permanente. Funciona como una 'sala de espera' donde decides exactamente
que cambios incluiras en tu proximo commit.

Las tres zonas de Git son:
  - Working Directory: Tus archivos actuales en el disco
  - Staging Area: Cambios marcados con 'git add' listos para commit
  - Repository: Historial permanente de commits guardados

Utilidad: Permite hacer commits parciales. Puedes modificar 5 archivos
pero solo hacer commit de 2, manteniendo los demas para despues.


Pregunta 2: El comando git status
Muestra el estado actual del repositorio. Es util ejecutarlo constantemente.
Informacion que proporciona:
  1. La rama en la que estas actualmente
  2. Archivos modificados no agregados al staging area (en rojo)
  3. Archivos en el staging area listos para commit (en verde)
  4. Archivos nuevos que Git no conoce (untracked files)


Pregunta 3: git fetch vs git pull
git fetch: Descarga los cambios del repositorio remoto pero NO los aplica.
           Solo actualiza la informacion local sobre el estado remoto.
git pull:  Descarga los cambios Y los fusiona automaticamente con tu rama local.
           Equivale a hacer 'git fetch' + 'git merge' en un solo comando.

Cuando usar cada uno:
  - git fetch: cuando quieres revisar los cambios antes de integrarlos
  - git pull: cuando confias en los cambios y los quieres integrar directamente

git fetch es mas seguro porque te permite revisar antes de fusionar.


Pregunta 4: Merge conflict (Conflicto de fusion)
Ocurre cuando dos personas modifican la misma linea del mismo archivo
en diferentes ramas y Git no puede decidir cual version conservar.

Ejemplo: Persona A y Persona B editan la misma linea de main.py.

Pasos para resolver un conflicto:
  1. Ejecutar git merge y ver que archivos tienen conflictos
  2. Abrir el archivo conflictivo (Git marca las secciones con <<<, ===, >>>)
  3. Editar manualmente el archivo dejando el contenido correcto
  4. Eliminar las marcas de conflicto (<<<, ===, >>>)
  5. Ejecutar git add sobre el archivo resuelto
  6. Completar con git commit
  Pregunta 1: Pull Request (PR)
Un Pull Request es una solicitud formal para fusionar cambios de una rama a otra.
Es el mecanismo central de colaboracion en GitHub.

Diferencia con merge directo:
  - El merge directo fusiona sin revision previa.
  - El PR permite que otros revisen, comenten y aprueben los cambios primero.

Ventajas del PR en proyectos colaborativos:
  - Control de calidad: otros desarrolladores revisan el codigo
  - Trazabilidad: queda registro de por que se hizo cada cambio
  - Seguridad: evita que codigo defectuoso llegue a produccion


Pregunta 2: Fork en GitHub
Un fork es una copia completa de un repositorio en tu propia cuenta de GitHub.

Diferencia con clone:
  - Fork: crea una copia en GitHub (en la nube, en tu cuenta)
  - Clone: descarga una copia al disco duro de tu computador

Para contribuir a un proyecto open source:
  1. Hacer fork del repositorio original
  2. Clonar TU fork a tu computador
  3. Crear una rama, hacer cambios y commit
  4. Subir la rama a tu fork
  5. Crear un Pull Request desde tu fork hacia el original


Pregunta 3: Archivo .gitignore
Es un archivo que le dice a Git que archivos y carpetas debe ignorar (no trackear).

5 tipos de archivos que NO deben subirse en Python:
  1. venv/ o env/          -> entorno virtual (muy pesado, se recrea con pip)
  2. _pycache_/          -> archivos compilados de Python (se generan solos)
  3. *.pyc                 -> bytecode de Python
  4. .env                  -> variables de entorno con claves secretas
  5. *.egg-info/           -> metadatos de instalacion del paquete

Problemas sin .gitignore: repositorio enormemente pesado, exposicion de
claves secretas, conflictos por archivos generados automaticamente.


Pregunta 4: Issues en GitHub
Los issues son reportes de tareas, bugs, mejoras o preguntas dentro de un proyecto.

Un buen issue debe contener:
  - Titulo claro y descriptivo
  - Descripcion del problema o tarea
  - Pasos para reproducir (si es un bug)
  - Comportamiento esperado vs comportamiento actual
  - Capturas de pantalla o logs si aplica

Relacion con commits: puedes cerrar un issue automaticamente escribiendo
en el mensaje de commit: 'fix: corregir error #5' (donde 5 es el numero del issue)


Pregunta 5: GitHub Actions
GitHub Actions es un sistema de automatizacion integrado en GitHub.
Permite ejecutar flujos de trabajo automaticos cuando ocurren eventos.

Ejemplos de tareas automatizables:
  1. CI (Integracion Continua): ejecutar los tests automaticamente cada vez
     que alguien hace push o crea un Pull Request.
  2. Despliegue automatico: publicar la aplicacion en un servidor cada vez
     que se fusiona codigo en la rama main.
  3. Analisis de calidad: ejecutar linters y revisores de codigo automaticamente.