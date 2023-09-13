<template>
  <transition name="slide-fade">
    <div v-if="showAlert" class="font-inter">
      <div :class="alertClasses" class="p-4 flex items-center relative text-sm rounded-s">
        <div class="flex items-center">
          <p class="font-bold">{{ title }}:</p>
          <p class="ml-2">{{ message }}</p>
          <button @click="closeAlert">
            <svg class="fill-current h-4 w-4" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 20 20">
              <title>Close</title>
              <path
                  d="M14.348 14.849a1.2 1.2 0 0 1-1.697 0L10 11.819l-2.651 3.029a1.2 1.2 0 1 1-1.697-1.697l2.758-3.15-2.759-3.152a1.2 1.2 0 1 1 1.697-1.697L10 8.183l2.651-3.031a1.2 1.2 0 1 1 1.697 1.697l-2.758 3.152 2.758 3.15a1.2 1.2 0 0 1 0 1.698z"/>
            </svg>
          </button>
        </div>
      </div>
      <div class="w-full h-1 bg-gray-300 overflow-y-hidden rounded-b">
        <div :style="{ width: timingBarWidth }" class="h-full bg-green-500"></div>
      </div>
    </div>
  </transition>
</template>


<script setup>
import {onBeforeUnmount, onMounted, ref} from 'vue';

const props = defineProps({
  type: String,
  title: String,
  message: String,
  autoCloseDuration: Number, // Duration in seconds
});

const showAlert = ref(true);
const timingBarWidth = ref('0%');
let timer; // Define the timer variable
const interval = 10; // Update interval in milliseconds

const alertClasses = {
  'bg-gray-100': props.type === 'error',
  'text-black': props.type === 'error',
};

const closeAlert = () => {
  showAlert.value = false;
  clearInterval(timer); // Clear the timer interval when the alert is closed
};

onMounted(() => {
  if (props.autoCloseDuration > 0) {
    const totalSteps = props.autoCloseDuration * 1000 / interval;

    let step = 0;
    timer = setInterval(() => {
      step++;
      timingBarWidth.value = `${(step / totalSteps) * 100}%`;

      if (step >= totalSteps) {
        clearInterval(timer);
        closeAlert();
      }
    }, interval);
  }
});

onBeforeUnmount(() => {
  clearInterval(timer); // Clear the interval when the component is unmounted
});
</script>

<style scoped>
/* ... your existing styles ... */

.slide-fade-enter-active, .slide-fade-leave-active {
  transition: all 0.3s ease;
}

.slide-fade-enter, .slide-fade-leave-to {
  opacity: 0;
  transform: translateX(20px);
}
</style>
