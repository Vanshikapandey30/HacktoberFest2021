<template>
  <!-- Main header -->
  <div class="main_resume_template">
    <div class="main_header">
      <HeaderPart @downloadtopdf="changeT()"></HeaderPart>
    </div>

    <div>
      <div class="main_body_template">
        <div class="main_template">
          <div class="resume_template" id="convert">
            <!-- Header Resume-->
            <div class="header_resume">
              <Header
                @openHeaderEdit="openHeader"
                :name="newName"
                :contact="newContact"
                :email="newEmail"
                :btnClose="btn_close"
              ></Header>
            </div>
            <!-- First Overview -->
            <div class="first_overview">
              <!-- Overview -->
              <Overview
                @openOverviewEdit="openOverview"
                :overview="newOverview"
                :btnClose="btn_close"
              ></Overview>
            </div>
            <hr />
            <!-- resume details -->
            <div class="bottom">
              <Experience
                @openExpEdit="openExperience"
                :experienceTitleName="experience_title_name"
                :experienceCompanyName="experience_company_name"
                :startDate="start_date"
                :endDate="end_date"
                :experienceRole="experience_role"
                :experienceDescOne="experience_desc_one"
                :experinceDescTwo="experience_desc_two"
                :btnClose="btn_close"
              ></Experience>
              <!-- Right side of resume details -->
              <div class="second_part">
                <Highlights
                  @openHighlightEdit="openHighlight"
                  :title="highlight_title"
                  :highlightList="highlight_list"
                  :btnClose="btn_close"
                ></Highlights>
                <Education
                  @openEduEdit="openEdcation"
                  :degree="degree_name"
                  :course="degree_course"
                  :university="degree_uni"
                  :address="degree_add"
                  :gpa="degree_gpa"
                  :btnClose="btn_close"
                ></Education>
                <Hobbies
                  @openHobbiesEdit="openHobbies"
                  :title="hobbie_title"
                  :hobbieList="hobbie_list"
                  :btnClose="btn_close"
                ></Hobbies>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>

    <div class="main_footer">
      <FooterPart></FooterPart>
    </div>
  </div>

  <!-- header_input -->
  <div class="main_resume_input" v-if="openChange == 1 && open">
    <div class="header_resume_input">
      <HeaderInput
        @inputeHeader="updateHeader"
        @closeInput="closingInput"
      ></HeaderInput>
    </div>
  </div>

  <!-- Overview input -->
  <div class="main_resume_input" v-if="openChange == 2 && open">
    <div class="overview_resume_input">
      <OverviewInput
        @inputOverview="updateOverview"
        @closeInput="closingInput"
      ></OverviewInput>
    </div>
  </div>

  <!-- Experience input -->
  <div class="main_resume_input" v-if="openChange == 3 && open">
    <div class="overview_resume_input">
      <ExperienceInput
        @inputExp="updateExperience"
        @closeInput="closingInput"
      ></ExperienceInput>
    </div>
  </div>

  <!-- Highlight input -->
  <div class="main_resume_input" v-if="openChange == 4 && open">
    <div class="overview_resume_input">
      <HighlightInput
        @inputHighlight="updateHighlight"
        @closeInput="closingInput"
      ></HighlightInput>
    </div>
  </div>

  <!-- Education input -->
  <div class="main_resume_input" v-if="openChange == 5 && open">
    <div class="overview_resume_input">
      <EducationInput
        @inputEducation="updateEducation"
        @closeInput="closingInput"
      ></EducationInput>
    </div>
  </div>

  <!-- Hobbies input -->
  <div class="main_resume_input" v-if="openChange == 6 && open">
    <div class="overview_resume_input">
      <HobbieInput
        @inputHobbie="updateHobbie"
        @closeInput="closingInput"
      ></HobbieInput>
    </div>
  </div>
</template>

<script>
import Header from './Header/Header.vue';
import Overview from './FirstOverview/Overview.vue';
import Experience from './Second/Experience.vue';
import Highlights from './Second/Highlights.vue';
import Education from './Second/Education.vue';
import Hobbies from './Second/Hobbies.vue';
import HeaderPart from './UI/HeaderPart.vue';
import FooterPart from './UI/FooterPart.vue';
import HeaderInput from './Input/HeaderInput.vue';
import OverviewInput from './Input/OverviewInput.vue';
import ExperienceInput from './Input/ExperienceInput.vue';
import HighlightInput from './Input/HighlightsInput.vue';
import EducationInput from './Input/EducationInput.vue';
import HobbieInput from './Input/HobbieInput.vue';

