<template>
  <div class="text-sm font-inter space-y-2">
    <label :for="selectId" class="block text-black">{{ labelText }}</label>
    <div class="relative">
      <select
          :id="selectId"
          :name="selectId"
          class="bg-gray-100 rounded border-2 border-transparent focus:outline-none px-4 py-2 w-full pr-10"
          @input="$emit('update:selectedValue', $event.target.value)"
          :value="selectedValue"
      >
        <option disabled class="text-gray-100" value="">{{ joinedOptions }}</option>
        <option v-for="option in options" :key="option.value" :value="option.value">{{ option.label }}</option>
      </select>
    </div>
  </div>
</template>

<script setup>
import {computed, defineProps, ref} from 'vue';

const props = defineProps({
  labelText: String,
  options: Array,
  selectedValue: String,
});

const selectId = `select-${Math.random().toString(36).substring(7)}`;

const joinedOptions = computed(() => {
  return props.options.slice(0, 3).map(option => option.label).join(', ') + '...';
});

</script>

<style scoped>
/* Add any additional styling or adjustments here */
</style>
