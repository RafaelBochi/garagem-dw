<script setup>
import { ref, computed } from 'vue';
import CategoriaAdd from '@/components/Forms/CategoriaAdd.vue';
import { useItensStore } from '@/stores/itens';

const itensStore = useItensStore();
const categorias = computed(() => itensStore.categorias);
const showForm = ref(false);

const deleteItem = async (id) => {
    await itensStore.deleteCategoria(id);
}
</script>

<template>
    <section>
        <CategoriaAdd v-if="showForm" @close-form="() => showForm = false"/>
        <button class="btn-add" @click="() => showForm = true">
            Adicionar categoria
        </button>

        <div class="itens">
            <div class="item" v-for="categoria in categorias" :key="categoria.id">
                <p class="descricao">
                    {{ categoria.descricao }}
                </p>

                <button class="btn-delete" @click="deleteItem(categoria.id)">
                    Deletar
                </button>
            </div>
        </div>
    </section>
</template>

<style scoped>
    section {
        width: 100%;
        height: 100%;
        transition: all 0.5s;
    }
</style>