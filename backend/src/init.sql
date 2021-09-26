INSERT INTO estaciones (id, nombre, latitud, longitud, estado) VALUES
(10, 'Aracataca Monato', 10.5522888888889, -74.083166667, 'activa'),
(20, 'Sitio Nuevo VIPIS 2', 10.552377778, -74.083183333,  'activa'),
(30, 'Plato', 9.779055556, -74.586611111, 'activa'),
(40, 'Sabanas de San Angel', 10.035516667, -74.216061111, 'activa'),
(50, 'Sitio Nuevo VIPIS 1', 11.029061111, -74.722666667,  'activa'),
(60, 'Sitio Nuevo VIPIS 3', 10.542861111, -74.066583333,  'activa'),
(70, 'Santa Bárbara de Pinto', 9.597194444, -74.636555556,  'activa'),
(80, 'Aracataca Lora 1', 10.531561111, -74.079316667,  'activa'),
(90, 'Aracataca Lora 2', 10.030572222, -74.085516667,  'activa');

INSERT INTO parametros (id,nombre,descripcion, min_valor, max_valor, unidad) VALUES
(1,'ch4', 'Metano (CH4)', 100, 3000,'ppb'),
(2,'co2', 'CO2', 150, 600,'ppm'),
(3,'Humedad', 'Humedad relativa', 30, 100,'%'),
(4,'Temperatura', 'Temperatura', 19, 45,'°C');


INSERT INTO mediciones(id,fecha, valor, qf, estacion_id, parametro_id) VALUES
(1,'2008/12/31 13:00:00.59','Bueno',10,1)

with datos_estaciones(estacion,lat,lon,fecha, variable, unidad, value, qf, nombre_estacion) as (
select
l.id AS estacion,
e.latitud AS lat,
e.longitud AS lon,
l.fecha AS fecha,
pa.nombre AS variable,
pa.unidad AS unidad,
l.valor AS value,
l.qf AS qf,
e.nombre AS nombre_estacion
from estaciones e inner join mediciones l on l.estacion_id = e.id join parametros pa on l.parametro_id = pa.id
) 
select
p.estacion,
p.lat AS latitud,
p.lon AS longitud,
p.fecha AS fecha,
case 
when (p.variable = 'co2') then max(p.value) 
else null end AS CO2,
case 
when (p.variable = 'ch4') then max(p.value) 
else null end AS CH4,
case 
when (p.variable = 'Humedad') then max(p.value) 
else null end AS Humedad,
case 
when (p.variable = 'Temperatura') then max(p.value) 
else null end AS Temperatura

from datos_estaciones p
	where p.qf = 'bueno' or p.qf = 'no_verificado'
group by p.estacion,p.nombre_estacion,p.lat,p.lon,p.fecha,p.variable