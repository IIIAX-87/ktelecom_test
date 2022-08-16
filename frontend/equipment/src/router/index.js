import { createRouter, createWebHistory } from 'vue-router'
import Equipment from '../views/Equipment.vue'
import Login from "@/views/Login";
import EquipmentEdit from "@/components/EquipmentEdit";
import EquipmentsAdd from "@/components/EquipmentsAdd";

const routes = [
  {
    path: '/',
    name: 'Equipment',
    component: Equipment
  },
  {
    path: '/equipment/:id/',
    name: 'EquipmentEdit',
    component: EquipmentEdit,
    props: true
  },
    {
    path: '/equipment_add',
    name: 'Equipment add',
    component: EquipmentsAdd
  },
      {
    path: '/login',
    name: 'Login',
    component: Login
  },

]

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes
})

export default router
