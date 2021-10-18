<template>
  <div class="header_input">
    <!-- Header Input Name -->
    <div class="header_input_name flex_input">
      <label for="username">Name:</label>
      <input
        type="text"
        name="username"
        class="change_input"
        autocomplete="off"
        v-model="name"
      />
    </div>
    <!-- Header Input Number -->
    <div class="header_input_phone flex_input">
      <label for="phoneno">Phone No.:</label>
      <input
        type="number"
        name="phoneno"
        class="change_input"
        autocomplete="off"
        v-model="phone"
      />
    </div>
    <!-- Header Input Email -->
    <div class="header_input_phone flex_input">
      <label for="email">Email:</label>
      <input
        type="email"
        name="email"
        class="change_input"
        autocomplete="off"
        v-model="email"
      />
    </div>
    <!-- submit btn -->
    <div class="btn_flex">
      <button class="btn submit_btn" @click="submit_header()">Submit</button>
      <button class="btn clear_btn" @click="close()">Close</button>
    </div>
  </div>
</template>

<script>
export default {
  data() {
    return {
      name: '',
      phone: '',
      email: '',
    };
  },
  methods: {
    submit_header() {
      this.$emit('inputeHeader', this.name, this.phone, this.email);
    },
    close() {
      this.$emit('closeInput');
    },
  },
};
</script>

<style scoped>
.flex_input {
  display: flex;
  flex-direction: column;
  justify-content: center;
  /* align-items: center; */
  margin-top: 30px;
}
.submit_btn {
  margin-top: 30px;
}
label {
  color: #fff;
  font-size: 20px;
  font-family: var(--font_sans);
}
.change_input {
  width: 300px;
  background: none;
  outline: none;
  border: none;
  border-bottom: 1px solid #eb23e1;
  margin-top: 10px;
  color: #ffffff;
  font-size: 15px;
  font-family: var(--font_roboto);
}
.btn_flex {
  display: flex;
  justify-content: center;
  align-items: center;
}
.clear_btn {
  margin-top: 30px;
}
</style>
