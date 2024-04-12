<script setup>
import LoginForm from '@/components/Login/LoginForm.vue';
import RegisterForm from '@/components/Login/RegisterForm.vue';
</script>

<template>
    <main>
        <LoginForm />
        <RegisterForm />
    </main>
</template>

<style scoped>
    main {
        height: 100%;
        display: flex;
        align-items: center;
        justify-content: center;
    }
</style>