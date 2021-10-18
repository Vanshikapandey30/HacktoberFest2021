<template>
  <div class="overview">
    <span class="overview_desc">
      {{ overview }}
    </span>
  </div>
  <div v-if="btnClose" @click="edit_overview()" class="header_edit">
    <button class="btn btn_change"><i class="fas fa-pen"></i></button>
  </div>
</template>

<script>
export default {
  props: ['overview', 'btnClose'],
  emits: ['openOverviewEdit'],
  methods: {
    edit_overview() {
      this.$emit('openOverviewEdit');
    },
  },
};
</script>

<style scoped>
.overview {
  width: 100%;
  height: auto;
  margin-left: 10px;
  margin-top: 20px;
  display: flex;
  justify-content: center;
  align-items: center;
}
.overview_desc {
  font-family: var(--font_roboto);
  font-size: 13px;
  line-height: 22px;
}
</style>
