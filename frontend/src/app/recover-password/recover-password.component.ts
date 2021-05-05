import { Component, OnInit } from '@angular/core';
import { ActivatedRoute , ParamMap } from '@angular/router';
import { FormBuilder, FormGroup, Validators } from '@angular/forms';
import { Router } from '@angular/router';
import {ClientService} from '../service/client.service';
import {environment} from '../../environments/environment';

import Swal from 'sweetalert2';

@Component({
  selector: 'app-recover-password',
  templateUrl: './recover-password.component.html',
  styleUrls: ['./recover-password.component.css']
})
export class RecoverPasswordComponent implements OnInit {

  form : FormGroup
  ids

  constructor(
    private route: Router,
    private fb: FormBuilder,
    private routes : ActivatedRoute,
    private client: ClientService,
  ) { }

  ngOnInit(): void {
    this.routes.paramMap
      .subscribe((params : ParamMap) => {
      let id = + params.get('id');
      this.ids = id;
      this.recoverPassword();
    });

    this.form = this.fb.group({
      password: ['', Validators.required],
      validatepassword: ['', Validators.required],
    });
  }

  recoverPassword(){
    let id = this.ids;
    this.client.getRequestId(`${environment.BASE_API_REGISTER}/recover/pass/`+ id).subscribe(
      (response : any) => {
        console.log(response);
        if(response.codestatus == true){
          Swal.fire({
            position: 'top-end',
            icon: 'success',
            title: 'Codigo Valido',
            showConfirmButton: false,
            timer: 1500
          })
        }else{
          Swal.fire({
            position: 'center',
            icon: 'warning',
            title: 'El codigo a expirado',
            showConfirmButton: false,
            timer: 1500
          })
          this.route.navigate(['/'])
        }
      },(error) => {
        Swal.fire({
          position: 'center',
          icon: 'error',
          title: 'Este codigo no es valido',
          showConfirmButton: false,
          timer: 1500
        })
        this.route.navigate(['/'])
      }
    )
  }

  onSubmit(){
    if(this.form.value.password == this.form.value.validatepassword){
      if(this.form.valid){
        let data = {
          password : this.form.value.password,
          validatepassword : this.form.value.validatepassword,
          code : this.ids
        }
        this.client.postRequest(`${environment.BASE_API_REGISTER}/recover/modification`, data).subscribe(
          (response : any) => {
            Swal.fire({
              position: 'center',
              icon: 'success',
              title: 'contraseña restablecida',
              showConfirmButton: false,
              timer: 1500
            })
            this.route.navigate(['/login']);
          },(error) => {
            console.log(error);
          }
        )
      }else
      console.log('Error validacion');
    }else{
      console.log('Error de igualdad')
    }
  }

}
