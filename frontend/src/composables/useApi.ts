import { ref } from 'vue'

type RequestBody = {
  genre: string
  keywords: string[]
}

export function useApi() {
  const response = ref('')
  const error = ref('')

  const makePostRequest = async (url: string, body: RequestBody) => {
    if (error.value) {
      error.value = ''
    }

    const requestOptions = {
      method: 'POST',
      headers: { 'content-type': 'application/json' },
      body: JSON.stringify(body),
    }

    try {
      const result = await fetch(url, requestOptions)
      if (result.status !== 200) {
        error.value = (await result.json())['detail']
      } else {
        response.value = (await result.json())['msg']
      }
    } catch (err) {
      error.value = err as string
    }
  }

  return {
    makePostRequest,
    response,
    error,
  }
}
