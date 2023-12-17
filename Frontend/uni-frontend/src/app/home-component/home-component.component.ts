import {AfterViewInit, Component, ElementRef, OnInit, ViewChild} from '@angular/core';
import {FormControl, FormGroup, ReactiveFormsModule, Validators} from "@angular/forms";
import {NgForOf, NgIf} from "@angular/common";
import {HttpClient, HttpClientModule} from "@angular/common/http";
import {error} from "@angular/compiler-cli/src/transformers/util";

@Component({
  selector: 'app-home-component',
  standalone: true,
  imports: [
    ReactiveFormsModule,
    HttpClientModule,
    NgIf,
    NgForOf
  ],
  templateUrl: './home-component.component.html',
  styleUrl: './home-component.component.scss'
})
export class HomeComponentComponent  implements  OnInit  {
  selectedImage:any
  points: Defect[] = []
  public imgWidth: any;
  public imgHeight: any;
  public url: any;
  public image:any;

  defectDesc = ["не дефект", "потертость" , "черная точка",
                        "плена","маркер","грязь",
                        "накол","н.д. накол","микровыступ",
                        "н.д. микровыступ","вмятина","мех.повреждение",
                        "риска","царапина с волчком"]
  loadingPredict = true;

  @ViewChild("layer1", { static: false }) layer1Canvas: any;
  private context: any;
  private layer1CanvasElement: any;
  selectedId = 0;
  @ViewChild('imageElement') imageElement: any;
  @ViewChild('canvasElement') canvasElement: any;

  printBox() {
    const image = this.imageElement.nativeElement;
    const canvas = this.canvasElement.nativeElement;
    const ctx = canvas.getContext('2d');

    // Установите размеры холста равными размерам изображения
    canvas.width = image.width;
    canvas.height = image.height;

    for (const item of this.points) {
      ctx.strokeStyle = 'red';
      ctx.lineWidth = 2;
      ctx.strokeRect(10, 10, 200, 200);

      // Отобразите изображение и холст
      image.onload = () => {
        ctx.drawImage(image, 0, 0);
      };
    }
  }
  // Нарисуйте прямоугольник на холсте


  myForm : FormGroup = new FormGroup({
    "imageUpload": new FormControl(),
    "radius": new FormControl(0.07, [Validators.min(0.1)])
  });
  constructor(private http: HttpClient) {
  }

  ngOnInit() {

  }


  calculateCoordinatesRadial(radius:any, x:any, y:any) {
    debugger;
    const radialCoordinate = Math.sqrt(x**2 + y**2) - radius;
    return radialCoordinate;
  }

  calculateCoordinatesaxial(radius:any, x:any, y:any) {
    const axialCoordinate = Math.atan2(y, x);

    return axialCoordinate;
  }

  onFileSelected(event:any) {
    const file:File = event.target.files[0];

    if (file) {

      const reader = new FileReader();
      reader.onload = (e: any) => {
        this.selectedImage = e.target.result;
      };
      reader.readAsDataURL(file);
      reader.onload = event => {
        this.image = new Image();
        this.image.src = reader.result;
        this.image.onload = () => {
          this.imgWidth = this.image.width;
          this.imgHeight = this.image.height;
          this.showImage();
        };
      };

      const formData = new FormData();

      formData.append("file", file);

      this.loadingPredict = true;
      const upload$ = this.http.post("http://reter34erwd.duckdns.org:6788/process-image", formData)
        .subscribe(values =>{
          let defects = [];
          this.loadingPredict = false;
          let i=0;
            // @ts-ignore
            for (const item of values) {
            i++;
            const defect = new Defect();
            defect.id = i;
            defect.X1 = item.x;
            defect.Y1 = item.y;
            defect.W = item.w;
            defect.H = item.h;
            defect.className = this.defectDesc[item.class_num];
            defect.classType = Math.round(item.class_num);
            defects.push(defect);
          }
          this.points = defects;
          this.showImage();
        },
          error => {
            this.loadingPredict = false;
          })
    }
  }


  showImage() {
    this.layer1CanvasElement = this.layer1Canvas.nativeElement;
    this.context = this.layer1CanvasElement.getContext("2d");
    this.layer1CanvasElement.width = this.imgWidth;
    this.layer1CanvasElement.height = this.imgHeight;
    this.context.drawImage(this.image, 0, 0, this.imgWidth, this.imgHeight);
    let parent = this;
    this.layer1CanvasElement.addEventListener("mousemove", function(e:any) {
      let x = 200;
      let y = 300;
      let w = 400;
      let h = 500;

      if (
        x <= e.clientX &&
        e.clientX <= x + w &&
        y <= e.clientY &&
        e.clientY <= y + h
      )
        parent.drawRect();
      else parent.drawRect();
    });

    this.drawRect();
  }

  drawRect(color = "black") {

    this.points.forEach( x=> {
      this.context.beginPath();
      this.context.rect(x.X1, x.Y1, x.W, x.H);
      this.context.lineWidth = 5;
      if (x.id == this.selectedId) {
        this.context.strokeStyle = 'red';
      } else {
        this.context.strokeStyle = color;
      }
      this.context.stroke();
    })

  }

  showSelected(point: Defect) {
    debugger;
    this.selectedId = point.id;
    this.showImage();
  }

  showLeave(point: Defect) {
    debugger;
    this.selectedId = 0;
    this.showImage();
  }

  PreparedX(point: Defect) {
   return  point.X1 + (point.W /2)

  }

  PreparedY(point: Defect) {
    return  point.Y1 + (point.H /2)
  }
}


class Defect {
  id = 0
  X1: number = 0;
  Y1: number = 0;
  W: number = 0;
  H: number = 0;

  className = ""
  classType = -1
}
