import {Component, OnInit} from '@angular/core';
import {HttpClient, HttpClientModule} from "@angular/common/http";
import {NgForOf, NgIf} from "@angular/common";
import {RouterLink} from "@angular/router";
import {FormControl, FormGroup, FormsModule, ReactiveFormsModule} from "@angular/forms";

@Component({
  selector: 'app-admin-panele-component',
  standalone: true,
  imports: [
    NgForOf,
    HttpClientModule,
    RouterLink,
    NgIf,
    FormsModule,
    ReactiveFormsModule,
  ],
  templateUrl: './admin-panele-component.component.html',
  styleUrl: './admin-panele-component.component.scss'
})
export class AdminPaneleComponentComponent implements OnInit{
  nodes: Array<node_detect> = []
  selectedModel:any
  loading_node = true;

  myForm : FormGroup = new FormGroup({
    "existNode": new FormControl('no'),
    "NodeName": new FormControl(),
    "Profile": new FormControl('medium'),
  });

  constructor(private http: HttpClient) {
  }
  ngOnInit(): void {
  this.updateNodes()

  }

  updateNodes(){
    this.loading_node = true;
    this.http.get("http://reter34erwd.duckdns.org:6788/get_active_nodes").subscribe((value:any) => {
      this.loading_node = false;
      debugger;
      value.forEach( (x:any) => {
        let nodeDetect = new node_detect();
        nodeDetect.node_ulr= x.node_ulr;
        nodeDetect.status = x.status;
        this.nodes.push(nodeDetect);
      })
    }, error => {
      this.loading_node = false;
      debugger;
    })
  }

  onFileSelected(event:any) {
    const file:File = event.target.files[0];

    if (file) {

      const reader = new FileReader();
      reader.onload = (e: any) => {
        this.selectedModel = e.target.result;
      };
      reader.readAsDataURL(file);
      const formData = new FormData();
      formData.append("file", file);

    }
  }

  AddServer() {
    const upload$ = this.http.post("http://reter34erwd.duckdns.org:6788/add_server",
      {
        exist: this.myForm.get("existNode")?.value,
        node_name: this.myForm.get("NodeName")?.value,
        profile: this.myForm.get("Profile")?.value,
      })
      .subscribe(values =>{
          this.updateNodes();
        },
        error => {
          this.updateNodes();
        })
  }
}

class node_detect {
  public node_ulr = "";
  public status = false;
}
