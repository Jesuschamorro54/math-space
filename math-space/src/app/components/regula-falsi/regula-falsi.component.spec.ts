import { ComponentFixture, TestBed } from '@angular/core/testing';

import { RegulaFalsiComponent } from './regula-falsi.component';

describe('RegulaFalsiComponent', () => {
  let component: RegulaFalsiComponent;
  let fixture: ComponentFixture<RegulaFalsiComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      declarations: [ RegulaFalsiComponent ]
    })
    .compileComponents();
  });

  beforeEach(() => {
    fixture = TestBed.createComponent(RegulaFalsiComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
