import { Component, OnInit } from '@angular/core';
import { ActivatedRoute , ParamMap } from '@angular/router';
import {environment} from '../../environments/environment';
import { FormBuilder, FormGroup, Validators } from '@angular/forms';
import { ClientService} from '../service/client.service';
import {AuthService} from '../service/auth.service';
import { Router } from '@angular/router';

import { ToastrService } from 'ngx-toastr';
import jwt_decode from 'jwt-decode'
import Swal from 'sweetalert2';

@Component({
  selector: 'app-add-devices',
  templateUrl: './add-devices.component.html',
  styleUrls: ['./add-devices.component.css']
})
export class AddDevicesComponent implements OnInit {

  formConsult : FormGroup;
  token;
  btnnext:boolean = false;
  clientdata;

  constructor(
    private fb: FormBuilder,
    private routes : ActivatedRoute,
    private client: ClientService,
    private auth: AuthService,
    private route: Router,
    private toastr: ToastrService
  ) { }

  btnCancel(){
    this.clientdata = '';
    this.btnnext = false;
    this.formConsult.reset();
  }

  ngOnInit(): void {
    this.token = jwt_decode(localStorage.getItem('token'));

    this.formConsult = this.fb.group({
      consult : ["", Validators.required]
    });
  }

  onSubmit(){

    if(this.formConsult.valid){
      let data = ({
        consult: this.formConsult.value.consult,
        id_user: this.token.id,
        environment : localStorage.getItem("environment")
      });
      this.client.postRequest(`${environment.BASE_API_REGISTER}/environment/main/consultclient`,data).subscribe(
        (Response : any) => {
          this.clientdata = Response;
          this.btnnext = true;
        },(error) => {
          console.log(error);
        }
      )
    }
  }

}
