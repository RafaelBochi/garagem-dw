<script setup>
import { useItensStore } from '@/stores/itens';
import { computed, ref } from 'vue';
import CarAdd from '@/components/Forms/CarAdd.vue';
const itensStore = useItensStore();

const carros = computed(() => itensStore.carros);
const showForm = ref(false)

const deleteItem = async (id) => {
    await itensStore.deleteCarro(id);
}
</script>

<template>
    <section>
        <CarAdd v-if="showForm" @close-form="() => showForm = false" />
        <button class="btn-add" @click="() => showForm = true">
            Adicionar carro
        </button>

        <div class="itens">
            <div class="item" v-for="carro in carros" :key="carro.id">
                <p class="nome">
                    {{ carro.nome }}
                </p>
                <p class="categoria">
                    {{ carro.categoria.descricao }}
                </p>
                <p class="cor">
                    {{ carro.cor.nome }}
                </p>
                <p class="marca">
                    {{ carro.marca.nome }} - {{ carro.marca.nacionalidade }}
                </p>
                <p class="acessorio">
                    {{ carro.acessorio.descricao }}
                </p>

                <button class="btn-delete" @click="deleteItem(carro.id)">
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

.carro {
    padding: 10px;
    box-shadow: rgba(99, 99, 99, 0.2) 0px 2px 8px 0px;
    width: 300px;
}

.nome {
    font-size: 1.6rem;
    font-weight: bolder;
}

p {
    font-size: 1.4rem;
}
</style>