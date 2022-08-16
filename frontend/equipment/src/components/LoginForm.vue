<template>
  <MDBInput v-model="login" label="username" type="text" placeholder="Логин"/>
  <MDBInput v-model="password" label="password" type="password" placeholder="Пароль"/>
  <MDBBtn @click="goLogin">Войти</MDBBtn>
</template>

<script>
import { MDBInput, MDBBtn } from 'mdb-vue-ui-kit';
axios.defaults.xsrfCookieName = 'csrftoken'
axios.defaults.xsrfHeaderName = 'X-CSRFToken'
import axios from "axios"
export default {
  name: "LoginForm",
  components: {
    MDBInput,
    MDBBtn
  },
  data() {
            return {
                login: '',
                password: '',
            }
        },
        methods: {
            goLogin () {
                let login_data = {
                    login: this.login,
                    password: this.password,
                }
                this.$store.dispatch('LOGIN', login_data)
            }

            },
}
</script>

<style scoped>

</style>