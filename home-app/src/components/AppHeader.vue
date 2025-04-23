<script setup></script>

<template>
  <header>Jason Kolenosky</header>
</template>

<style scoped>
header {
  font-size: 4rem;
  text-align: center;
  background-color: #f6dea0;
}

@media screen and (max-width: 991px) {
  header {
    font-size: 3rem;
  }
}

@media screen and (max-width: 767px) {
  header {
    font-size: 2rem;
  }
}

@media screen and (max-width: 479px) {
  header {
    font-size: 2rem;
  }
}

@media (prefers-color-scheme: dark) {
  header {
    color: black;
  }
}
</style>
