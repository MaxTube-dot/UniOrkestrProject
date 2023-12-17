import { ComponentFixture, TestBed } from '@angular/core/testing';

import { AdminPaneleComponentComponent } from './admin-panele-component.component';

describe('AdminPaneleComponentComponent', () => {
  let component: AdminPaneleComponentComponent;
  let fixture: ComponentFixture<AdminPaneleComponentComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      imports: [AdminPaneleComponentComponent]
    })
    .compileComponents();
    
    fixture = TestBed.createComponent(AdminPaneleComponentComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
