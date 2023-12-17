import { Routes } from '@angular/router';
import {HomeComponentComponent} from "./home-component/home-component.component";
import {AdminPaneleComponentComponent} from "./admin-panele-component/admin-panele-component.component";

export const routes: Routes = [
  { path: "", component: HomeComponentComponent },
  { path: "verification", component: HomeComponentComponent },
  { path: "admin", component: AdminPaneleComponentComponent },
];
