<template>
  <div class="header_part">
    <div class="logo">
      <img
        src="https://cdn.dribbble.com/users/24078/screenshots/15522433/media/e92e58ec9d338a234945ae3d3ffd5be3.jpg?compress=1&resize=400x300"
        alt="logo"
        class="logo"
      />
    </div>
    <div class="buttons">
      <!-- <button class="btn btn_reset">Reset</button> -->
      <button @click="downloadPdf()" class="btn btn_download">Download</button>
    </div>
  </div>
</template>

<script>
export default {
  methods: {
    downloadPdf() {
      this.$emit('downloadtopdf');
    },
  },
};
</script>

<style scoped>
.header_part {
  height: 15vh;
  width: 100%;
  background-color: #000000;
  display: flex;
  justify-content: space-between;
  align-items: center;
}
.logo {
  height: 90px;
}
.buttons {
  margin-right: 100px;
}
.btn {
  margin-right: 30px;
  border: none;
  cursor: pointer;
  width: 100px;
  height: 35px;
  border-radius: 3px;
  font-family: var(--font_sans);
  font-size: 15px;
  transition: transform 0.3s ease;
}
.btn_reset {
  background: none;
  color: white;
  border: 2px dashed white;
}
.btn:hover {
  transform: translateY(10%);
}
</style>
