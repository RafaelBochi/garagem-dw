<script setup>
import { RouterView } from 'vue-router'
import { onMounted } from 'vue';
import { useItensStore } from './stores/itens';

const itensStore = useItensStore();

onMounted(async ()=> {
  await itensStore.getAll();

  console.log(itensStore.carros)
})
</script>

<template>
  <RouterView />
</template>

<style scoped>
</style>
