<template>
  <div class="home">
    <EquipmentSearch/>
    <EquipmentList/>
  </div>
</template>

<script>
import EquipmentList from '@/components/EquipmentList.vue'
import EquipmentSearch from '@/components/EquipmentSearch.vue'

export default {
  name: 'Equipment',
  components: {
    EquipmentList,
    EquipmentSearch
  }
}
</script>
