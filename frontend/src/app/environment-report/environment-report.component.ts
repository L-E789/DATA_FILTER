import { Component, OnInit } from '@angular/core';
import { ActivatedRoute , ParamMap, Router } from '@angular/router';
import {AuthService} from '../service/auth.service';
import { ClientService } from '../service/client.service';
import {environment} from '../../environments/environment';
import * as html2pdf from 'html2pdf.js';

import { ToastrService } from 'ngx-toastr';

@Component({
  selector: 'app-environment-report',
  templateUrl: './environment-report.component.html',
  styleUrls: ['./environment-report.component.css']
})
export class EnvironmentReportComponent implements OnInit {

  data: any;

  constructor(
    private route: Router,
    private routes : ActivatedRoute,
    private auth: AuthService,
    private client: ClientService,
    private toastr: ToastrService
  ) { }

  ngOnInit(): void {
    if(localStorage.getItem('token')){
      this.routes.paramMap
      .subscribe((params : ParamMap) => {
      let id = + params.get('id');
      this.data = 0;
      this.showData(id);
    });
    }else{
      this.auth.logout();
      this.route.navigate(['/login'])
    }


  }

  showData(id : number){
    let data = ({
      id : id
    });
    this.client.postRequest(`${environment.BASE_API_REGISTER}/report/general`,data).subscribe(
      (Response : any) => {
        if(Response.error == 400){
          this.toastr.info("Lo sentimos, debido a la poca información no es posible generar un informe");
          this.route.navigate(['/environments']);
        }else{
          this.data = Response;
        }
      },(error) => {
        this.toastr.info("Lo sentimos, debido a la poca información no es posible generar un informe");
        this.route.navigate(['/environments']);
      }
    )
  }

  generatepdf(){
    const options = {
      name: 'output.pdf',
      filename:'DT informe de entorno',
      imagen : {type: 'jpg'},
      html2canvas : {},
      jsPDF : {orientation:'landscape'}
    }

    const element:Element = document.getElementById('table');
    html2pdf().from(element).set(options).save()
  }

}
