Pregunta 1: Git Rebase vs Git Merge
Git Merge: fusiona dos ramas creando un nuevo 'commit de fusion'.
           Preserva el historial completo tal como ocurrio.

Git Rebase: mueve los commits de una rama y los 'reaplica' sobre otra.
            Reescribe el historial para que parezca lineal y limpio.

Cuando usar rebase: para limpiar commits antes de hacer un Pull Request,
o para actualizar tu rama con los cambios de main sin crear commits de fusion.

'Reescribir la historia' significa cambiar los identificadores (hash) de los commits,
lo cual puede causar problemas si otros ya tienen esos commits.
Regla de oro: NUNCA hagas rebase en ramas publicas compartidas.


Pregunta 2: Git Stash
git stash guarda temporalmente los cambios no confirmados (sin hacer commit).
Util cuando necesitas cambiar de rama pero tienes trabajo a medias.

Ejemplo de situacion: estas trabajando en una nueva funcionalidad y tu jefe
te pide arreglar urgentemente un bug en la rama principal. Usas stash para
guardar tu trabajo incompleto, cambias de rama, arreglas el bug, y luego
recuperas tu trabajo con 'git stash pop'.

Comandos:
  git stash           -> guarda los cambios actuales
  git stash list      -> lista todos los stash guardados
  git stash pop       -> recupera y elimina el stash mas reciente
  git stash apply     -> recupera sin eliminar del stash


Pregunta 3: Commits Convencionales
Es un estandar para escribir mensajes de commit de forma estructurada.
Formato: tipo(alcance): descripcion breve

Importante porque facilita: leer el historial, generar changelogs automaticos,
y entender rapidamente el tipo de cada cambio.

Prefijos adicionales:
  chore:    tareas de mantenimiento (actualizar dependencias)
  perf:     mejoras de rendimiento
  ci:       cambios en integracion continua
  build:    cambios en el sistema de construccion
  revert:   revertir un commit anterior


Pregunta 4: Git Flow
Git Flow es un modelo de trabajo con ramas para proyectos estructurados.
Define reglas claras sobre como y cuando crear cada tipo de rama.

Tipos de ramas en Git Flow:
  main:     codigo en produccion (siempre estable)
  develop:  rama principal de desarrollo
  feature/: nuevas funcionalidades (se crean desde develop)
  release/: preparacion de una nueva version
  hotfix/:  correcciones urgentes directamente en main


Pregunta 5: HEAD Detached (HEAD desvinculado)
Ocurre cuando HEAD apunta directamente a un commit en lugar de a una rama.

Causas comunes: hacer 'git checkout' a un hash de commit especifico,
o a un tag en lugar de a una rama.

Como salir del HEAD detached:
  git checkout main      -> volver a la rama main (perder los cambios)
  git checkout -b nueva-rama  -> crear una rama nueva desde el estado actual


Pregunta 6: Git Log y sus opciones utiles
git log muestra el historial de commits del repositorio.

Flags utiles:
  git log --oneline          -> una linea por commit (hash corto + mensaje)
  git log --graph            -> muestra el grafico de ramas visualmente
  git log --oneline --graph  -> combinacion ideal para ver el historial
  git log -n 5               -> muestra solo los ultimos 5 commits
  git log --author='Nombre'  -> filtra commits por autor
  