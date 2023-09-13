import {defineStore} from "pinia";
import {AuthService, OpenAPI} from "@/client";
import router from "@/routers/router";


export const useAuthStore = defineStore('auth', () => {
    async function login(username, password) {
        return AuthService.authGetToken({username: username, password: password})
            .then(
                (result) => {
                    localStorage.setItem("access_token", result.access_token)
                    localStorage.setItem("refresh_token", result.refresh_token)
                    OpenAPI.TOKEN = result.access_token
                }
            )
    }

    async function refreshAccess() {
        AuthService.authRefreshAccessToken(localStorage.getItem("refresh_token"))
            .then((result) => {
                localStorage.setItem("access_token", result.access_token)
                OpenAPI.TOKEN = result.access_token
            })
    }

    async function registerLogin(access_token, refresh_token) {
        localStorage.setItem("access_token", access_token)
        localStorage.setItem("refresh_token", refresh_token)
        OpenAPI.TOKEN = access_token
    }

    async function logout() {
        localStorage.clear()
        OpenAPI.TOKEN = null
        await router.push("admin/login")
    }

    return {login, logout, registerLogin};
})