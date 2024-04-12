import { defineStore } from 'pinia';
import { useStorage } from '@vueuse/core';
import userService from '@/api/user'
import router from '@/router'

export const useUserStore = defineStore('counter', {
  state: () => ({
    user: useStorage("user", {}),
    loggedIn: useStorage("loggedIn", false)
  }),
  actions: {
    async login(user) {
      try {
        const data = await userService.login(user);
        this.user = data.user;
        this.loggedIn = true;
        router.push('/')
      }
      catch(e) {
        this.user = {};
        this.loggedIn = false;
        console.log(e)
      }
    },
    async register(user) {
      try {
        const data = await userService.register(user);
        this.user = data.user;
        this.loggedIn = true;
        router.push('/')
      }
      catch(e) {
        this.user = {};
        this.loggedIn = false;
        console.log(e)
      }
    }
  }
})
