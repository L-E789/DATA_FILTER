import { Component, OnInit } from '@angular/core';

@Component({
  selector: 'app-customer-history',
  templateUrl: './customer-history.component.html',
  styleUrls: ['./customer-history.component.css']
})
export class CustomerHistoryComponent implements OnInit {

  constructor() { }

  boleano: boolean = false;

  public data = [
    {name: 'Luis Eduardo', apellido: 'Rodriguez', cedula: '100674823', email: 'luisedt@gmail.com'},
    {name: 'Mario', apellido: 'Mendoza', cedula: '100853539', email: 'mario@gmail.com'},
    {name: 'Jose Antonio', apellido: 'Suarez', cedula: '100630287', email: 'Joseantonio@gmail.com'},
    {name: 'Carlos Manuel', apellido: 'Nuñez', cedula: '100735012', email: 'Carlosmanuel@gmail.com'}];

    title = 'angulardatatables';
    dtOptions: DataTables.Settings = {};

  ngOnInit(): void {
    this.dtOptions = {
      pagingType: 'full_numbers',
      pageLength: 10,
      dom: 'Bfrtip',
      responsive: true,
      
      language: {
        processing: "Procesando...",
        search: "Buscar:",
        lengthMenu: "Mostrar _MENU_ &eacute;l&eacute;ments",
        info: "Mostrando desde _START_ al _END_ de _TOTAL_ elementos",
        infoEmpty: "Mostrando ningún elemento.",
        infoFiltered: "(filtrado _MAX_ elementos total)",
        infoPostFix: "",
        loadingRecords: "Cargando registros...",
        zeroRecords: "No se encontraron registros",
        emptyTable: "No hay datos disponibles en la tabla",
        paginate: {
          first: "Primero",
          previous: "Anterior",
          next: "Siguiente",
          last: "Último"
        },
        aria: {
          sortAscending: ": Activar para ordenar la tabla en orden ascendente",
          sortDescending: ": Activar para ordenar la tabla en orden descendente"
        }
      }
    };

  }

}
