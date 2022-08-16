<template>
  <MDBInput @input:="this.find(serial_number)" label="Введите серийный номер" v-model="serial_number" />
  <MDBInput label="Введите примечание" v-model="description" />
</template>

<script>
import { MDBInput } from 'mdb-vue-ui-kit'
import {mapActions, mapGetters} from "vuex";
export default {
  data() {
    return {
      serial_number:"",
      description:"",
    }
  },
  name: "EquipmentSearch",
  components: {
      MDBInput,
    },
  computed: mapGetters([
            "EQUIPMENTS",
        ]),
  methods: {
    find(serial_number){
      this.EQUIPMENTS.filter(item => item.serial_number === serial_number)
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