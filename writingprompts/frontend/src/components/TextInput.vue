<script setup lang="ts">
import { sanitizeString } from '@/composables/sanitize.ts'

defineProps<{
  maxLength: number
  maxInputs: number
}>()

const textInputs = defineModel<string[]>({ default: [''] })

function sanitizeInput(event: Event, index: number) {
  const target = event.target as HTMLInputElement
  textInputs.value[index] = sanitizeString(target.value)
}

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
      :value="textInputs[index]"
      @input="sanitizeInput($event, index)"
      :placeholder="`max ${maxLength} characters`"
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
  margin-left: 2px;
}

.remove-field {
  background-color: lightcoral;
  margin-left: 4px;
  margin-right: 2px;
}

@media screen and (max-width: 479px) {
  .input-element {
    width: 95%;
  }

  .input-field {
    width: 75%;
  }
}

@media (prefers-color-scheme: dark) {
  .field-button {
    color: black;
  }
}
</style>
