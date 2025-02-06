<script setup lang="ts">
import AppHeader from '@/components/AppHeader.vue'
import Logo from '@/assets/books.svg'
import DropdownMenu from '@/components/dropdownMenu.vue'
import { ref } from 'vue'

const selectedOption = ref('')
</script>

<template>
  <AppHeader msg="Writing Prompt Generator" :logo="Logo" />

  <DropdownMenu v-model="selectedOption" :options="['horror', 'comedy', 'mystery']" />
</template>
