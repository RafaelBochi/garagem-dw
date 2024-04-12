<script setup>
import { ref, computed } from 'vue';
import { useItensStore } from '@/stores/itens';
import MarcaAdd from '@/components/Forms/MarcaAdd.vue';

const itensStore = useItensStore();
const marcas = computed(() => itensStore.marcas);
const showForm = ref(false);

const deleteItem = async (id) => {
    await itensStore.deleteMarca(id);
}
</script>

<template>
    <section>
        <MarcaAdd v-if="showForm" @close-form="() => showForm = false"/>
        <button class="btn-add" @click="() => showForm = true">
            Adicionar marca
        </button>

        <div class="itens">
            <div class="item" v-for="marca in marcas" :key="marca.id">
                <p class="nome">
                    {{ marca.nome }}
                </p>
                <p class="nacionalidade">
                    {{ marca.nacionalidade }}
                </p>

                <button class="btn-delete" @click="deleteItem(marca.id)">
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