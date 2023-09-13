<template>
  <div class="flex flex-col items-center justify-center h-screen">
    <h1 class="text-2xl font-bold mb-4">Register</h1>
    <div class="w-[100%] max-w-xs space-y-4">
      <p class="font-inter text-sm py-3">
        Hello, please enter your new credentials for instant access.
      </p>
      <form @submit.prevent="handleRegister" class="flex flex-col space-y-3 w-full">
        <!-- TODO: may handle keyup.enter event when no focus -->

        <!-- Username field with error handling -->
        <InputComponent
            @keyup.enter="handleRegister"
            labelText="Username:"
            placeholderText="Choose your username"
            inputType="username"
            v-model="form.username"
        />

        <!-- Password field with error handling -->
        <InputComponent
            @keyup.enter="handleRegister"
            labelText="Password:"
            placeholderText="Choose your password"
            inputType="password"
            v-model="form.password"
        />

        <!-- Password confirmation field with error handling -->
        <InputComponent
            @keyup.enter="handleRegister"
            labelText="Password confirmation:"
            placeholderText="Re-enter your password"
            inputType="password"
            v-model="form.password_confirmation"
        />

        <ButtonComponent
            style="min-height: 2rem"
            type="submit"
            :disabled="isLoading"
        >
          <template v-if="!isLoading">
            Register
          </template>
          <template v-else>
            <SpinnerComponent size="1.25rem"/>
          </template>
        </ButtonComponent>
      </form>
    </div>
  </div>

</template>

<script setup>
import {ref} from "vue";
import ButtonComponent from "@/components/ButtonComponent.vue";
import InputComponent from "@/components/InputComponent.vue";
import SpinnerComponent from "@/components/SpinnerComponent.vue";
import {AuthService} from "@/client";
import router from "@/routers/router";
import {useAuthStore} from "@/stores/authStore";
import AlertComponent from "@/components/AlertComponent.vue";

const form = ref({
  username: null,
  password: null,
  password_confirmation: null,
});

const isLoading = ref(false);
const registerFailedAttempts = ref([])


function handleRegister() {
  const authStore = useAuthStore()
  isLoading.value = true;
  const inviteToken = new URLSearchParams(window.location.search).get('token');
  console.log(inviteToken)

  AuthService.authRegister({
    invite_token: inviteToken,
    username: form.value.username,
    password: form.value.password
  })
      .then(
          (response) => {
            isLoading.value = false;
            authStore.registerLogin(response.access_token, response.refresh_token)
                .catch((reason) => {
                  registerFailedAttempts.value.push({
                    title: "Register Failed",
                    message: reason,
                  });
                })

            router.push('/admin/users')
          })
      .catch(
          (reason) => {
            registerFailedAttempts.value.push({
              title: "Register Failed",
              message: reason,
            });
          })
      .finally(
          () => {
            isLoading.value = false;
          }
      )
}
</script>

<style scoped>
</style>