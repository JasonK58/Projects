<script setup lang="ts">
import AppHeader from '@/components/AppHeader.vue'
import Logo from '@/assets/books.svg'
import DropdownMenu from '@/components/dropdownMenu.vue'
import { ref } from 'vue'

const selectedGenre = ref('')
</script>

<template>
  <AppHeader msg="Writing Prompt Generator" :logo="Logo" />

  <DropdownMenu
    v-model="selectedGenre"
    :options="['horror', 'comedy', 'mystery']"
    placeholder-option="Select a genre"
  />
</template>
