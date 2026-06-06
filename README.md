# Introducción al Cálculo (USS)

Repositorio de estudio y resoluciones para la asignatura **Introducción al Cálculo (DCEX 0008)** en la Universidad San Sebastián.

---

## 📁 Estructura del Repositorio

El repositorio está organizado en las siguientes secciones principales para facilitar el estudio y la consulta de materiales:

*   **`Teoría/`**: Diapositivas oficiales de las clases de cátedra del curso (Clase 1 a 14) dictadas por la académica Soledad Merino Ñanco.
*   **`Taller/`**: Colección de guías de ejercicios oficiales (Listados 1 a 9) y recursos prácticos.
    *   **`Taller/Respuestas Gemini/`**: Resoluciones exhaustivas, redactadas con rigurosidad académica y formato formal de álgebra paso a paso (Listados 7, 8 y 9).
*   **`Apuntes Markdown/`**: Apuntes digitales tomados en Notion y sincronizados automáticamente a formato Markdown (`.md`) para facilitar su lectura local e indexación.
*   **`Evaluaciones/`**: Certámenes y controles históricos del curso.
    *   **`Evaluaciones/Solemnes/Solemne 2/`**: Materiales correspondientes a la evaluación Solemne 2, incluyendo el informe redactado y el código fuente `.tex` / `.pdf` de la presentación del proyecto.

---

## 🛠️ Herramientas y Sincronización

### Sincronización Automática con Notion (`sync_notion.py`)
Ubicado en la carpeta de herramientas locales del sistema, este script en Python se conecta mediante la API de Notion a la base de datos de apuntes académicos del estudiante para descargar, transformar y organizar las notas directamente en la carpeta local `Apuntes Markdown/`.

### Script de Sincronización con GitHub (`sync_git.sh`)
Para mantener el repositorio al día de forma automática sin comandos manuales repetitivos, se incluye el script de shell `sync_git.sh` en la raíz de la carpeta de trabajo:
*   Realiza un `git pull --rebase` automático para evitar conflictos con actualizaciones remotas.
*   Añade todos los archivos nuevos o modificados respetando las directivas del archivo `.gitignore`.
*   Realiza un commit automático con marca de tiempo actual (ej. `Sincronización Académica: 2026-06-06 14:53:00`) y ejecuta un `git push` a la rama principal.

Para ejecutarlo, simplemente abre la terminal en la raíz del proyecto y corre:
```bash
./sync_git.sh
```

---

## 🛡️ Políticas de Privacidad y Datos
Para resguardar la privacidad y los datos sensibles del entorno de desarrollo del estudiante, el archivo `.gitignore` está configurado para excluir del seguimiento de Git:
*   Planificaciones administrativas y cronogramas internos.
*   Archivos PDF generales de números reales no pertenecientes al programa público.
*   Archivos temporales del sistema, cachés de Python (`__pycache__`), y directorios auxiliares como `.antigravitycli/`.
*   Archivos auxiliares de compilación de LaTeX (`.aux`, `.log`, `.nav`, `.out`, `.snm`, `.synctex.gz`, `.toc`) e imágenes pesadas o capturas en la carpeta de presentaciones de la Solemne 2, manteniendo únicamente los archivos fuente `.tex` y el compilado final `.pdf`.