import { describe, it, expect } from 'vitest'

import { sanitizeString } from '@/composables/sanitize.ts'

describe('sanitize.ts', () => {
  it('Sanitizes input by removing whitespace and commas', async () => {
    const inputString = 'Testing, Testing'
    const expectedString = 'TestingTesting'

    const result = sanitizeString(inputString)

    expect(result).toBe(expectedString)
  })
})
