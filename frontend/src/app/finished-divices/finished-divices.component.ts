import { Component, OnInit } from '@angular/core';
import {environment} from '../../environments/environment';
import { ToastrService } from 'ngx-toastr';
import { ActivatedRoute , ParamMap } from '@angular/router';
import { ClientService} from '../service/client.service';
import { EnvironmentsComponent } from '../environments/environments.component'

import Swal from 'sweetalert2';

@Component({
  selector: 'app-finished-divices',
  templateUrl: './finished-divices.component.html',
  styleUrls: ['./finished-divices.component.css']
})
export class FinishedDivicesComponent implements OnInit {

  id_environment : number;
  data : any;
  more: any;
  noresults : number;

  constructor(
    private routes : ActivatedRoute,
    private client: ClientService,
    private toastr: ToastrService,
    private env: EnvironmentsComponent
  ) { }

  ngOnInit(): void {
    this.routes.paramMap
    .subscribe((params : ParamMap) => {
    let id = + params.get('id');
    this.id_environment = id;
    });
    this.show()
  }

  search(search:string){
    if(this.data != 0){
      this.noresults = null;
      let searchArr : any[] = []
      let tosearch = search.toLowerCase();
      if (tosearch.length > 0){
        for(let i = 0; i < this.data.length; i++){
            let buscar = this.data[i];
            let showdata = buscar.client.toLowerCase();
            if(showdata.indexOf(tosearch) >= 0){
              searchArr.push(buscar);
            }
        }
        if(searchArr.length > 0 ){
          this.data = searchArr;
        }else{
          this.noresults = 1;
        }
      }else{
        this.show();
      }
    }
  }
  
  moreInfo(id : number){
    let data = ({
      environment : this.id_environment,
      id_device: id
    });
    this.client.postRequest(`${environment.BASE_API_REGISTER}/show/device/progress/moreinfo`,data).subscribe(
      (Response : any) => {
        this.more = Response;
      },(error) => {
        console.error(error);
      }
    )
  }

  show(){
    let data = ({
      status : 3,
      environment : this.id_environment
    })
    this.client.postRequest(`${environment.BASE_API_REGISTER}/show/device/finished`,data).subscribe(
      (Response : any) => {
        if(Response){
          this.data = Response;
        }else{
          this.data = 0;
        }
      },(error) => {
        this.data = 0;
      }
    )
  }

  removeDevice(id : number){
    let data = ({
      id_device : id,
      status : 4,
      environment : this.id_environment
    });
    Swal.fire({
      title: '¿Estás seguro?',
      text: "¡Estás a punto de retirar este dispositivo!",
      icon: 'warning',
      showCancelButton: true,
      confirmButtonColor: '#3085d6',
      cancelButtonColor: '#d33',
      confirmButtonText: 'Si',
      cancelButtonText: `Cancelar`,
    }).then((result) => {
      if (result.isConfirmed) {
        this.client.postRequest(`${environment.BASE_API_REGISTER}/device/remove`,data).subscribe(
          (Response : any) => {
            this.env.countDevices();
            this.show();
          },(error) => {
            console.error(error);
          }
        )
      }
    })
  }
}