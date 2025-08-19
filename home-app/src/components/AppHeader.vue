<script setup lang="ts">
import foo from "../assets/images/location-pin.svg";

defineProps<{
  name: string;
  title: string;
  location: string;
}>();
</script>

<template>
  <header>
    <div id="name">
      <span>{{ name }}</span>
    </div>
    <div id="title">
      <span>{{ title }}</span>
    </div>
    <hr />
    <div id="location">
      <div>
        <img :src="foo" alt="location-pin" />
        <span>{{ location }}</span>
      </div>
    </div>
  </header>
</template>

<style scoped>
header {
  --text-padding: 15px;
  background-color: #f6dea0;
  display: flex;
  flex-wrap: wrap;
  color: black;
}

#name {
  float: left;
  width: 50%;
  height: 100%;
  text-align: left;
  font-size: 3rem;
}

#name span {
  margin-left: var(--text-padding);
}

#title {
  float: right;
  width: 50%;
  font-size: 2rem;
  display: flex;
  align-items: flex-end;
  justify-content: flex-end;
}

#title span {
  margin-right: var(--text-padding);
  height: auto;
}

hr {
  width: 100%;
  height: 1px;
  border: 0;
  border-bottom: 3px solid black;
  padding: 0;
  margin: 0;
}

#location {
  font-size: 2rem;
}

#location div img {
  margin-left: var(--text-padding);
  margin-right: 3px;
  width: 2.5vh;
}

@media screen and (max-width: 720px) {
  #name {
    font-size: 2rem;
  }

  #title {
    font-size: 1.5rem;
  }

  #location {
    font-size: 1.5rem;
  }
}

@media screen and (max-width: 510px) {
  header {
    --text-padding: 0px;
  }
  #name,
  #title,
  #location {
    width: 100%;
    float: none;
    text-align: center;
    display: block;
  }
}
</style>
