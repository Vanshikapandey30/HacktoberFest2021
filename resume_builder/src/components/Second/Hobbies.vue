<template>
  <div class="hobbies">
    <!-- Education Title -->
    <div class="hobbies_title">
      <span>{{ title }}</span>
      <!-- submit btn -->
      <div @click="edit_hobbie()" class="header_edit">
        <button v-if="btnClose" class="btn btn_change">
          <i class="fas fa-pen"></i>
        </button>
      </div>
    </div>
    <!-- Hobbies Description -->
    <div class="hobbies_desc">
      <ul class="hobbies_desc_ul" contenteditable="true">
        <li v-for="(hobbie, index) in newArr" :key="index" class="flex_list">
          {{ hobbie }}
          <div @click="delete_item(index)" class="header_edit">
            <button v-if="btnClose" class="btn btn_change">
              <i class="fas fa-trash"></i>
            </button>
          </div>
        </li>
      </ul>
    </div>
  </div>
</template>

<script>
export default {
  props: ['title', 'hobbieList', 'btnClose'],
  data() {
    return {
      newArr: ['Playing cricket', 'Reading books', 'Listening Music'],
    };
  },
  methods: {
    edit_hobbie() {
      this.$emit('openHobbiesEdit');
    },
    delete_item(index) {
      this.newArr.splice(index, 1);
    },
  },
  watch: {
    hobbieList() {
      this.newArr = this.hobbieList.split(',');
    },
  },
};
</script>

<style scoped>
.flex_list {
  display: flex;
}
.hobbies {
  height: auto;
  width: 100%;
}
.hobbies_title {
  margin-top: 30px;
  margin-left: 30px;
  font-size: 20px;
  font-family: var(--font);
  color: #cb570c;
  display: flex;
}
.hobbies_desc {
  margin-top: 10px;
  margin-left: 30px;
  font-family: var(--font_sans);
}
.hobbies_desc_ul > li {
  font-size: 15px;
}
</style>
