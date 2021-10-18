<template>
  <div class="education_input">
    <!-- Education Input Name -->
    <div class="flex_both">
      <div class="education_input_degree_name flex_input">
        <label for="name">Degree Name:</label>
        <input
          type="text"
          name="name"
          class="change_input"
          autocomplete="off"
          v-model="name"
        />
      </div>
      <!-- Education Input course -->
      <div class="header_input_name flex_input">
        <label for="course">Course:</label>
        <input
          type="text"
          name="course"
          class="change_input"
          autocomplete="off"
          v-model="course"
        />
      </div>
    </div>

    <div class="flex_both">
      <!-- Education Input university -->
      <div class="education_input_uni flex_input">
        <label for="uni">University:</label>
        <input
          type="text"
          name="uni"
          class="change_input"
          autocomplete="off"
          v-model="uni"
        />
      </div>
      <!-- Education Input address -->
      <div class="header_input_name flex_input">
        <label for="address">Address:</label>
        <input
          type="text"
          name="address"
          class="change_input"
          autocomplete="off"
          v-model="address"
        />
      </div>
    </div>

    <!-- Education Input address -->
    <div class="header_input_name flex_input">
      <label for="gpa">GPA:</label>
      <input
        type="text"
        name="gpa"
        class="change_input"
        autocomplete="off"
        v-model="gpa"
      />
    </div>

    <!-- submit btn -->
    <div class="btn_flex">
      <button class="btn submit_btn" @click="submit_education()">Submit</button>
      <button class="btn clear_btn" @click="close()">Close</button>
    </div>
  </div>
</template>

<script>
export default {
  data() {
    return {
      name: '',
      course: '',
      uni: '',
      address: '',
      gpa: '',
    };
  },
  methods: {
    submit_education() {
      this.$emit(
        'inputEducation',
        this.name,
        this.course,
        this.uni,
        this.address,
        this.gpa
      );
    },
    close() {
      this.$emit('closeInput');
    },
  },
};
</script>

<style>
.flex_both {
  display: flex;
}
.education_input_degree_name {
  margin-right: 10px;
}
.education_input_uni {
  margin-right: 10px;
}
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
