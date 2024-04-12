<script setup>
import { useItensStore } from "../../stores/itens";
import { defineEmits, ref } from "vue";

const itensStore = useItensStore();
const carro = ref({
    nome: '',
    marca: Number,
    cor: Number,
    categoria: Number,
    acessorio: Number,
    imagem: ''
});

const emit = defineEmits(['closeForm']);

const post = async () => {
    await itensStore.postCarro(carro.value);
    carro.value.nome = '';
    carro.value.marca = Number;
    carro.value.cor = Number;
    carro.value.categoria = Number;
    carro.value.acessorio = Number;
    carro.value.imagem = '';
    emit('closeForm');
}
</script>

<template>
    <section>
        <div class="back" @click="$emit('closeForm')"></div>
        <div class="form">
            <h2>
                Adicionar carro
            </h2>

            <input type="text" placeholder="Nome" v-model="carro.nome">

            <input type="file" />

            <select name="marca" v-model="carro.marca">
                <option v-for="marca in itensStore.marcas" :value="marca.id" :key="marca.id">{{ marca.nome }}</option>
            </select>

            <select name="cor" v-model="carro.cor">
                <option v-for="cor in itensStore.cores" :value="cor.id" :key="cor.id">{{ cor.nome }}</option>
            </select>

            <select name="categoria" v-model="carro.categoria">
                <option v-for="categoria in itensStore.categorias" :value="categoria.id" :key="categoria.id">{{ categoria.descricao }}</option>
            </select>

            <select name="acessorio" v-model="carro.acessorio">
                <option v-for="acessorio in itensStore.acessorios" :value="acessorio.id" :key="acessorio.id">{{ acessorio.descricao }}</option>
            </select>

            <button class="btn-add" @click="post">
                Adicionar Carro
            </button>
        </div>
    </section>
</template>

<style scoped>
    section {
        width: 100%;
        height: 100%;
        position: fixed;
        top: 0;
        left: 0;
        z-index: 3;
        display: flex;
        align-items: center;
        justify-content: center;
        backdrop-filter: blur(5px);
    }

    .form {
        width: 400px;
        height: 400px;
        background-color: #fff;
        box-shadow: rgba(99, 99, 99, 0.2) 0px 2px 8px 0px;
        display: flex;
        align-items: center;
        justify-content: center;
        flex-wrap: wrap;
        gap: 20px;
        row-gap: 20px;
        padding: 10px;
        z-index: 2;
    }

    .back {
        width: 100%;
        height: 100%;
        position: fixed;
        top: 0;
        left: 0;
        z-index: 1;
    }

    h2 {
        width: 80%;
    }

    input, select {
        width: 150px;
        height: 30px;
        border: 1px solid #ccc;
        border-radius: 5px;
        padding: 2.5px 5px;
    }
</style>