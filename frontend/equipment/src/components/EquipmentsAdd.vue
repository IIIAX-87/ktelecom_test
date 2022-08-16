<template>
<button @click="addLine">Добавить строки</button>
            <div v-for="(equipment, index) in equipments"><br>
              <label>Тип оборудования: </label>
        <select v-model="equipment.equipment_type">
        <option
                v-for="equipment_type in EQUIPMENTS_TYPE.results"
                :key="index"
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
      v-model="equipment.serial_number"
    />
    <br/>
    <label>Описание: </label>
    <input
      type="text"
      v-model="equipment.description"
    />
            </div>
<br/>
<br/>
  <button @click="save()">Сохранить</button>
</template>

<script>
import {mapActions, mapGetters} from "vuex";

export default {
  name: "EquipmentsAdd",
  data() {
            return {
                equipments: [],
            }
        },
  components: {
  },
  methods: {
    addLine(){
      this.equipments.push({
        'equipment_type':'',
        'serial_number':'',
        'description':'',
      })
    },
    save(){
      this.SAVE_EQUIPMENTS(this.equipments)
    },
    ...mapActions([
                "GET_EQUIPMENTS_TYPE_FROM_API",
                "SAVE_EQUIPMENTS"
            ]),},
  async mounted() {
            this.GET_EQUIPMENTS_TYPE_FROM_API();
            },
  computed: mapGetters([
            "EQUIPMENTS_TYPE",
        ]),
}
</script>

<style scoped>

</style>