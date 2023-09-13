<template>
  <div class="text-sm font-inter space-y-2">
    <label :for="inputId" class="block text-black">{{ labelText }}</label>
    <div class="relative">
      <input
          :type="inputType"
          :id="inputId"
          :name="inputId"
          class="bg-gray-100 rounded border-2 border-transparent focus:outline-none px-4 py-2 w-full pr-10"
          :placeholder="placeholderText"
          :value="modelValue"
          @input="$emit('update:modelValue', $event.target.value)"
      >
      <button v-if="props.inputType === 'password'" @click="togglePasswordVisibility"
              type="button"
              class="absolute right-2 top-1/2 transform -translate-y-1/2 font-inter text-xs">
        {{ showPassword ? 'Hide' : 'Show' }}
      </button>
    </div>
  </div>
</template>

<script setup>
import {computed, ref, defineProps} from 'vue';

const props = defineProps({
  labelText: String,
  placeholderText: String,
  inputType: String,
  modelValue: String,
});

const inputId = `input-${Math.random().toString(36).substring(7)}`;

const showPassword = ref(false);

const inputType = computed(() => showPassword.value ? 'text' : props.inputType);

const togglePasswordVisibility = () => {
  showPassword.value = !showPassword.value;
};

</script>

<style scoped>
/* Define text-red style here */
</style>
