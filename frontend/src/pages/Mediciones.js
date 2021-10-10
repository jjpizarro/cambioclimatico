import React, {useState, useEffect,useMemo} from "react";
import MedicionServicio from '../services/mediciones.services';
import ModalForm from '../components/ModalForm';
import Pagination from '../components/Pagination'
let PageSize = 10;
const Mediciones = (props) =>{
    const [mediciones, setMediciones] = useState([]);
    const [estaciones, setEstaciones] = useState([]);
    const [parametros,setParametros] = useState([]);
    const [currentPage, setCurrentPage] = useState(1);

      /*const currentTableData = useMemo(() => {
        const firstPageIndex = (currentPage - 1) * PageSize;
        const lastPageIndex = firstPageIndex + PageSize;
       
        MedicionServicio.getMediciones().then(response=>{
          setMediciones(response.data);
          lista = response.data;
        });
        return mediciones.slice(firstPageIndex, lastPageIndex);
      }, [currentPage]);*/
    const initialFiltros = {
        estacion : '',
        startdate: null,
        enddate: null, 
        parametro:''

    }
    const [filtros, setFiltros] = useState(initialFiltros);
    const handleOnChange = (event) => {
        const { name, value } = event.target;
        setFiltros({
          ...filtros,
          [name]: value
        });
        
      };
      
    useEffect(() => {
        /*MedicionServicio.getMediciones().then(response=>{
            setMediciones(response.data);
        });*/
        MedicionServicio.getEstaciones().then(response=>{
            setEstaciones(response.data);
        });
        MedicionServicio.getParametros().then(response =>{
            setParametros(response.data);
        });

    }, []);
    const executeSubmit = (ev)=>{
        ev.preventDefault();
        MedicionServicio.filtrarBusqueda(filtros).then(response=>{
          setMediciones(response.data);
        });
    }

    const updateMediciones = (item) => {
      const itemIndex = mediciones.findIndex(data => data.id === item.id)
      const newArray = [...mediciones.slice(0, itemIndex), item, ...mediciones.slice(itemIndex + 1)]
      setMediciones(newArray)
    }
    return (
        <>
         
        <main className="h-100">
            <div className="pricing-header p-3 pb-md-4 mx-auto text-center">
            <h1 className="display-6 fw-normal">Mediciones</h1>
            <p className="fs-6 text-muted">Lorem ipsum dolor, sit amet consectetur adipisicing elit. Obcaecati ut, quos a enim saepe odit velit unde dignissimos eum ullam amet corrupti placeat aspernatur earum nemo quia consequuntur corporis esse.</p>
          </div>
          <div className="row justify-content-center">
            <div className="col-md-10">
              <div className="card">
                <div className="card-body">
                  
                  <form onSubmit={executeSubmit} className="row row-cols-lg-auto g-3 align-items-center">
                    <div className="col-sm-3">
                      <label className="visually-hidden" for="param">Estación</label>
                      <select className="form-select" id="estacion" name="estacion" value={filtros.estacion}  onChange={handleOnChange} >
                      <option selected>Seleccione...</option>
                      {(
                            estaciones.map(estacion =>(
                                <option value={estacion.id}>{estacion.nombre}</option>
                            ))
                        )}
                      </select>
                    </div>
                    <div className="col-sm-3">
                      <label className="visually-hidden" for="startdate">Fecha inicial</label>
                      <input type="datetime-local" className="form-control" id="startdate" name="startdate" value={filtros.startdate}  onChange={handleOnChange}/>
                    </div>
                    <div className="col-sm-3">
                      <label className="visually-hidden" for="enddate">Fecha final</label>
                      <input type="datetime-local" className="form-control" id="enddate" name="enddate" value={filtros.enddate}  onChange={handleOnChange}/>
                    </div>
                    <div className="col-sm-3">
                      <label className="visually-hidden" for="parametro">Parámetro</label>
                      <select className="form-select" id="parametro" name ="parametro" value="parametro" value={filtros.parametro}  onChange={handleOnChange}>
                        <option selected>Seleccione...</option>
                        {(
                            parametros.map(parametro =>(
                                <option value={parametro.id}>{parametro.nombre}</option>
                            ))
                        )}
                        
                      </select>
                    </div>
                    <div className="col-sm-2">
                      <button type="submit" className="btn btn-primary">Buscar</button>

                    </div>
                  </form>
                </div>
              </div>
            </div>
          </div>
          <p></p>
          <div className="row justify-content-center">
            <div className="col-md-10">
              <table className="table">
                <thead>
                  <tr><th>Estación</th><th>Fecha</th><th>Parámatro</th><th>Medición</th><th>Unidad</th><th>Calidad</th><th>Acción</th></tr>
                </thead>
                <tbody className="">
                {mediciones.length > 0 ? (
                    mediciones.map((medicion)=>(
                        <tr key={medicion.id}>
                        <td>{medicion.estacion}</td>
                        <td>{medicion.fecha}</td>
                        <td>{medicion.parametro}</td>
                        <td>{medicion.valor}</td>
                        <td>{medicion.unidad}</td>
                        <td>{medicion.qf}</td>
                        <td>
                           <ModalForm medicion={medicion} onUpdate = {updateMediciones} />
                          {/*<svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" fill="currentColor" className="bi bi-pencil-square" viewBox="0 0 16 16">
                          <path d="M15.502 1.94a.5.5 0 0 1 0 .706L14.459 3.69l-2-2L13.502.646a.5.5 0 0 1 .707 0l1.293 1.293zm-1.75 2.456-2-2L4.939 9.21a.5.5 0 0 0-.121.196l-.805 2.414a.25.25 0 0 0 .316.316l2.414-.805a.5.5 0 0 0 .196-.12l6.813-6.814z"/>
                          <path fill-rule="evenodd" d="M1 13.5A1.5 1.5 0 0 0 2.5 15h11a1.5 1.5 0 0 0 1.5-1.5v-6a.5.5 0 0 0-1 0v6a.5.5 0 0 1-.5.5h-11a.5.5 0 0 1-.5-.5v-11a.5.5 0 0 1 .5-.5H9a.5.5 0 0 0 0-1H2.5A1.5 1.5 0 0 0 1 2.5v11z"/>
                          </svg>*/}
                        
                        </td>
                      </tr>   
                    ))

                ):(<tr>
            <td colSpan={7}>No se encontraron registros</td>
          </tr>)}
                  
                </tbody>
              </table>
              {/*<Pagination
                className="pagination-bar"
                currentPage={currentPage}
                totalCount={mediciones.length}
                pageSize={PageSize}
                onPageChange={page => setCurrentPage(page)}
              />*/}
            </div>
          </div>
        </main>
        </>
    )
}

export default Mediciones;