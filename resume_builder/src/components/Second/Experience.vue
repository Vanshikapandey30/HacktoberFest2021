<template>
  <div class="experience">
    <ul>
      <li class="experince_li">
        <!-- Experience Title -->
        <div class="experience_title">
          <span>{{ experienceTitleName }}</span>
          <!-- submit btn -->
          <div v-if="btnClose" @click="edit_exp()" class="header_edit">
            <button class="btn btn_change"><i class="fas fa-pen"></i></button>
          </div>
        </div>
        <!-- Experience Description -->
        <div class="experience_desc">
          <!-- Experience Description title -->
          <div class="experience_desc_title">
            <span>
              {{ experienceCompanyName }}
            </span>
          </div>
          <!-- Experience Description role -->
          <div class="experience_desc_date">
            <span class="start_date">{{ startDate }} - </span>
            <span class="end_date">{{ endDate }}</span>
          </div>
          <!-- Experience Description role -->
          <div class="experience_desc_role">
            <span>{{ experienceRole }}</span>
          </div>
          <div class="experience_todo_points">
            <ul class="experience_todo_ul">
              <li>{{ experienceDescOne }}</li>
              <li>{{ experinceDescTwo }}</li>
            </ul>
          </div>
        </div>
      </li>
    </ul>
    <!-- Experience todo points -->
  </div>
</template>

<script>
export default {
  props: [
    'experienceTitleName',
    'experienceCompanyName',
    'startDate',
    'endDate',
    'experienceRole',
    'experienceDescOne',
    'experinceDescTwo',
    'btnClose',
  ],
  methods: {
    edit_exp() {
      this.$emit('openExpEdit');
    },
  },
};
</script>

<style>
.experience {
  height: auto;
  width: 70%;
  border-right: 1px solid #333;
}
.experince_li {
  list-style: none;
}
.experience_title {
  margin-top: 30px;
  margin-left: 30px;
  font-size: 20px;
  font-family: var(--font);
  color: #cb570c;
  display: flex;
}
.experience_desc {
  margin-top: 10px;
  margin-left: 30px;
}
.experience_desc_title > span {
  font-family: var(--font_sans);
  font-weight: 600;
  font-size: 18px;
}
.experience_desc_role > span {
  font-family: var(--font_sans);
  font-weight: 600;
  font-size: 13px;
  color: #888;
}
.experience_desc_date > span {
  font-family: var(--font_sans);
  font-weight: 600;
  font-size: 13px;
  color: #888;
}
.experience_todo_points {
  margin-top: 10px;
  margin-left: 45px;
  margin-right: 30px;
}
.experience_todo_ul > li {
  font-family: var(--font_sans);
  font-size: 14px;
  line-height: 20px;
  margin-bottom: 5px;
}
</style>
