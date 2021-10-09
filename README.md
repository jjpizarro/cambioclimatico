# cambioclimatico

## Comandos de ayuda
### Revisar las instancias de docker
docker-compose exec <nombreservicio> psql -U postgres

### Backup de la bd
docker exec -t id_contenedor pg_dumpall -c -U usuario-db > dump_`date +%d-%m-%Y"_"%H_%M_%S`.sql
### Ejecución de scripts a la bd
docker cp path_archivo_sql id_contenedor:path/nombrearchivo.sql
docker exec -it id_contenedor bash
psql nombre_base_datos usuario_bd -f /ruta/archivo.sql