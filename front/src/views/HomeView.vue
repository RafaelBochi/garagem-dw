<script setup>
import Header from '@/components/Home/Header.vue';
import Menu from '@/components/Home/Menu.vue';
import { RouterView } from 'vue-router';
import { ref } from 'vue';

const showMenu = ref(false);

function toggleMenu() {
  showMenu.value = !showMenu.value;
  console.log(showMenu.value)
}
</script>

<template>
  <main>
    <Header @toggle-menu="toggleMenu" />
    <Menu :showMenu="showMenu" />
    <section :class="showMenu ? 'body-resised' : ''">
      <RouterView />
    </section>
  </main>
</template>

<style scoped>
main {
  display: flex;
  flex-direction: column;
  align-items: end;
}

section {
  width: 100%;
  height: 100%;
  transition: all 0.5s;
  padding: 10px;
}

.body-resised {
  width: calc(100% - 300px) !important;
}
</style>
