<template>
  <div class="education">
    <!-- Education Title -->
    <div class="education_title">
      <span contenteditable="true">Education</span>
      <div @click="edit_edu()" class="header_edit">
        <button v-if="btnClose" class="btn btn_change">
          <i class="fas fa-pen"></i>
        </button>
      </div>
    </div>
    <!-- Education Description -->
    <div class="education_desc">
      <ul class="education_desc_ul" contenteditable="true">
        <li>
          <span class="education_desc_degree_name">{{ degree }},</span>
          <br />
          <span class="education_desc_course_name">{{ course }},</span>
          <br />
          <span class="education_desc_uni_name"> {{ university }}, </span>
          <br />
          <span class="education_desc_uni_place"> {{ address }}, </span>
          <br />
          <span class="education_desc_uni_cgpa"> {{ gpa }} GPA </span>
          <br />
        </li>
      </ul>
    </div>
  </div>
</template>

<script>
export default {
  props: ['degree', 'course', 'university', 'address', 'gpa', 'btnClose'],
  methods: {
    edit_edu() {
      this.$emit('openEduEdit');
    },
  },
};
</script>

<style scoped>
.education_title {
  margin-top: 30px;
  margin-left: 30px;
  font-size: 20px;
  font-family: var(--font);
  color: #cb570c;
  display: flex;
}
.education_desc {
  margin-left: 30px;
  margin-top: 10px;
}
.education_desc_ul {
  font-family: var(--font_sans);
  display: flex;
  flex-direction: column;
}
.education_desc_ul > li {
  color: #333;
  font-size: 14px;
}
.education_desc_degree_name {
  color: #000;
  font-weight: bold;
}
</style>
