<script setup>
import AppHeading from "../components/AppHeading.vue";
import AppHeader from "../components/AppHeader.vue";
import AppPill from "../components/AppPill.vue";
import AppSubHeading from "../components/AppSubHeading.vue";
import AppList from "../components/AppList.vue";
</script>

<template>
  <AppHeader
    name="Jason Kolenosky"
    title="Software Developer"
    location="Richmond, BC"
  />
  <AppHeading title="Projects" />
  <AppPill title="Writing Prompt Generator" url="/writing-prompts" />

  <AppHeading title="Skills" />
  <AppSubHeading title="LANGUAGES/LIBRARIES:" />
  <AppList
    :listValues="[
      'C#',
      'Linq',
      'PowerShell',
      'Python',
      'R',
      'React',
      'SQL',
      'Typescript',
    ]"
  />
</template>

<style scoped></style>
