<script setup lang="ts">
import AppHeader from '@/components/AppHeader.vue'
import Logo from '@/assets/books.svg'
import DropdownMenu from '@/components/dropdownMenu.vue'
import { ref } from 'vue'
import TextInput from '@/components/TextInput.vue'

const maxLength = 20
const maxInputs = 5
const selectedGenre = ref('')
const textInputs = ref([''])
</script>

<template>
  <AppHeader msg="Writing Prompt Generator" :logo="Logo" />

  <DropdownMenu
    v-model="selectedGenre"
    :options="['horror', 'comedy', 'mystery']"
    placeholder-option="Select a genre"
  />

  <div><TextInput :max-length="maxLength" :max-inputs="maxInputs" v-model="textInputs" /></div>
</template>
