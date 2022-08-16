<template>
  <div class="home">
    <EquipmentTypeList/>
  </div>
</template>

<script>
import EquipmentTypeList from '@/components/EquipmentTypeList.vue'

export default {
  name: 'EquipmentType',
  components: {
    EquipmentTypeList,
  }
}
</script>
