<script setup>
import { useItensStore } from "../../stores/itens";
import { ref, defineEmits } from "vue";
const emit = defineEmits(['closeForm']);
const itensStore = useItensStore();
const categoria = ref({ descricao: "" });

const post = async () => {
    await itensStore.postCategoria(categoria.value);
    categoria.value.descricao = "";
    emit('closeForm');
}
</script>

<template>
    <section>
        <div class="back" @click="$emit('closeForm')"></div>
        <div class="form">
            <h2>
                Adicionar categoria
            </h2>

            <input type="text" placeholder="Descricao" v-model="categoria.descricao">

            <button class="btn-add" @click="post">
                Adicionar categoria
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