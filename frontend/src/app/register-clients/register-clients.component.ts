import { Component, OnInit } from '@angular/core';
import {environment} from '../../environments/environment';
import { FormBuilder, FormGroup, Validators } from '@angular/forms';
import {AuthService} from '../service/auth.service';
import { ClientService} from '../service/client.service';
import { Router } from '@angular/router';

import { ToastrService } from 'ngx-toastr';

@Component({
  selector: 'app-register-clients',
  templateUrl: './register-clients.component.html',
  styleUrls: ['./register-clients.component.css']
})
export class RegisterClientsComponent implements OnInit {

  form : FormGroup

  constructor(
    private fb: FormBuilder,
    private client: ClientService,
    private auth: AuthService,
    private route: Router,
    private toastr: ToastrService
  ) { }

  ngOnInit(): void {
    this.form = this.fb.group({
      name:[''],
      surname:[''],
      identification:[''],
      phone: [''],
      email: ['', Validators.email],
      address: ['']
    });
  }

  onSubmit(){
    if(this.form.valid){
      let data = ({
        name : this.form.value.name,
        surname : this.form.value.surname,
        identification : this.form.value.identification,
        email : this.form.value.email,
        phone : this.form.value.phone,
        address: this.form.value.address,
        environment : localStorage.getItem('environment')
      });
      this.client.postRequest(`${environment.BASE_API_REGISTER}/environment/main/registerclient`, data).subscribe(
        (Response : any) => {
          console.log(Response);
          this.toastr.success('se agrego el cliente con exito');
          this.form.reset();
        },(error) => {
          console.log(error);
        }
      )
    }
  }

}
