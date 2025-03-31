import { describe, it, vi, expect } from 'vitest'
import type { Mock } from 'vitest'
import { useApi } from '../useApi'

describe('useApi.ts', () => {
  const url = 'https://test.com'
  const requestBody = { genre: 'comedy', keywords: ['cop', 'buddy'] }
  const mockSuccessResponse = { msg: 'success' }
  const mockErrorResponse = { detail: 'error' }
  global.fetch = vi.fn(() =>
    Promise.resolve({
      ok: true,
      status: 200,
      json: async () => Promise.resolve(mockSuccessResponse),
    }),
  ) as Mock

  it('makes a valid post request to the API', async () => {
    global.fetch = vi.fn(() =>
      Promise.resolve({
        ok: true,
        status: 200,
        json: async () => Promise.resolve(mockSuccessResponse),
      }),
    ) as Mock

    const { makePostRequest, response, error } = useApi()
    await makePostRequest(url, requestBody)

    expect(response.value).toEqual(mockSuccessResponse.msg)
    expect(error.value).toEqual('')
  })

  it('returns an error message if the request is not successful', async () => {
    global.fetch = vi.fn(() =>
      Promise.resolve({
        ok: true,
        status: 422,
        json: async () => Promise.resolve(mockErrorResponse),
      }),
    ) as Mock

    const { makePostRequest, response, error } = useApi()
    await makePostRequest(url, requestBody)

    expect(error.value).toEqual(mockErrorResponse.detail)
    expect(response.value).toEqual('')
  })
})
