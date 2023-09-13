<template>
  <button class="bg-black hover:bg-ash-gray text-sm text-white font-inter font-medium py-1 rounded"
          @click="$emit('click')">
    <slot/>
  </button>
</template>

<script setup>
</script>

<style scoped>
/* You can add custom styles here if needed */
</style>
