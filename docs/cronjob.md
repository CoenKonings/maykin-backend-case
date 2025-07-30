# Cronjob
To ensure the database stays up to date, add the following cronjob on the production server:
```
0   0   *   *   *       cd /var/www/hotelmgmt && ./updatehotels.sh
```
This runs the updatehotels command every day at 00:00. The cronjob assumes the project was installed at `/var/www/hotelmgmt`, and a python environment is located at `/var/www/hotelmgmt/.venv`.
