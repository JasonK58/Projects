<script setup lang="ts">
defineProps<{
  options: string[]
}>()

const selectedOption = defineModel()
</script>

<template>
  <select class="select" v-model="selectedOption">
    <option value="">Select a genre</option>
    <option class="option" v-for="option in options" :value="option" :key="option">
      {{ option }}
    </option>
  </select>
</template>

<style scoped>
select {
  height: 3rem;
  width: 12rem;
  border: 1px solid black;
  font-size: 22px;
}
</style>
