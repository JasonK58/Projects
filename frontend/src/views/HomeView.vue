<script setup lang="ts">
import AppHeader from '@/components/AppHeader.vue'
import Logo from '@/assets/books.svg'
import DropdownMenu from '@/components/dropdownMenu.vue'
import { ref } from 'vue'
import TextInput from '@/components/TextInput.vue'
import { useApi } from '@/composables/useApi.ts'

const maxLength = 20
const maxInputs = 5
const apiUrl = import.meta.env.VITE_API_URL
const selectedGenre = ref('')
const textInputs = ref([''])
const { makePostRequest, results, error } = useApi()
</script>

<template>
  <AppHeader msg="Writing Prompt Generator" :logo="Logo" />

  <DropdownMenu
    v-model="selectedGenre"
    :options="['horror', 'comedy', 'mystery']"
    placeholder-option="Select a genre"
  />

  <TextInput :max-length="maxLength" :max-inputs="maxInputs" v-model="textInputs" />

  <button
    @click="
      makePostRequest(apiUrl + 'writingprompt', {
        genre: selectedGenre,
        keywords: textInputs,
      })
    "
  >
    Generate Writing Prompt</button
  ><br />
  <span>Result: {{ results }}</span
  ><br />
  <span>Error: {{ error }}</span>
</template>
