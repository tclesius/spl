// router.js
import loginRouteGuard from './routeGuards';
import Login from "@/views/auth/Login.vue";
import {createRouter, createWebHistory} from "vue-router";
import Register from "@/views/auth/Register.vue";
import NotFound from "@/views/NotFound.vue";
import AdminLayout from "@/views/layouts/AdminLayout.vue";
import Users from "@/views/users/Index.vue";
import Invites from "@/views/invites/Index.vue";

export default createRouter({
    history: createWebHistory(),
    routes: [
        {
            path: '/admin',
            children: [
                {
                    path: 'login',
                    component: Login,
                    meta: {requiresGuest: true},
                    beforeEnter: loginRouteGuard,
                },
                {
                    path: 'register',
                    component: Register,
                    meta: {requiresGuest: true},
                },
            ],
        },
        {
            path: '/admin',
            component: AdminLayout,
            children: [
                {
                    path: 'invites',
                    component: Invites,
                    meta: {requiresAuth: true},
                    beforeEnter: loginRouteGuard,
                },
                {
                    path: 'users',
                    component: Users,
                    meta: {requiresAuth: true},
                    beforeEnter: loginRouteGuard,
                },
                {
                    path: '/:pathMatch(.*)*',
                    component: NotFound,
                    meta: {requiresAuth: true},
                    beforeEnter: loginRouteGuard,
                },
            ],
        },
        {
            path: '/admin',
            redirect: '/admin/login',
        },
    ],
});