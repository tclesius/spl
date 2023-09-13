<template>
  <div class="bg-dew-gray text-black font-semibold rounded-md py-1 px-2 items-center inline-block">
    <span>{{ name }}: {{ value }}</span>
  </div>
</template>

<script setup>
import {defineProps} from 'vue';

const props = defineProps({
  name: String,
  value: Number,
});
</script>

<style scoped>
/* Add any additional styling or adjustments here */
</style>
