import { Component, OnInit } from '@angular/core';
import { FormBuilder, FormGroup, Validators } from '@angular/forms';
import {environment} from '../../environments/environment';
import { ClientService} from '../service/client.service';

import { ToastrService } from 'ngx-toastr';

@Component({
  selector: 'app-contact-us',
  templateUrl: './contact-us.component.html',
  styleUrls: ['./contact-us.component.css']
})
export class ContactUsComponent implements OnInit {

  form : FormGroup;

  constructor(
    private fb : FormBuilder,
    private toastr: ToastrService,
    private client: ClientService
  ) { }

  ngOnInit(): void {
    this.form = this.fb.group({
      name : ['', Validators.required],
      email : ['', Validators.email],
      message : ['', Validators.required]
    });
  }

  save(){
    if(this.form.valid){
      let data = ({
        name : this.form.value.name,
        email : this.form.value.email,
        message : this.form.value.message
      });
      this.client.postRequest(`${environment.BASE_API_REGISTER}/contact`,data).subscribe(
        (Response : any) => {
          this.form.reset();
          this.toastr.success("La informacion fue enviada","Gracias");
        },(error) => {
          console.error(error);
        }
      )
    }else{
      this.toastr.warning("Complete todos los campos");
    }
  }

}
