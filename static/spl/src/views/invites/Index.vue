<script setup>
import ButtonComponent from "@/components/ButtonComponent.vue";

</script>

<template>
  <table>
    <tr>
      <th>ID</th>
      <th>Admin</th>
      <th>Username</th>
      <th>Email</th>
      <th>Created at</th>
      <th>Avatar</th>
    </tr>
    <tr v-for="user in users">
      <td>{{ user.id }}</td>
      <td>{{ user.admin }}</td>
      <td>{{ user.username }}</td>
      <td>{{ user.email }}</td>
      <td>{{ user.created_at }}</td>
      <td>Placeholder</td>
      <td>
        <ButtonComponent
            class="p-2"
            :disabled="isLoading"
            @click="inviteUser"
            @click.stop="inviteUser"
            type="button"
        >Revoke
        </ButtonComponent>
      </td>
      <td>
        <ButtonComponent
            class="p-2 bg-red-500"
            :disabled="isLoading"
            @click="removeUser(user.id)"
            @click.stop="removeUser(user.id)"
            type="button"
        >Resend
        </ButtonComponent>
      </td>
    </tr>
  </table>
</template>

<style scoped>

</style>