import {createStore} from 'vuex'
import axios from 'axios'
import router from "../router/index";

export default createStore({
  state: {
      equipments: [],
      equipment: '',
      equipments_type: []
  },
  mutations: {
      GET_EQUIPMENTS(state, equipments){
          state.equipments = equipments
      },
      GET_EQUIPMENT(state, equipment){
          state.equipment = equipment
      },
      GET_EQUIPMENTS_TYPE(state, equipments_type){
          state.equipments_type = equipments_type
      },
  },
  actions: {
    async LOGIN ({commit}, login_data) {
        return axios({
                url: 'http://localhost:8000/api/user/login/',
                method: "POST",
                data: {
                    username: login_data.login,
                    password: login_data.password,
                }
            }
        )
            .then((response) => {
                localStorage.setItem("token", response.data.access)
                axios.defaults.headers.common['Authorization'] = "Bearer " + localStorage.token
                router.push({name: "Equipment"})
            })
            .catch((error) => {
                localStorage.removeItem('token')
                delete axios.defaults.headers.common['Authorization']
                router.push({name: "Login"})
            })
        },
      async GET_EQUIPMENTS_FROM_API({commit}, url='http://localhost:8000/api/equipment/') {
        return axios(url, {
            method: "GET",
        })
            .then((equipments) => {
                commit('GET_EQUIPMENTS', equipments.data);
                return equipments;
            })
            .catch((error) => {
                localStorage.removeItem('token')
                delete axios.defaults.headers.common['Authorization']
                router.push({name: "Login"})
            })
  },
      async GET_EQUIPMENTS_TYPE_FROM_API({commit}) {
        return axios('http://localhost:8000/api/equipment-type/', {
            method: "GET",
        })
            .then((equipments_type) => {
                commit('GET_EQUIPMENTS_TYPE', equipments_type.data);
                return equipments_type;
            })
            .catch((error) => {
                localStorage.removeItem('token')
                delete axios.defaults.headers.common['Authorization']
                router.push({name: "Login"})
            })
  },
      async GET_EQUIPMENT_FROM_API({commit}, id) {
          return axios('http://localhost:8000/api/equipment/' + id + '/', {
              method: "GET",
          })
              .then((equipment) => {
                  commit('GET_EQUIPMENT', equipment.data);
                  return equipment;
              })
              .catch((error) => {
                  localStorage.removeItem('token')
                  delete axios.defaults.headers.common['Authorization']
                  router.push({name: "Login"})
              })
      },
      async DELETE_EQUIPMENT_FROM_API({commit}, equipment) {
            return axios('http://localhost:8000/api/equipment/' + equipment.id + '/' , {
                method: "DELETE",
            })
           .then(() => {
                      router.push({name: "Equipment"})
                  })
      },
      async SAVE_EQUIPMENT({commit}, equipment) {
            return axios('http://localhost:8000/api/equipment/' + equipment.id + '/' , {
                method: "PUT",
                data: {
                    "equipment_type": equipment.equipment_type.id,
                    "serial_number": equipment.serial_number,
                    "description": equipment.description,
                }
            })
           .then(() => {
                      router.push({name: "Equipment"})
                  })
      },
      async SAVE_EQUIPMENTS({commit}, equipments) {
            return axios('http://localhost:8000/api/equipment/', {
                method: "POST",
                data: equipments
            })
           .then((response) => {
                      alert(response.data)
                      router.push({name: "Equipment"})
                  })
      },

  },
  modules: {
  },
  getters: {
    EQUIPMENTS (state) {
          return state.equipments;
    },
    EQUIPMENT (state) {
          return state.equipment;
    },
    EQUIPMENTS_TYPE (state) {
          return state.equipments_type;
    },
  }
})
