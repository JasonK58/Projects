import { ref } from 'vue'

type RequestBody = {
  genre: string
  keywords: string[]
}

export function useApi() {
  const results = ref(null)
  const error = ref('')

  const makePostRequest = async (url: string, body: RequestBody) => {
    const requestOptions = {
      method: 'POST',
      headers: { 'content-type': 'application/json' },
      body: JSON.stringify(body),
    }
    try {
      results.value = await (await fetch(url, requestOptions)).json()
    } catch (err) {
      error.value = err as string
    }
  }

  return {
    makePostRequest,
    results,
    error,
  }
}
