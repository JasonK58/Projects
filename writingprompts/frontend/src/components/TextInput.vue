<script setup lang="ts">
defineProps<{
  maxLength: number
  maxInputs: number
}>()

const textInputs = defineModel<string[]>({ default: [''] })

function AddInputField(value: string) {
  if (value) {
    textInputs.value.push('')
  }
}

function RemoveInputField(index: number) {
  textInputs.value.splice(index, 1)
}
</script>

<template>
  <div class="input-element" v-for="(_, index) in textInputs" :key="index">
    <input
      class="input-field"
      type="text"
      :maxlength="maxLength"
      @keydown.space.prevent
      v-model="textInputs[index]"
    />
    <div class="image-container">
      <div
        class="field-button remove-field"
        v-if="index < textInputs.length - 1 || (index == textInputs.length - 1 && index > 0)"
        @click="RemoveInputField(index)"
      >
        -
      </div>
      <div
        class="field-button add-field"
        v-if="index == textInputs.length - 1 && maxInputs > index + 1"
        @click="AddInputField(textInputs[index])"
      >
        +
      </div>
    </div>
  </div>
</template>

<style scoped>
.input-element {
  display: table;
  margin-left: auto;
  margin-right: auto;
  margin-bottom: 0.5rem;
}

.input-field {
  font-size: 24px;
  border: 2px solid black;
  border-radius: 5px;
  float: left;
}

.image-container {
  height: 2rem;
  display: flex;
  float: left;
  margin-left: 0.2rem;
  margin-top: 0.05rem;
  object-fit: contain;
  cursor: pointer;
}

.field-button {
  border: 2px solid black;
  border-radius: 5px;
  width: 2rem;
  text-align: center;
  line-height: 1.6rem;
  font-weight: bold;
  font-size: 1.5rem;
}

.add-field {
  background-color: lightgreen;
}

.remove-field {
  background-color: lightcoral;
  margin-right: 2px;
}
</style>
