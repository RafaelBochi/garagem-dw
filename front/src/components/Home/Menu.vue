<script setup>
import { RouterLink } from "vue-router";
defineProps(['showMenu'])
</script>

<template>
    <aside class="" :class="showMenu ? 'opened' : 'closed'">
        <div class="link">
            <RouterLink to="/">
            <p>
                Carros
            </p>
            </RouterLink>
        </div>
        
        <div class="link">
            <RouterLink to="/acessorios">
            <p>
                acessorios
            </p>
            </RouterLink>
        </div>

        <div class="link">
            <RouterLink to="/marcas">
            <p>
                marcas
            </p>
            </RouterLink>
        </div>

        <div class="link">
            <RouterLink to="/cores">
            <p>
                cores
            </p>
            </RouterLink>
        </div>

        <div class="link">
            <RouterLink to="/categorias">
            <p>
                categorias
            </p>
            </RouterLink>
        </div>
    </aside>
</template>

<style scoped>
aside {
    position: fixed;
    top: 80px;
    left: -300px;
    width: 300px;
    height: calc(100% - 80px);
    display: flex;
    flex-direction: column;
    align-items: center;
    justify-content: center;
    gap: 1rem;
    padding: 1rem;
    border-right: 1px solid #ccc;   
    background-color: #fff;
    z-index: 3;
}

a {
    text-decoration: none;
    color: #000;
}

.link {
    font-size: 2rem;
    cursor: pointer;
    width: 80%;
    text-transform: uppercase;
    font-weight: bolder;
    letter-spacing: 0.1rem;
}

.opened {
    animation: opened 0.5s forwards;
}

.closed {
    animation: closed 0.5s forwards;
}

@keyframes opened {
    from {
        left: -300px;
    }
    to {
        left: 0;
    }
}

@keyframes closed {
    from {
        left: 0;
    }
    to {
        left: -300px;
    }
}
</style>