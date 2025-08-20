<script setup lang="ts">
import SectionBreak from "./SectionBreak.vue";

defineProps<{
  title: string;
}>();
</script>

<template>
  <div class="heading-title">
    {{ title }}
  </div>
  <SectionBreak />
</template>

<style scoped>
.heading-title {
  font-size: 2rem;
  color: black;
  text-align: left;
  padding-left: var(--text-padding);
  margin-top: 1rem;
  clear: both;
}
</style>
