<script setup>
import AcessorioAdd from '@/components/Forms/AcessorioAdd.vue';
import { useItensStore } from '@/stores/itens';
import { ref, computed } from 'vue';

const itensStore = useItensStore();

const acessorios = computed(() => itensStore.acessorios);
const showForm = ref(false);

const deleteItem = async (id) => {
    await itensStore.deleteAcessorio(id);
}
</script>

<template>
    <section>
        <AcessorioAdd v-if="showForm" @close-form="() => showForm = false"/>
        <button class="btn-add" @click="() => showForm = true">
            Adicionar acessorio
        </button>

        <div class="itens">
            <div class="item" v-for="acessorio in acessorios" :key="acessorio.id">
                <p class="descricao">
                    {{ acessorio.descricao }}
                </p>

                <button class="btn-delete" @click="deleteItem(acessorio.id)">
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