<template>
  <div class="hobbie_input">
    <!-- Hobbie Input title -->
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
    <div class="hobbies_input_title flex_input">
      <label for="list">Hobbies List:</label>
      <input
        type="text"
        name="list"
        class="change_input"
        autocomplete="off"
        placeholder="Add comma seperated highlight"
        v-model="hobbies_list"
      />
    </div>
    <!-- submit btn -->
    <!-- submit btn -->
    <div class="btn_flex">
      <button class="btn submit_btn" @click="submit_hobbies()">Submit</button>
      <button class="btn clear_btn" @click="close()">Close</button>
    </div>
  </div>
</template>

<script>
export default {
  data() {
    return {
      title: '',
      hobbies_list: '',
    };
  },
  methods: {
    submit_hobbies() {
      this.$emit('inputHobbie', this.title, this.hobbies_list);
      this.hobbies_list = '';
    },
    close() {
      this.$emit('closeInput');
    },
  },
};
</script>

<style></style>
