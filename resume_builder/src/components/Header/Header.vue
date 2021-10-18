<template>
  <header class="header flex">
    <!-- Name -->
    <div class="name">
      <span class="name_second"> {{ name }} </span>
      <div @click="edit_name()" class="header_edit">
        <button v-if="btnClose" class="btn btn_change">
          <i class="fas fa-pen"></i>
        </button>
      </div>
    </div>
    <!-- phone number -->
    <div class="phone">
      <span class="phone_number"> +91 {{ contact }} </span>
    </div>
    <!-- Email -->
    <div class="email">
      <span class="email_desc"> {{ email }} </span>
    </div>
  </header>
</template>

<script>
export default {
  props: ['name', 'contact', 'email', 'btnClose'],
  methods: {
    edit_name() {
      this.$emit('openHeaderEdit');
    },
  },
};
</script>

<style>
.header {
  width: 100%;
  height: 25%;
  background-color: #333e50;
}
.flex {
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
}
.name {
  color: white;
  font-family: var(--font);
  font-size: 35px;
  display: flex;
  /* flex-direction: column; */
  justify-content: center;
  align-items: center;
}
.name_second {
  color: #fff;
}
.phone_number {
  color: #fff;
  font-size: 15px;
  font-family: var(--font_roboto);
}
.email_desc {
  color: #fff;
  font-family: var(--font_roboto);
}
.input_header {
  width: 60%;
  display: flex;
  height: 60%;
}
.btn_icon {
  width: 20px;
  height: 20px;
  margin-left: 20px;
  border: 0.2px solid black;
  border-radius: 5px;
  background: #fc30ef;
  color: #fff;
  font-size: 10px;
  cursor: pointer;
}
.header_edit {
  transform: translateX(10px);
}
.header_edit > .btn_change > i {
  font-size: 10px;
  color: white;
  transform: translateY(-5px);
}
.btn_change {
  border: 1px solid black;
  padding: 3px;
  border-radius: 4px;
  background: red;
  width: 20px;
  height: 20px;
}
</style>
