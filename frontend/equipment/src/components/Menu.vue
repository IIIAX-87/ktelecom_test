<template>
  <MDBNavbar expand="lg" light bg="white" container>
        <MDBNavbarNav  class="mb-2 mb-lg-0">
          <MDBNavbarItem to="/">
            Оборудование
          </MDBNavbarItem>
          <MDBNavbarItem to="/equipment_add">
            Добваить оборудование
          </MDBNavbarItem>
        </MDBNavbarNav>
      </MDBNavbar>
</template>

<script>
import {MDBNavbar, MDBNavbarNav, MDBNavbarItem } from 'mdb-vue-ui-kit';
export default {
  data() {
    return {
    }
  },
  name: "Menu",
  components: {
    MDBNavbar,
    MDBNavbarNav,
    MDBNavbarItem
  },
}
</script>

<style scoped>

</style>