<script setup>
import {ref} from 'vue';
import Input from "@/components/InputComponent.vue";

const props = defineProps({
  labelText: String,
  inputId: String,
  modelValue: Boolean
});

const emits = defineEmits(['update:modelValue']);

// Generate a random number as a unique identifier
const uniqueId = ref(Math.random().toString(36).substring(7));
</script>

<template>
  <div class="font-inter flex items-center space-x-2">
    <input
        type="checkbox"
        :id="`input-${uniqueId}`"
        :name="`input-${uniqueId}`"
        class="outline-none border-0 text-primary accent-ash-gray focus:ring-primary h-4 w-4"
        :checked="modelValue"
        @input="$emit('update:modelValue', $event.target.checked)"
    >
    <label :for="inputId" class="font-medium text-sm ">{{ labelText }}</label>
  </div>
</template>

<style scoped>

</style>
