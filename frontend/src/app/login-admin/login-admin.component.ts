import { Component, OnInit } from '@angular/core';
import { FormBuilder, FormGroup, Validators } from '@angular/forms';
import { ClientService } from '../service/client.service';
import {environment} from '../../environments/environment';

import { ToastrService } from 'ngx-toastr';


@Component({
  selector: 'app-login-admin',
  templateUrl: './login-admin.component.html',
  styleUrls: ['./login-admin.component.css']
})
export class LoginAdminComponent implements OnInit {

  form : FormGroup;

  constructor(
    private fb: FormBuilder,
    private client: ClientService,
    private toastr: ToastrService
  ) { }

  ngOnInit(): void {
    this.form = this.fb.group({
      user : ['', Validators.required],
      password : ['', Validators.required]
    });
  }

  login(){
    if(this.form.valid){
      let data = ({
        user : this.form.value.user,
        password : this.form.value.password
      });
      this.client.postRequest(`${environment.BASE_API_REGISTER}`,data).subscribe(
        (Response : any) => {
          console.log(Response);
        },(error) => {
          console.log(error);          
        }
      )
    }
  }
  

}
