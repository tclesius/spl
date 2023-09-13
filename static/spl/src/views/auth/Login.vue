<template>
  <div class="flex flex-col items-center justify-center h-screen">
    <h1 class="text-2xl font-bold mb-4">Login</h1>

    <div class="w-[100%] max-w-xs space-y-4">
      <div class="flex flex-col space-y-2 w-full">
        <!-- TODO: may handle keyup.enter event when no focus -->
        <InputComponent
            @keyup.enter="handleLogin"
            labelText="Username:"
            placeholderText="Enter your username"
            inputType="username"
            v-model="form.username"
        />
        <InputComponent
            @keyup.enter="handleLogin"
            labelText="Password:"
            placeholderText="Enter your password"
            inputType="password"
            v-model="form.password"
        />
        <CheckBoxComponent
            labelText="Remember me"
            inputId="test"
            v-model="rememberMe"
            class="py-2"
        />
        <ButtonComponent
            style="min-height: 2rem" @click="handleLogin" :disabled="isLoading"
        >
          <template v-if="!isLoading">
            Login
          </template>
          <template v-else>
            <SpinnerComponent size="1.25rem"/>
          </template>
        </ButtonComponent>
      </div>
    </div>
    <div class="bottom-4 right-4 z-50 max-h-[80vh] absolute overflow-y-hidden">
      <AlertComponent v-for="(attempt, index) in loginFailedAttempts" :key="index" type="error" :title="attempt.title"
                      :message="attempt.message" autoCloseDuration="1" class="mb-2"/>
    </div>
  </div>

</template>

<script setup>
import {ref} from "vue";
import CheckBoxComponent from "@/components/CheckBoxComponent.vue";
import ButtonComponent from "@/components/ButtonComponent.vue";
import InputComponent from "@/components/InputComponent.vue";
import SpinnerComponent from "@/components/SpinnerComponent.vue";
import AlertComponent from "@/components/AlertComponent.vue";
import {useAuthStore} from "@/stores/authStore";
import router from "@/routers/router";

const rememberedUser = localStorage.getItem("username")

const form = ref({
      username: rememberedUser, // item present if remember me activated
      password: null
    }
);
const rememberMe = ref(!!rememberedUser); // TODO: implement remember me funcitonality

const isLoading = ref(false);
const loginFailedAttempts = ref([]);
const isLoginInProgress = ref(false); // Flag to track if a login is already in progress
const authStore = useAuthStore()

const handleLogin = () => {
  if (isLoginInProgress.value) {
    // Don't proceed if a login is already in progress
    return;
  }

  isLoading.value = true;
  isLoginInProgress.value = true;

  authStore.login(form.value.username, form.value.password)
      .then(
          () => {
            isLoading.value = false;
            isLoginInProgress.value = false
            router.push('/admin/users')
            if (rememberMe.value) {
              localStorage.setItem("username", form.value.username)
            } else {
              localStorage.removeItem("username")
            }
          })
      .catch(
          () => {
            loginFailedAttempts.value.push({
              title: "Login Failed",
              message: "Invalid credentials. Please try again.",
            });
          })
      .finally(
          () => {
            isLoading.value = false;
            isLoginInProgress.value = false
          }
      )
};
</script>

<style scoped>
</style>
