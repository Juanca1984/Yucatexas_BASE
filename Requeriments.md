# **Especificación de requerimientos** ✏️📋

## **Resumen del Proyecto:** 
 
En este proyecto contruiremos una plataforma de transferencias, con el objetivo de ofrecer una solución viable para diferentes empresas en la cual podrán agilizar procesos de pagos, sistemas de administración y control de inventarios.

## **Método de priorización:** MosCow

- Must have (es necesario)
- Should have (es recomendable)
- Could have (podría implementares)
- Won't have (no se implemetará... quizá en un futuro)


## **Requerimientos funcionales.**


|**CODIGO**|**Requerimiento**|**Prioridad**|
| :-: | :-: | :-: |
|RF01|El usuario podrá registrarse y acceder al sistema.|Must|
|RF02|El usuario podrá visualizar las facturas dadas por los proveedores.|Must|
|RF03|El usuario podrá mandar a validar los gastos registrados.|Must|
|RF04|Existirán dos tipos de cuenta, la de usuario y la de los proveedores.|Must|
|RF05|Los proveedores podrán realizar el llenado de facturas en la plataforma.|Should|
|RF08|El pago se podrá efectuar de manera manual o automática.|Should|
|RF09|El usuario podrá visualizar su estado de cuenta de cierto período de tiempo.|Should|
|RF10|Se podrá elegir la cuenta con la que se pagará la deuda.|Should|
|RF06|El sistema desplegará una pestaña para visualizar pagos, pagos pendientes y saldos actuales. |Could|
|RF07|Se podrán registrar y administrar pagos recurrentes. |Could|

## **Requerimientos no funcionales.**


|**CODIGO**|**Requerimiento**|**Prioridad**|
| :-: | :-: | :-: |
|RNF01|La plataforma actualizará el saldo mediante la API.|Must|
|RNF03|La plataforma deberá realizar las operaciones con respecto al saldo dependiendo del tipo de pago.|Must|
|RNF04|El saldo disponible se actualizará según las transacciones realizadas.|Must|
|RNF05|Se podrán asociar cuentas de banco. |Must|
|RNF02|La plataforma deberá recolectar los datos de la factura.|Should|
|RNF06|Se registrará la factura del proveedor en el registro de gastos|Could|
|RNF07|Se mostrarán en el calendario los pagos por realizar y se eliminarán los pagos realizados.|Should|

