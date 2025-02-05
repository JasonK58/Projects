<script setup lang="ts">
defineProps<{
  msg: string
}>()
</script>

<template>
  <div class="header">
    <img alt="logo" class="logo" src="@/assets/books.svg" width="300" height="125" />
    <h1>{{ msg }}</h1>
  </div>
</template>

<style scoped>
.header {
  width: 33rem;
  border: 1px solid white;
  margin: 0 auto;
  margin-top: 1rem !important;
  padding: 0;
  height: 100vh;
}
.header img {
  float: left;
  width: 10rem;
  height: 10rem;
}

.header h1 {
  text-align: left;
  margin-top: 3rem;
}
</style>
