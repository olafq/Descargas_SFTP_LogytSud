@echo off
echo voy a ruta del script
cd C:\Users\querolol\OneDrive - Danone\Desktop\Descarga-LogytSud

echo Activando el entorno virtual
call my-Danone\Scripts\activate

echo Ejecutando Script-v2.py
echo Ejecutando Script-v2.py >> ejecucion.txt
python.exe Script-v2.py >> ejecucion.txt 2>&1

if %errorlevel% neq 0 (
    echo Error en la ejecución de Script-v2.py >> ejecucion.txt
    echo Error en la ejecución de Script-v2.py
) else (
    echo Ejecución exitosa de Script-v2.py >> ejecucion.txt
    echo Ejecución exitosa de Script-v2.py
)
echo ================================ >> ejecucion.txt

pause
