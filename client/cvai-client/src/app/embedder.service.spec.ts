import { TestBed } from '@angular/core/testing';

import { EmbedderService } from './embedder.service';

describe('EmbedderService', () => {
  beforeEach(() => TestBed.configureTestingModule({}));

  it('should be created', () => {
    const service: EmbedderService = TestBed.get(EmbedderService);
    expect(service).toBeTruthy();
  });
});
