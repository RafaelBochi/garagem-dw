import { createRouter, createWebHistory } from 'vue-router'
import HomeView from '../views/HomeView.vue'
import LoginView from '@/views/LoginView.vue'
import AcessoriosView from '@/views/Itens/AcessoriosView.vue'
import CategoriasView from '@/views/Itens/CategoriasView.vue'
import CoresView from '@/views/Itens/CoresView.vue'
import MarcasView from '@/views/Itens/MarcasView.vue'
import CarrosView from '@/views/Itens/CarrosView.vue'

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/',
      name: 'home',
      component: HomeView,
      children: [
        {
          path: '/acessorios',
          name: 'acessorios',
          component: AcessoriosView
        },
        {
          path: '/categorias',
          name: 'categorias',
          component: CategoriasView
        },
        {
          path: '/cores',
          name: 'cores',
          component: CoresView
        },
        {
          path: '/marcas',
          name: 'marcas',
          component: MarcasView
        },
        {
          path: '/',
          name: 'carros',
          component: CarrosView
        }
      ]
    },
    {
      path: '/login',
      name: 'login',
      component: LoginView
    }
  ]
})

export default router
