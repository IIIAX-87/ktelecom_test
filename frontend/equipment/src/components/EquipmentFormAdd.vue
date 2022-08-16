<template>
  <form>
  <label>Тип оборудования: </label>
    <select v-model="equipment_type">
        <option
                v-for="equipment_type in EQUIPMENTS_TYPE.results"
                :key="equipment_type.id"
                :value="equipment_type.id"
                :label="equipment_type.name"
        >
        </option>
    </select>
  <br/>
  <br/>
    <label>Серийный номер: </label>
    <input
      type="text"
      v-model="serial_number"
    />
    <br/>
    <label>Описание: </label>
    <input
      type="text"
      v-model="description"
    />
    <Field name="field" :rules="isRequired" />
    <ErrorMessage name="field" />
</form>
</template>

<script>
import { Field, Form, ErrorMessage } from 'vee-validate';
import {mapActions, mapGetters} from "vuex";
export default {
  data() {
            return {
                equipment_type: "",
                serial_number: "",
                description: ""
            }
        },
  name: "EquipmentFormAdd",
  components: {
    Field,
    Form,
    ErrorMessage,
  },
  computed: mapGetters([
            "EQUIPMENTS_TYPE",
        ]),
  methods: {
    isRequired(value) {
      if (value && value.trim()) {
        return true;
      }
      return 'This is required';
    },
    delete(equipment){
      console.log(equipment)
      this.DELETE_EQUIPMENT_FROM_API(equipment)
    },
            ...mapActions([
                "GET_EQUIPMENTS_TYPE_FROM_API"
            ]),},
  async mounted() {
            this.GET_EQUIPMENTS_TYPE_FROM_API();
            },
}
</script>

<style scoped>

</style>