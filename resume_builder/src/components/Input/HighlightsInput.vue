<template>
  <div class="highlight_input">
    <!-- Highlights Input title -->
    <div class="highlight_input_title flex_input">
      <label for="title">Title:</label>
      <input
        type="text"
        name="title"
        class="change_input"
        autocomplete="off"
        v-model="title"
      />
    </div>
    <!-- Highlights Input list -->
    <div class="highlight_input_title flex_input">
      <label for="list">Highlist List:</label>
      <input
        type="text"
        name="list"
        class="change_input"
        autocomplete="off"
        placeholder="Add comma seperated highlight"
        v-model="highlight_list"
      />
    </div>
    <!-- submit btn -->
    <div class="btn_flex">
      <button class="btn submit_btn" @click="submit_highlight()">Submit</button>
      <button class="btn clear_btn" @click="close()">Close</button>
    </div>
  </div>
</template>

<script>
export default {
  data() {
    return {
      title: '',
      highlight_list: '',
    };
  },
  methods: {
    submit_highlight() {
      this.$emit('inputHighlight', this.title, this.highlight_list);
      this.highlight_list = '';
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
