# **Requerimientos** ✏️📋

## **Resumen del Proyecto:** 

Prototipo de un sistema de votación basado en la tecnología blockchain para la elección de un representante del aula.

## **Método de priorización:** MosCow

Siendo Must el más importante por del software, Should el siguiente en importancia, could el tercero en importancia y Would aquello que no es tan importante para el software.


## **Requerimientos funcionales.**


|**CODIGO**|**Requerimiento**|**Prioridad**|
| :-: | :-: | :-: |
|RF01|El usuario deberá registrarse para acceder al sistema.|Must|
|RF02|El usuario ya registrado podrá acceder al sistema |Must|
|RF03|El usuario podrá visualizar las facturas dadas por los proveedores.|Must|
|RF04|El usuario podrá mandar a validar los gastos registrados.|Must|
|RF05|Existirá dos tipos de cuenta, la de usuario y la de los proveedores.|Must|
|RF07|Los proveedores podrán acceder a la página y hacer el llenado de sus facturas.|Must|
|RF08|El saldo disponible se irá actualizando según las transacciones realizadas.|Must|
|RF09|El usuario podrá ver en todo momento el saldo que se tiene.|Must|
|RF10|Se podrán visualizar los pagos hechos hasta el momento.|Must|
|RF11|Después de su validación se agendará el pago.|Should|
|RF12|El pago podrá ser manual o automático.|Should|
|RF13|Se podrá visualizar los pagos pendientes y acceder a los detalles.|Should|
|RF14|El usuario podrá visualizar su estado de cuenta de cierto período de tiempo.|Should|
|RF15|Se podrá visualizar los pagos pendientes y acceder a los detalles.|Should|
|RF16|Se podrán visualizar los pagos hechos hasta el momento.|Should|
|RF17|Se podrá elegir la cuenta con la que se pagará la deuda.|Should|

## **Requerimientos no funcionales.**


|**CODIGO**|**Requerimiento**|**Prioridad**|
| :-: | :-: | :-: |
|RNF1|La plataforma actualizará el saldo mediante el api.|Must|
|RNF2|La plataforma deberá recolectar los datos de la factura.|Must|
|RNF3|La plataforma deberá realizar las operaciones con respecto al saldo dependiendo del tipo de pago.|Must|
|RNF3|Se registrará la factura del proveedor en el registro de gastos|Must|
|RNF4|Se podrán asociar cuentas del banco. |Should|
|RNF5|Se mostrarán en el calendario los pagos por realizar y se eliminarán los pagos realizados.|Should|

