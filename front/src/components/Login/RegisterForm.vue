<script setup>

</script>

<template>
    <div class="form">
        <h1>
            Registrar-se
        </h1>

        <div class="inputs">
            <input type="text" class="username" placeholder="Username">
            <input type="text" class="email" placeholder="Email">
            <input type="password" class="password" placeholder="Password">
        </div>
        
        <button class="btn-register">
            Registrar-se
        </button>
    </div>
</template>

<style scoped>
    .form {
        display: flex;
        flex-direction: column;
        width: 30%;
        height: 70%;
        align-items: center;
        justify-content: center;
        gap: 30px;
        box-shadow: rgba(0, 0, 0, 0.24) 0px 3px 8px;
        border-left: 1px solid rgba(0, 0, 0, 0.493);
    }

    .inputs {
        display: flex;
        flex-direction: column;
        width: 60%;
        gap: 20px;
    }

    .inputs input {
        width: 100%;
        height: 30px;
        outline: none;
        border: none;
        border-radius: 5px;
        padding: 0 10px;
        box-shadow: rgba(99, 99, 99, 0.2) 0px 2px 8px 0px;
    }

    .btn-register {
        width: 40%;
        height: 30px;
        text-transform: uppercase;
        font-weight: bolder;
        letter-spacing: 0.2rem;
        background-color: #056CF2;
        color: #ffffff;
        border-radius: 10px;
        border: none;
        cursor: pointer;
    }
</style>
