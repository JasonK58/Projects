import { describe, it, vi, expect } from 'vitest'
import type { Mock } from 'vitest'
import { useApi } from '../useApi'

describe('useApi.ts', () => {
  const url = 'http://test'
  const requestBody = { genre: 'comedy', keywords: ['cop', 'buddy'] }
  const mockResponse = { msg: 'success' }
  global.fetch = vi.fn(() =>
    Promise.resolve({
      json: () => Promise.resolve(mockResponse),
    }),
  ) as Mock

  it('makes a valid post request to the API', async () => {
    const { makePostRequest, results, error } = useApi()
    await makePostRequest(url, requestBody)

    expect(results.value).toEqual(mockResponse)
    expect(error.value).toEqual('')
  })
})
