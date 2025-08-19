<script setup lang="ts">
defineProps<{
  title: string;
}>();
</script>

<template>
  <div class="heading-title">{{ title }}</div>
</template>

<style scoped>
.heading-title {
  font-size: 2rem;
  width: 100%;
  padding: 1rem 0 1rem 0;
  color: black;
}
</style>
