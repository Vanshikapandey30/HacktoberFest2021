<template>
  <div class="header_input">
    <!-- overview texfield -->
    <div class="flex_input overview_input">
      <label for="overview">Overview</label>
      <textarea
        name="overview"
        cols="100"
        rows="10"
        class="textarea_overview"
        v-model="overview_text"
      ></textarea>
      <div class="btn_flex">
        <button class="btn submit_btn" @click="submit_overview()">
          Submit
        </button>
        <button class="btn clear_btn" @click="close()">Close</button>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  emits: ['closeInput'],
  data() {
    return {
      overview_text:
        " Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. Lorem Ipsum is simply dummy text of the printing and typesetting industry.",
    };
  },
  methods: {
    submit_overview() {
      this.$emit('inputOverview', this.overview_text);
    },
    close() {
      this.$emit('closeInput');
    },
  },
};
</script>

<style>
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
.textarea_overview {
  background: inherit;
  color: white;
  font-family: var(--font_sans);
  font-size: 15px;
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
