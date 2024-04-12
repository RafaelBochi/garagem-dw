<script setup>
import { computed } from "vue";
import { RouterLink } from "vue-router";
import { useUserStore } from '@/stores/user';

const userStore = useUserStore();

const user = computed(() => userStore.user)
const loggedIn = computed(() => userStore.loggedIn)
</script>

<template>
    <header>
        <box-icon name='menu' size="lg" class="btn-menu" @click="$emit('toggleMenu')"></box-icon>
        <h2>
            CarList
        </h2>

        <div class="user" v-if="loggedIn">
            <p class="username">
                {{ user.username }}
            </p>
        </div>

        <div class="user-actions" v-else>
            <RouterLink to="/login">
                <button class="btn-login">
                    Entrar
                </button>
            </RouterLink>
        </div>
    </header>
</template>

<style scoped>
header {
    width: 100%;
    height: 80px;
    box-shadow: rgba(100, 100, 111, 0.2) 0px 7px 29px 0px;
    display: flex;
    align-items: center;
    justify-content: space-between;
    padding: 0 30px;
    border-bottom: 1px solid #ccc;
    z-index: 2;
}

.btn-menu {
    cursor: pointer;
}

h2 {
    font-size: 3.0rem;
}

.username {
    font-size: 1.4rem;
}

.btn-login {
    cursor: pointer;
    background-color: #056CF2;
    padding: 7px 20px;
    color: #fff;
    border: none;
    border-radius: 5px;
    text-transform: uppercase;
    font-weight: bolder;
    letter-spacing: 0.1rem;
}
</style>
