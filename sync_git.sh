#!/usr/bin/env bash

# Script para sincronización automática de Introducción al Cálculo con GitHub
# Autor: Gemini Academic Assistant

REPO_DIR="/mnt/9b846436-0407-4e80-b8af-5417ffbdee8e/Universidad/USS/Ramos actuales/Intro. Cálculo "
cd "$REPO_DIR" || exit 1

echo "=== Iniciando Sincronización con GitHub ==="
echo "Directorio: $REPO_DIR"

# 1. Traer posibles cambios remotos y rebasar para evitar conflictos
echo ">> Obteniendo cambios del repositorio remoto..."
git pull --rebase origin main

# 2. Agregar todos los archivos nuevos y modificados
echo ">> Añadiendo archivos al área de preparación..."
git add -A

# 3. Comprobar si hay cambios para confirmar
if git diff-index --quiet HEAD --; then
    echo ">> No hay cambios pendientes para subir."
else
    # Confirmar cambios con marca de tiempo
    TIMESTAMP=$(date "+%Y-%m-%d %H:%M:%S")
    COMMIT_MSG="Sincronización Académica: $TIMESTAMP"
    echo ">> Creando confirmación: '$COMMIT_MSG'..."
    git commit -m "$COMMIT_MSG"
    
    # Subir al repositorio remoto
    echo ">> Subiendo cambios a GitHub (origin main)..."
    git push origin main
    echo ">> ¡Sincronización completada con éxito!"
fi

echo "=========================================="