export default {
  components: {
    Header,
    Overview,
    Experience,
    Highlights,
    Education,
    Hobbies,
    HeaderPart,
    FooterPart,
    HeaderInput,
    OverviewInput,
    ExperienceInput,
    HighlightInput,
    EducationInput,
    HobbieInput,
  },
  data() {
    return {
      btn_close: true,
      newName: 'Manas Mishra',
      newContact: '6202286832',
      newEmail: 'mk1316a@gmail.com',
      newOverview:
        ' Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industrys standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. Lorem Ipsum is simply dummy text of the printing and typesetting industry.',
      // experince
      experience_title_name: 'Experience',
      experience_company_name: 'Ozone AI',
      start_date: '7-8-2018',
      end_date: '7-9-2018',
      experience_role: 'ML Engineer',
      experience_desc_one:
        'Utilized PySpark to distribute data processing on large streaming datasets to improve ingestion and processing speed of that daat by 87%',
      experience_desc_two:
        'Build basic ETL that ingested transactional and event data from a web app with 10,000 daily active users that saved over $85,000 annually in external vendor costs',

      // highlights
      highlight_title: 'Highlights',
      highlight_list: '',

      // Education
      degree_name: 'Bachelor of Science',
      degree_course: 'Automotive Technology',
      degree_uni: 'Kalasalingam Academy of Research and Education',
      degree_add: 'Virudhanagar, Tamilnadu, India',
      degree_gpa: ' 3.7',

      // hobbies
      hobbie_title: 'Hobbies',
      hobbie_list: '',

      // common
      openChange: 0,
      open: false,
    };
  },
  methods: {
    changeT() {
      this.btn_close = false;
      var element = document.getElementById('convert');
      html2pdf(element);
    },
    updateHeader(var1, var2, var3) {
      this.newName = var1;
      this.newContact = var2;
      this.newEmail = var3;
      this.open = false;
    },
    closingInput() {
      this.open = false;
    },
    openHeader() {
      this.openChange = 1;
      this.open = !this.open;
    },
    openOverview() {
      this.openChange = 2;
      this.open = !this.open;
    },
    updateOverview(var1) {
      this.newOverview = var1;
      this.open = false;
    },
    openExperience() {
      this.openChange = 3;
      this.open = !this.open;
    },
    updateExperience(var1, var2, var3, var4, var5, var6, var7) {
      this.experience_title_name = var1;
      this.experience_company_name = var2;
      this.start_date = var3;
      this.end_date = var4;
      this.experience_role = var5;
      this.experience_desc_one = var6;
      this.experience_desc_two = var7;
      this.open = false;
    },
    openHighlight() {
      this.openChange = 4;
      this.open = !this.open;
    },
    updateHighlight(var1, var2) {
      this.highlight_title = var1;
      this.highlight_list = var2;
      this.open = !this.open;
    },
    openEdcation() {
      this.openChange = 5;
      this.open = !this.open;
    },
    updateEducation(var1, var2, var3, var4, var5) {
      this.degree_name = var1;
      this.degree_course = var2;
      this.degree_uni = var3;
      this.degree_add = var4;
      this.degree_gpa = var5;
      this.open = !this.open;
    },
    openHobbies() {
      this.openChange = 6;
      this.open = !this.open;
    },
    updateHobbie(var1, var2) {
      this.hobbie_title = var1;
      this.hobbie_list = var2;
      this.open = !this.open;
    },
  },
};
</script>

<style scoped>
hr {
  margin-top: 10px;
}
.main_resume_template {
  width: 100vw;
  height: auto;
}
.main_template {
  width: 50vw;
  height: 80%;
}

.resume_template {
  width: 100%;
  height: 100%;

  border: 0.5px solid #333;
}
.first_overview {
  display: flex;
}
.bottom {
  display: flex;
}
.second_part {
  width: 40%;
}
.header_resume {
  height: 50%;
}
.main_body_template {
  display: flex;
  justify-content: center;
  align-items: center;
}
#convert {
  outline: none;
}
.main_resume_input {
  display: flex;
  justify-content: center;
  align-items: center;
  transform: translateY(-90vh);
  /* background: lightcoral; */
  height: 75vh;
}
.header_resume_input {
  display: flex;
  justify-content: center;
  width: 60vw;
  border: 1px solid black;
  height: 100%;
  align-items: center;
  background: #001559;
  border-radius: 10px;
  opacity: 1;
}
.overview_resume_input {
  display: flex;
  justify-content: center;
  width: 60vw;
  border: 1px solid black;
  height: 100%;
  align-items: center;
  background: #001559;
  border-radius: 10px;
  opacity: 1;
}
</style>
