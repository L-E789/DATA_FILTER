import { Component, OnInit } from '@angular/core';
import { ClientService} from '../service/client.service';
import {environment} from '../../environments/environment';
import { FormBuilder, FormGroup, Validators } from '@angular/forms';
import { Router } from '@angular/router';

import { ToastrService } from 'ngx-toastr';


@Component({
  selector: 'app-register',
  templateUrl: './register.component.html',
  styleUrls: ['./register.component.css']
})
export class RegisterComponent implements OnInit {

  form : FormGroup;
  spinner:boolean = true;

  constructor(
    private fb: FormBuilder, 
    private route: Router,
    private client: ClientService,
    private toastr: ToastrService) { }


  ngOnInit(): void {
    this.form = this.fb.group({
      name: ['', Validators.required],
      surname: ['', Validators.required],
      email: ['', Validators.email],
      password: ['', Validators.required],
      validatepassword: ['', Validators.required],
    });
  }

  async onSubmit(){
    if (this.form.valid){
      if(this.form.value.password == this.form.value.validatepassword){
        this.spinner = false;
        let data ={
          name: this.form.value.name,
          surname: this.form.value.surname,
          email: this.form.value.email,
          password: this.form.value.password,
          validatepassword: this.form.value.validatepassword
        };
        console.log(data)
        this.client.postRequest(`${environment.BASE_API_REGISTER}/register`, data).subscribe(
          (response: any) =>{
            console.log(response)
            this.toastr.success('Valide el correo electronico para activar su cuenta');
            this.route.navigate(['/login'])
          },(error) =>{
            console.log("Error")
          }
        )
      }else{
        this.spinner = true;
        this.toastr.error('Las contraseñas no coinciden. vuelve a intentarlo','Error');
      }
    }else{
      this.spinner = true;
      this.toastr.error('Rellene todos los campos','Error');
    }
  }

  get name(){return this.form.get('name')};
}
