<script setup>
import AppHeading from "../components/AppHeading.vue";
import AppHeader from "../components/AppHeader.vue";
import AppPill from "../components/AppPill.vue";
</script>

<template>
  <AppHeader
    name="Jason Kolenosky"
    title="Software Developer"
    location="Richmond, BC"
  />
  <AppHeading title="Projects" />
  <AppPill title="Writing Prompt Generator" url="/writing-prompts" />
</template>

<style scoped></style>
