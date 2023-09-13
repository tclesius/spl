<template>
  <div :style="spinnerContainerStyles">
    <div class="spinner" :style="spinnerStyles"></div>
  </div>
</template>

<script setup>
const props = defineProps({
  size: {
    type: String,
    default: "1.25rem",
  },
});

const spinnerStyles = {
  width: `${props.size}`,
  height: `${props.size}`,
};
const spinnerContainerStyles = {
  display: "flex",
  justifyContent: "center",
  alignItems: "center",
}

</script>

<style scoped>
.spinner {
  border: 4px solid #ffffff;
  border-top: 4px solid #000000;
  border-radius: 50%;
  animation: spin 1s linear infinite;
}

@keyframes spin {
  0% {
    transform: rotate(0deg);
  }
  100% {
    transform: rotate(360deg);
  }
}
</style>