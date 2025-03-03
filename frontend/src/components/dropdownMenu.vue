<script setup lang="ts">
defineProps<{
  placeholderOption?: string
  options: string[]
}>()

const selectedOption = defineModel<string>()
</script>

<template>
  <div>
    <select class="select" v-model="selectedOption">
      <option v-if="placeholderOption" value="">{{ placeholderOption }}</option>
      <option class="option" v-for="option in options" :value="option" :key="option">
        {{ option }}
      </option>
    </select>
  </div>
</template>

<style scoped>
select {
  height: 3rem;
  width: 100%;
  border: 1px solid black;
  font-size: 22px;
}
</style>
