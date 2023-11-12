import './assets/main.css'

import { createApp } from 'vue'
import { createPinia } from 'pinia'
import App from './App.vue'
import './index.css'
import Vue3Toastify from 'vue3-toastify'

const app = createApp(App)

app.use(createPinia())
app.use(Vue3Toastify, {
  autoClose: 3000
})

app.mount('#app')
