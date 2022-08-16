<template>
    <EquipmentForm/>
    <br/><br/>
    <button @click="SAVE_EQUIPMENT(this.EQUIPMENT)">Сохранить</button>
    <br/>
    <br/>
    <button @click="DELETE_EQUIPMENT_FROM_API(this.EQUIPMENT)">Удалить</button>
</template>

<script>
import { MDBInput, MDBTextarea, MDBBtn } from 'mdb-vue-ui-kit'
import {mapActions, mapGetters} from "vuex";
import EquipmentForm from "@/components/EquipmentForm";
export default {

  name: "EquipmentEdit",
  components: {
    MDBInput,
    MDBTextarea,
    MDBBtn,
    EquipmentForm
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
                "GET_EQUIPMENTS_TYPE_FROM_API"
            ]),},
  async mounted() {
            this.GET_EQUIPMENT_FROM_API(this.$route.params.id);
            this.GET_EQUIPMENTS_TYPE_FROM_API();
            },
}
</script>

<style scoped>

</style>