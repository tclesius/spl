<template>
  <div class="flex items-center justify-between px-4 py-2 bg-gray-900 text-white">
    <div class="flex items-center">
      <span class="text-lg font-semibold">spl admin</span>
    </div>
    <div class="relative">
      <button @click="toggleDropdown" class="text-white focus:outline-none">
        User
      </button>
      <div
          v-if="dropdownOpen"
          class="absolute right-0 mt-2 w-48 bg-white border border-gray-300 rounded shadow-lg"
      >
        <ul>
          <li @click="logout" class="cursor-pointer px-4 py-2 hover:bg-gray-100">
            Logout
          </li>
          <li @click="changePassword" class="cursor-pointer px-4 py-2 hover:bg-gray-100">
            Change Password
          </li>
        </ul>
      </div>
    </div>
  </div>
</template>

<script setup>
import {ref} from 'vue';

const dropdownOpen = ref(false);

const toggleDropdown = () => {
  dropdownOpen.value = !dropdownOpen.value;
};

const logout = () => {
  // Implement your logout logic here
};

const changePassword = () => {
  // Implement your change password logic here
};
</script>

<style scoped>
/* Styles for your top navigation bar */
</style>
