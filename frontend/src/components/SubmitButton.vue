<script setup lang="ts">
defineProps({
  msg: String,
})
</script>

<template>
  <div id="submit">{{ msg }}</div>
</template>

<style scoped>
#submit {
  font-weight: bold;
  border: 2px solid black;
  border-radius: 5px;
  cursor: pointer;
  text-align: center;
  width: 15em;
  background-color: #55c2da;
}
</style>
