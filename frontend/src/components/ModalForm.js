import React, { useState, useEffect } from 'react';
import Button from 'react-bootstrap/Button';
import Modal from 'react-bootstrap/Modal';
import ModalBody from 'react-bootstrap/ModalBody';
import ModalHeader from 'react-bootstrap/ModalHeader';
import Form from 'react-bootstrap/Form';
import Row from 'react-bootstrap/Row';
import Col from 'react-bootstrap/Col';
import MedicionServicio from '../services/mediciones.services';



export default function ModalForm({medicion,onUpdate}) {
   
  const [show, setShow] = useState(false);

  const handleClose = () => setShow(false);
  const handleShow = () => setShow(true);

  const closeBtn = <button className="close" onClick={handleClose}>&times;</button>
  const labelButton = 'Validar';
  const button = <Button
            variant="outline-secondary"
            onClick={handleShow}
            style={{float: "left", marginRight:"10px"}}>{labelButton}
          </Button>
  const title = 'Cambiar bandera de calidad';
  const initialValueState = {id:medicion.id,qf:medicion.qf};
  const [form, setValues] = useState(initialValueState);
  const onChange = e => {
      setValues({
        ...form,
        [e.target.name]: e.target.value
      });
    }
  const submitFormEdit = e => {
    e.preventDefault();

    MedicionServicio.updateMedicion(form).then(response=>{
      onUpdate(response.data);
      handleClose();
    });
  }
   
  return (
      <div>
        {button}
        <Modal show={show} onHide={handleClose}>
          <ModalHeader closeButton  close={closeBtn}><h4>{title}</h4></ModalHeader>
          <ModalBody>
              <Form onSubmit={ submitFormEdit}>
                  <Form.Group>
                      <Form.Label>Estación</Form.Label>
                      <Form.Control disabled type="text" name="estacion" id="estacion" value={medicion.estacion} />
                  </Form.Group>
                  <Form.Group>
                      <Form.Label>Parámetro</Form.Label>
                      <Form.Control disabled type="text" name="parametro" id="parametro" value={medicion.parametro}  />
                  </Form.Group>
                  <Form.Group>
                      <Form.Label>Medición</Form.Label>
                      <Form.Control disabled type="email" name="email" id="email" value={medicion.valor}  />
                  </Form.Group>
                  <Form.Group className="mb-3">
                        <Form.Label>Bandera de calidad</Form.Label>
                      <Form.Select name="qf" id="qf" aria-label="Seleccione" onChange={onChange} value={medicion.qf}>
                          <option>Seleccione ... </option>
                          <option value="bueno">Bueno</option>
                          <option value="no_verificado">No Verificado</option>
                          <option value="sospechoso">Sospechoso</option>
                          <option value="malo">Malo</option>
                          <option value="dato_faltante">Dato faltante</option>
                        
                      </Form.Select>
                  </Form.Group>
                  <Form.Group as={Row} className="justify-content-md-center mb-3">
                    <Col md="auto">
                      <Button type="submit" variant="success">Guardar</Button>{' '}
                      <Button onClick={e => handleClose() } variant="secondary">Cancelar</Button>
                    </Col>
                  </Form.Group>
        
              </Form>
          </ModalBody>
        </Modal>
      </div>
    )
}