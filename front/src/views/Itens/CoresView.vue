<script setup>
import { ref, computed } from 'vue';
import { useItensStore } from '@/stores/itens';
import CorAdd from '@/components/Forms/CorAdd.vue';

const itensStore = useItensStore();
const cores = computed(() => itensStore.cores);
const showForm = ref(false);

const deleteItem = async (id) => {
    await itensStore.deleteCor(id);
}
</script>

<template>
    <section>
        <CorAdd v-if="showForm" @close-form="() => showForm = false"/>
        <button class="btn-add" @click="() => showForm = true">
            Adicionar cor
        </button>

        <div class="itens">
            <div class="item" v-for="cor in cores" :key="cor.id">
                <p class="nome">
                    {{ cor.nome }}
                </p>

                <button class="btn-delete" @click="deleteItem(cor.id)">
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