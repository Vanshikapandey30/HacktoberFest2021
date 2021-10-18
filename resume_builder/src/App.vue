<template>
  <div class="main_body" spellcheck="false">
    <Compile></Compile>
  </div>
</template>

<script>
import Compile from './components/Compile.vue';
export default {
  components: {
    Compile,
  },
};
</script>

<style>
@import url('https://fonts.googleapis.com/css2?family=Montserrat:wght@600&family=Roboto&display=swap');
@import url('https://fonts.googleapis.com/css2?family=Source+Sans+Pro:wght@400;600&display=swap');

:root {
  --font: 'Montserrat', sans-serif;
  --font_roboto: 'Roboto', sans-serif;
  --font_sans: 'Source Sans Pro', sans-serif;
}

* {
  margin: 0;
  padding: 0;
  box-sizing: border-box;
  /* overflow-x: hidden; */
}
body {
  overflow-x: hidden;
}
#app {
  width: 100vw;
  height: 100%;
}
.main_body {
  height: 100%;
  width: 100%;
}
</style>
