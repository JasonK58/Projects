<script setup lang="ts">
defineProps<{
  title: string;
  url: string;
}>();
</script>

<template>
  <div class="pill">
    <a :href="url" target="_blank" class="title">{{ title }}</a>
  </div>
</template>

<style scoped>
.pill {
  display: flex;
  border: 3px solid black;
  border-radius: 5px;
  background-color: #f79e2f;
  margin: 0 0 var(--text-padding) var(--text-padding);
  float: left;
}

.pill:hover {
  cursor: pointer;
}

.title {
  padding: 7px;
  font-weight: 550;
  text-decoration: none;
  color: black;
}
</style>
