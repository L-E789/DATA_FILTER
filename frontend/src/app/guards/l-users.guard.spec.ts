import { TestBed } from '@angular/core/testing';

import { LUsersGuard } from './l-users.guard';

describe('LUsersGuard', () => {
  let guard: LUsersGuard;

  beforeEach(() => {
    TestBed.configureTestingModule({});
    guard = TestBed.inject(LUsersGuard);
  });

  it('should be created', () => {
    expect(guard).toBeTruthy();
  });
});
