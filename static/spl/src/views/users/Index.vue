<template>
  <div>
    <h1 class="text-3xl font-semibold flex items-center p-10 pb-0">
      Users
      <PillComponent class="text-base align-middle mx-3" name="Count" :value="userCount"/>
    </h1>

    <!-- Add a User section -->
    <div class="mt-4 space-y-2 max-w-xs p-10">
      <h2 class="text-base font-semibold">Add a User</h2>
      <SelectComponent
          labelText="Type:"
          :options="selectOptions"
          v-model="form.is_admin"
      />
      <InputComponent
          labelText="Email:"
          placeholderText="Enter a email address"
          inputType="text"
          v-model="form.email"
      />
      <ButtonComponent
          class="px-3 min-h-[2rem] w-32"
          :disabled="isLoading"
          @click="inviteUser"
          @click.stop="inviteUser"
          type="button"
      >
        <template v-if="!isLoading">
          Send Invitation
        </template>
        <template v-else>
          <SpinnerComponent size="1.25rem"/>
        </template>
      </ButtonComponent>


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
            >Change Password
            </ButtonComponent>
          </td>
          <td>
            <ButtonComponent
                class="p-2 bg-red-500"
                :disabled="isLoading"
                @click="removeUser(user.id)"
                @click.stop="removeUser(user.id)"
                type="button"
            >Delete
            </ButtonComponent>
          </td>
        </tr>
      </table>
    </div>

    <div class="bottom-4 right-4 z-50 max-h-[80vh] absolute overflow-y-hidden">
      <AlertComponent v-for="(attempt, index) in alerts" :key="Index" type="error"
                      :title="attempt.title"
                      :message="attempt.message" autoCloseDuration="3" class="mb-2"/>
    </div>
  </div>
</template>

<script setup>
import PillComponent from "@/components/PillComponent.vue";
import InputComponent from "@/components/InputComponent.vue";
import SelectComponent from "@/components/SelectComponent.vue";
import {onMounted, ref} from "vue";
import ButtonComponent from "@/components/ButtonComponent.vue";
import SpinnerComponent from "@/components/SpinnerComponent.vue";
import AlertComponent from "@/components/AlertComponent.vue";
import {AdminService} from "@/client";
import {useAuthStore} from "@/stores/authStore";
import router from "@/routers/router";


const selectOptions = [
  {label: "Admin", value: true},
  {label: "User", value: false}
]

const form = ref({
  is_admin: false,
  email: ''
})


const userCount = ref(null)
const users = ref([])
const alerts = ref([])
const isLoading = ref(false)
const authStore = useAuthStore()

const removeUser = (userId) => {
  AdminService.userRemoveUser(userId)
      .then((response) => {
        const index = users.value.findIndex((user) => user.id === userId)
        if (~index) {
          users.value.splice(index, 1)
        }

        const alert = {
          title: 'Success',
          message: response,
        }
        alerts.value.push(alert)
      })
      .catch((reason) => {
            if (reason.status === 401) {
              authStore.logout() // TODO here should later be the refreshtoken logic be handled
            }
            const alert = {
              title: 'Failure',
              message: reason,
            }
            alerts.value.push(alert)
          }
      )
}
const getUsers = () => {
  AdminService.userGetAllUser()
      .then((response) => {
        userCount.value = response.data.length
        users.value = response.data
      })
      .catch((reason) => {
            if (reason.status === 401) {
              authStore.logout() // TODO here should later be the refreshtoken logic be handled
            }
            const alert = {
              title: 'Failure',
              message: reason,
            }
            alerts.value.push(alert)
          }
      )
      .finally(() => {
        isLoading.value = false
      })
}

function inviteUser() {
  console.log(form.value)
  AdminService.inviteSend(form.value)
      .then(() => {
        const alert = {
          title: 'Success',
          message: 'Invitation sent.',
        }
        alerts.value.push(alert)
      })
      .catch((reason) => {
            if (reason.status === 401) {
              authStore.logout() // TODO here should later be the refreshtoken logic be handled
            }
            const alert = {
              title: 'Failure',
              message: reason,
            }
            alerts.value.push(alert)
          }
      )
      .finally(() => {
        isLoading.value = false
      })
}

onMounted(() => {
  getUsers()
})
</script>

<style scoped>
table {
  table-layout: fixed;
}

td {
  overflow: hidden;
  text-overflow: ellipsis;
  word-wrap: break-word;
}

@media only screen and (max-width: 480px) {
  /* horizontal scrollbar for tables if mobile screen */
  table {
    table-layout: fixed;
    overflow-x: auto;
    display: block;
  }
}
</style>
