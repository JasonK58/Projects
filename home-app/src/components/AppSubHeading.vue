<script setup lang="ts">
defineProps<{ title: string }>();
</script>

<template>
  <h3>{{ title }}</h3>
</template>

<style scoped>
h3 {
  margin-left: var(--text-padding);
  margin-bottom: 0;
}
</style>
