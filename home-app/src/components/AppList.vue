<script setup lang="ts">
import { computed } from "vue";

const { listValues } = defineProps<{ listValues: string[] }>();

const combinedValues = computed(() => listValues.join(", "));
</script>

<template>
  <p>{{ combinedValues }}</p>
</template>

<style scoped>
p {
  margin-top: 0;
  margin-left: var(--text-padding);
  clear: both;
}
</style>
