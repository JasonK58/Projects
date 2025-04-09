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
    <div id="dropdown">
      <DropdownMenu
        v-model="selectedGenre"
        :options="['horror', 'comedy', 'mystery']"
        placeholder-option="Select a genre"
      />
    </div>

    <div id="text_inputs">
      <span>Provide zero to five keywords to use:</span>
      <TextInput :max-length="maxLength" :max-inputs="maxInputs" v-model="textInputs" />
    </div>
  </div>

  <div style="clear: both"></div>

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
#settings_wrapper {
  width: 50%;
  margin-left: 35%;
  height: 100%;
}

#dropdown {
  width: 49%;
  margin-bottom: 1em;
}

#text_inputs {
  margin-bottom: 4em;
}

#text_inputs span {
  font-size: 1.5em;
}

#submit_button {
  width: 20%;
  margin-left: 35%;
}

.result {
  margin-top: 1em;
  width: 50%;
  margin-left: 25%;
  font-size: 1.5em;
}

#error {
  color: red;
}
</style>
