<script setup lang="ts">
defineProps<{
  msg: string
  logo?: string
}>()
</script>

<template>
  <div class="header">
    <img v-if="logo" alt="logo" class="logo" :src="logo" width="300" height="125" />
    <h1>{{ msg }}</h1>
  </div>
</template>

<style scoped>
.header {
  width: 40%;
  height: 100%;
  top: 1em;
  margin-left: 33%;
}

.header img {
  float: left;
  width: 10rem;
  height: 10rem;
}

.header h1 {
  text-align: left;
  font-size: 3.2em;
  margin-left: 4em;
}
</style>
