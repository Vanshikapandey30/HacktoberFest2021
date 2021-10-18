<template>
  <div class="experience_input">
    <div class="title_name_both flex_both">
      <div class="exp_input_title flex_input">
        <label for="exp_title">Title:</label>
        <input
          type="text"
          name="exp_title"
          class="change_input"
          autocomplete="off"
          v-model="title"
        />
      </div>
      <!-- Experience name -->
      <div class="exp_input_name flex_input">
        <label for="exp_name">Name:</label>
        <input
          type="text"
          name="exp_name"
          class="change_input"
          autocomplete="off"
          v-model="name"
        />
      </div>
    </div>
    <!-- Experience title name -->

    <div class="experience_input flex_both">
      <!-- Experience start date -->
      <div class="exp_input_start_date flex_input">
        <label for="exp_start_date">Start Date:</label>
        <input
          type="date"
          name="exp_start_date"
          class="change_input"
          autocomplete="off"
          v-model="start_date"
        />
      </div>
      <!-- Experience end date -->
      <div class="exp_input_end_date flex_input">
        <label for="exp_end_date">End Date:</label>
        <input
          type="date"
          name="exp_end_date"
          class="change_input"
          autocomplete="off"
          v-model="end_date"
        />
      </div>
    </div>

    <!-- Experience role -->
    <div class="exp_input_role flex_input">
      <label for="exp_role">Role:</label>
      <input
        type="text"
        name="exp_role"
        class="change_input"
        autocomplete="off"
        v-model="role"
      />
    </div>
    <!-- Experience Description 1 -->
    <div class="exp_input_desc1 flex_input">
      <label for="exp_desc1">Description 1:</label>
      <textarea
        type="text"
        name="exp_desc1"
        class="change_input"
        autocomplete="off"
        v-model="desc1"
      ></textarea>
    </div>
    <!-- Experience Description 1 -->
    <div class="exp_input_desc2 flex_input">
      <label for="exp_desc2">Description 2:</label>
      <textarea
        type="text"
        name="exp_desc2"
        class="change_input"
        autocomplete="off"
        v-model="desc2"
      ></textarea>
    </div>
    <!-- submit btn -->
    <div class="btn_flex">
      <button class="btn submit_btn" @click="submit_exp()">Submit</button>
      <button class="btn clear_btn" @click="close()">Close</button>
    </div>
  </div>
</template>

<script>
export default {
  data() {
    return {
      title: '',
      name: '',
      start_date: '',
      end_date: '',
      role: '',
      desc1: '',
      desc2: '',
    };
  },
  methods: {
    submit_exp() {
      this.$emit(
        'inputExp',
        this.title,
        this.name,
        this.start_date,
        this.end_date,
        this.role,
        this.desc1,
        this.desc2
      );
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
  margin-top: 10px;
}
.submit_btn {
  margin-top: 10px;
}
label {
  color: #fff;
  font-size: 15px;
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
  margin-top: 10px;
}
.flex_both {
  display: flex;
}
.exp_input_title {
  margin-right: 10px;
}
.exp_input_start_date {
  margin-right: 10px;
}
::-webkit-calendar-picker-indicator {
  filter: invert(1);
}
</style>
