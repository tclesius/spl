import './assets/main.css'
import '@fortawesome/fontawesome-free/css/all.css';

import {createApp} from 'vue'
import {createPinia} from 'pinia'


import App from './App.vue'
import router from "@/routers/router";
import {OpenAPI} from "@/client";

const app = createApp(App)

OpenAPI.BASE = 'http://127.0.0.1:8000' // TODO: get the base via .env

app.use(createPinia())
app.use(router)

app.mount('#app')
