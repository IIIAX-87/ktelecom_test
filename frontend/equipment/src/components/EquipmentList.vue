<template>
<MDBTable>
    <thead>
      <tr>
        <th scope="col">id</th>
        <th scope="col">Тип оборудования</th>
        <th scope="col">Серийный номер</th>
        <th scope="col">Примечание</th>
      </tr>
    </thead>
    <tbody>
      <tr v-for="equipment in EQUIPMENTS.results">
        <th scope="row">{{ equipment.id }}</th>
        <td>{{ equipment.equipment_type.name }} (mask: {{ equipment.equipment_type.mask }})</td>
        <td>{{ equipment.serial_number }}</td>
        <td>{{ equipment.description }}</td>
        <td>
          <MDBBtn color="warning" rounded size="sm">
            <router-link :to="{name: 'EquipmentEdit', params: {id: equipment.id}}">Изменить</router-link>
          </MDBBtn>
<!--          <MDBBtn color="danger" rounded size="sm">Удалить</MDBBtn>-->
        </td>
      </tr>
    </tbody>
  </MDBTable>
  <button v-if="EQUIPMENTS.previous" @click="this.GET_EQUIPMENTS_FROM_API(EQUIPMENTS.previous)">Предыдущая страница</button>
  <button v-if="EQUIPMENTS.next" @click="this.GET_EQUIPMENTS_FROM_API(EQUIPMENTS.next)">Следующая страница</button>

</template>

<script>
import { MDBTable, MDBBtn } from 'mdb-vue-ui-kit'
import {mapActions, mapGetters} from "vuex";
export default {
  data() {
    return {
      equip:"",
      serial_number:""
    }
  },
  name: "EquipmentList",
  components: {
    MDBTable,
    MDBBtn
  },
  computed: mapGetters([
            "EQUIPMENTS",
        ]),
  methods: {
    filter_serial(serial_number){
      console.log(serial_number)
      // this.EQUIPMENTS.results.filter(item => item.serial_number === serial_number)
    },
            ...mapActions([
                "GET_EQUIPMENTS_FROM_API",
            ]),},
  async mounted() {
            this.GET_EQUIPMENTS_FROM_API();
            },

}
</script>

<style scoped>
</style>
