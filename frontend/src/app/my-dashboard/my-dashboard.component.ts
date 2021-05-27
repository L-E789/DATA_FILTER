import { Component, OnInit } from '@angular/core';
import {environment} from '../../environments/environment';
import { ActivatedRoute , ParamMap } from '@angular/router';
import { ClientService} from '../service/client.service';
import { FormBuilder, FormGroup, Validators } from '@angular/forms';

import { ToastrService } from 'ngx-toastr';
import jwt_decode from 'jwt-decode'
import Swal from 'sweetalert2';

@Component({
  selector: 'app-my-dashboard',
  templateUrl: './my-dashboard.component.html',
  styleUrls: ['./my-dashboard.component.css']
})
export class MyDashboardComponent implements OnInit {

  token: any;
  id_environment : number;
  data: number;

  constructor(
    private fb: FormBuilder,
    private routes : ActivatedRoute,
    private client: ClientService,
    private toastr: ToastrService
  ) { }

  ngOnInit(): void {
    this.token = jwt_decode(localStorage.getItem('token'));

    this.routes.paramMap
    .subscribe((params : ParamMap) => {
    let id = + params.get('id');
    this.id_environment = id;
  });
  this.show(); 
}

  show(){
    let data = ({
      status : 2,
      environment : this.id_environment,
      user: this.token.id
    });
    this.client.postRequest(`${environment.BASE_API_REGISTER}/show/device/progress/my_dashboard`,data).subscribe(
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


}
