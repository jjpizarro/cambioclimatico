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

class Medicion(Base):
    __tablename__ = "mediciones"
    id = Column(Integer, primary_key= True, index=True)
    fecha = Column(DateTime, nullable=False)
    valor = Column(Float)
    qf = Column(Enum(QualityFlag))
    estacion_id = Column(Integer,ForeignKey('estaciones.id'))
    parametro_id = Column(Integer,ForeignKey('parametros.id'))

INSERT INTO mediciones(id,fecha, valor, qf, estacion_id, parametro_id) VALUES
(1,'2008/12/31 13:00:00.59','Bueno',10,1)