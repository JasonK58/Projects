<script setup lang="ts">
import AppHeader from '@/components/AppHeader.vue'
import Logo from '@/assets/books.svg'
import DropdownMenu from '@/components/dropdownMenu.vue'
import { ref } from 'vue'
import TextInput from '@/components/TextInput.vue'
import { useApi } from '@/composables/useApi.ts'
import SubmitButton from '@/components/SubmitButton.vue'

const maxLength = 20
const maxInputs = 5
const apiUrl = import.meta.env.VITE_API_URL
const selectedGenre = ref('')
const textInputs = ref([''])
const displayText = ref('')
const { makePostRequest, response, error } = useApi()

async function makeRequest() {
  await makePostRequest(apiUrl + 'writingprompt', {
    genre: selectedGenre.value,
    keywords: textInputs.value,
  })

  displayText.value = error.value ? '' : response.value
}
</script>

<template>
  <div id="header_wrapper">
    <AppHeader msg="Writing Prompt Generator" :logo="Logo" />
  </div>

  <div id="settings_wrapper">
    <DropdownMenu
      id="genre_dropdown"
      v-model="selectedGenre"
      :options="['horror', 'comedy', 'mystery']"
      placeholder-option="Select a genre"
    />

    <div id="text_inputs">
      <span>Provide zero to five keywords to use:</span>
      <TextInput :max-length="maxLength" :max-inputs="maxInputs" v-model="textInputs" />
    </div>
  </div>

  <div id="submit_button">
    <SubmitButton msg="Generate Writing Prompt" @click="makeRequest()" />
  </div>
  <div class="result">{{ displayText }}</div>
  <div class="result" id="error">{{ error }}</div>
</template>

<style scoped>
#header_wrapper {
  width: 100%;
  height: 14em;
  margin-top: 1em;
}

#text_inputs {
  margin-top: 1rem;
  margin-bottom: 1rem;
  text-align: center;
}

#text_inputs span {
  font-size: 1.5em;
  display: flex;
  justify-content: center;
}

#submit_button {
  display: flex;
  width: 100%;
  justify-content: center;
}

.result {
  margin-top: 1em;
  font-size: 1.5em;
  width: 90%;
  margin-left: auto;
  margin-right: auto;
  text-align: center;
}

#error {
  color: red;
}
</style>
