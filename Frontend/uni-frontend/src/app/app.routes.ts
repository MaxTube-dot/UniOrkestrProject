import { Routes } from '@angular/router';
import {HomeComponentComponent} from "./home-component/home-component.component";
import {AdminPaneleComponentComponent} from "./admin-panele-component/admin-panele-component.component";
import {AboutComponent} from "./about/about.component";
import {StatisticComponentComponent} from "./statistic-component/statistic-component.component";

export const routes: Routes = [
  { path: "", component: HomeComponentComponent },
  { path: "verification", component: HomeComponentComponent },
  { path: "admin", component: AdminPaneleComponentComponent },
  { path: "about", component: AboutComponent },
  { path: "statistics", component: StatisticComponentComponent },
];
