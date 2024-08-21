import pysftp
import os

# Ruta del archivo de texto
ruta_txt = 'RutaLocalDescargas.txt'

# Leer la primera línea del archivo de texto
with open(ruta_txt, 'r') as file:
    local_directory = file.readline().strip()

# Asegúrate de que la ruta del directorio local es válida
if not os.path.exists(local_directory):
    raise Exception(f"El directorio local '{local_directory}' no existe.")

# Define los detalles de conexión al servidor SFTP
sftp_host = 'sftp.transfer.logyttpr.com.ar'
sftp_port = 22  # El puerto SFTP por defecto es 22
sftp_username = 'danone_lacteos_ar'
sftp_password = 'yDJy3iIkbl8c1swzl2ZT4tF88mY3ZBN8tewodhhv4tj4EC7'
remote_directory = '/outputs/prod'


# Configura las opciones de conexión
cnopts = pysftp.CnOpts()
cnopts.hostkeys = None

# Conéctate al servidor SFTP
with pysftp.Connection(
        host=sftp_host,
        username=sftp_username,
        password=sftp_password,
        port=sftp_port,
        cnopts=cnopts) as sftp:
    # Cambia al directorio remoto
    sftp.cwd(remote_directory)
    print("Conexión exitosa")

    # Descarga todo el directorio remoto al directorio local
    sftp.get_d(remote_directory, local_directory)

print('Descarga completada.')


