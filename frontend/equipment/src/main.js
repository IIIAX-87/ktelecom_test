import 'mdb-vue-ui-kit/css/mdb.min.css'
import { createApp } from 'vue'
import App from './App.vue'
import router from './router'
import store from './store'
import VeeValidate from 'vee-validate';


createApp(App)
    .use(store)
    .use(router)
    .use(VeeValidate, {locale: 'ru',})
    .mount('#app')
