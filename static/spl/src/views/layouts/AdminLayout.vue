<template>
  <div class="flex h-screen">
    <div class="flex-none max-w-[12em] overflow-y-auto bg-dew-gray">
      <SidebarComponent/>
    </div>
    <div class="flex-grow">
      <NavBarComponent/>
      <router-view/>
    </div>
  </div>
</template>

<script setup>
import SidebarComponent from "@/components/SidebarComponent.vue";
import NavBarComponent from "@/components/NavBarComponent.vue";
</script>

<style scoped>
</style>
