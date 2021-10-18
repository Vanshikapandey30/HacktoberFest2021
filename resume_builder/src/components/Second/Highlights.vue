<template>
  <div class="highlights">
    <!-- Highlights Title -->
    <div class="highlights_title">
      <span>{{ title }}</span>
      <div @click="edit_highlight()" class="header_edit">
        <button v-if="btnClose" class="btn btn_change">
          <i class="fas fa-pen"></i>
        </button>
      </div>
    </div>
    <!-- Highlights Description -->
    <div class="heighlights_desc">
      <ul class="heighlights_desc_ul">
        <li
          v-for="(highList, index) in newArr"
          :key="index"
          contenteditable="true"
          class="flex_list"
        >
          {{ highList }}
          <div v-if="btnClose" @click="delete_item(index)" class="header_edit">
            <button class="btn btn_change"><i class="fas fa-trash"></i></button>
          </div>
        </li>
      </ul>
    </div>
  </div>
</template>

<script>
export default {
  props: ['title', 'highlightList', 'btnClose'],
  data() {
    return {
      // highlightListItem: [],
      newArr: [
        'Result Oriented',
        'Revenue Generation',
        'Business Development',
        'Effective Marketing',
        'Organisational Capacity',
      ],
    };
  },
  methods: {
    edit_highlight() {
      this.$emit('openHighlightEdit');
    },
    delete_item(index) {
      this.newArr.splice(index, 1);
    },
  },
  watch: {
    highlightList() {
      this.newArr = this.highlightList.split(',');
      // this.highlightListItem.push(myArr);
    },
  },
};
</script>

<style scoped>
.flex_list {
  display: flex;
}
.highlights {
  height: auto;
  width: 100%;
}
.highlights_title {
  margin-top: 30px;
  margin-left: 30px;
  font-size: 20px;
  font-family: var(--font);
  color: #cb570c;
  display: flex;
}
.heighlights_desc {
  margin-top: 10px;
  margin-left: 30px;
  font-family: var(--font_sans);
}
.heighlights_desc_ul > li {
  font-size: 15px;
}
</style>
