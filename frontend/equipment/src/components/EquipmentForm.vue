<template>
<!--  <label>Тип оборудования: </label>-->
<!--    <input-->
<!--      type="text"-->
<!--      readonly-->
<!--      v-model="this.EQUIPMENT.equipment_type.name"-->
<!--    />-->
  <br/>
  <br/>
    <label>Серийный номер: </label>
    <input
      type="text"
      v-model="this.EQUIPMENT.serial_number"
    />
    <br/>
    <label>Описание: </label>
    <input
      type="text"
      v-model="this.EQUIPMENT.description"
    />

</template>

<script>
import { MDBInput, MDBTextarea, MDBBtn } from 'mdb-vue-ui-kit'
import {mapActions, mapGetters} from "vuex";
export default {
  data() {
            return {
                equipment_type: ""
            }
        },
  name: "EquipmentForm",
  components: {
    MDBInput,
    MDBTextarea,
    MDBBtn
  },
  computed: mapGetters([
            "EQUIPMENT",
            "EQUIPMENTS_TYPE",
        ]),
  methods: {
    delete(equipment){
      this.DELETE_EQUIPMENT_FROM_API(equipment)
    },
            ...mapActions([
                "GET_EQUIPMENT_FROM_API",
                "DELETE_EQUIPMENT_FROM_API",
                "SAVE_EQUIPMENT",
            ]),},
  async mounted() {
            this.GET_EQUIPMENT_FROM_API(this.$route.params.id);
            },
}
</script>

<style scoped>

</style>