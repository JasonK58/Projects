<script setup lang="ts">
defineProps<{
  placeholderOption?: string
  options: string[]
}>()

const selectedOption = defineModel<string>()
</script>

<template>
  <div class="select-wrapper">
    <select class="select" v-model="selectedOption">
      <option v-if="placeholderOption" value="">{{ placeholderOption }}</option>
      <option class="option" v-for="option in options" :value="option" :key="option">
        {{ option }}
      </option>
    </select>
  </div>
</template>

<style scoped>
.select-wrapper {
  display: flex;
}

.select {
  font-size: 2rem;
  background-color: #f9f9f9;
  border-radius: 5px;
  margin: auto;
  width: 20rem;
}
</style>
