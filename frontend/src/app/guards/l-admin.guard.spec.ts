import { TestBed } from '@angular/core/testing';

import { LAdminGuard } from './l-admin.guard';

describe('LAdminGuard', () => {
  let guard: LAdminGuard;

  beforeEach(() => {
    TestBed.configureTestingModule({});
    guard = TestBed.inject(LAdminGuard);
  });

  it('should be created', () => {
    expect(guard).toBeTruthy();
  });
});
