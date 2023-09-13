<template>
  <div class="font-inter sidebar max-w-[12em] bg-dew-gray">
    <div v-for="(category, index) in categories" :key="index">
      <div
          class="font-bold category-header cursor-pointer flex justify-between items-center pt-10 py-2 px-4"
          @click="toggleCategory(category)"
      >
        {{ category.name }}
      </div>
      <ul v-if="category.expanded" class="text-sm">
        <li v-for="(subCategory, subIndex) in category.subcategories" :key="subIndex">
          <router-link :to="subCategory.link"
                       class="block py-1 px-4 text-ash-gray hover:bg-gray-100 transition "
                       active-class="font-bold">
            {{ subCategory.name }}
          </router-link>
        </li>
      </ul>
    </div>
  </div>
</template>

<script setup>
import {ref} from 'vue';

const categories = ref([
  {
    name: 'User Management',
    expanded: true, // Initially expanded
    subcategories: [
      {name: 'Users', link: '/admin/users'},
      {name: 'Invites', link: '/admin/invites'},
    ]
  },
  {
    name: 'Dashboard',
    expanded: true, // Initially expanded
    subcategories: [
      {name: 'Google Analytics', link: '/admin/analytics'},
    ]
  },
  {
    name: 'Media Management',
    expanded: true, // Initially expanded
    subcategories: [
      {name: 'Releases', link: '/admin/releases'},
      {name: 'Producers', link: '/admin/producers'},
      {name: 'Subdivisions', link: '/admin/Subdivisions'}
    ]
  }
  // Add more categories as needed
]);

const toggleCategory = (category) => {
  category.expanded = !category.expanded;
};
</script>

<style scoped>
/* You can remove this scoped style block if not needed */
</style>
