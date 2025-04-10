<script setup lang="ts">
defineProps<{
  msg: string
  logo?: string
}>()
</script>

<template>
  <div class="header">
    <img v-if="logo" alt="logo" class="logo" :src="logo" width="300" height="125" />
    <span>{{ msg }}</span>
  </div>
</template>

<style scoped>
.header {
  top: 1rem;
  margin-left: 1rem;
  height: 8rem;
  display: flex;
  align-items: center;
  gap: 1rem;
}

.header img {
  width: 8rem;
  height: auto;
}

.header span {
  text-align: left;
  font-size: 3.2em;
}

@media screen and (max-width: 479px) {
  .header span {
    font-size: 1.9rem;
  }
}
</style>
