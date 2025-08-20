<script setup lang="ts"></script>

<template>
  <hr />
</template>

<style scoped>
hr {
  height: 1px;
  border: 0;
  border-bottom: 2px solid black;
  margin: -5px 0 var(--text-padding) var(--text-padding);
  width: 50%;
}
@media screen and (max-width: 510px) {
  hr {
    margin-bottom: 10px;
  }
}
</style>
