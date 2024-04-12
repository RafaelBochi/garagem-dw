import { defineStore } from "pinia";
import itensService from '@/api/itens'

export const useItensStore = defineStore('itens', {
    state: () => ({
        carros: [],
        acessorios: [],
        marcas: [],
        categorias: [],
        cores: []
    }),
    actions: {
        async getAll() {
            const carros = await itensService.getCarros();
            const acessorios = await itensService.getAcessorios();
            const marcas = await itensService.getMarcas();
            const categorias = await itensService.getCategorias();
            const cores = await itensService.getCores();

            this.carros = carros;
            this.acessorios = acessorios;
            this.marcas = marcas;
            this.categorias = categorias;
            this.cores = cores;
        },
        async postCarro(carro) {
            console.log(carro)
            await itensService.postCarro(carro);
            this.getAll();
        },
        async postAcessorio(acessorio) {
            await itensService.postAcessorio(acessorio);
            this.getAll();
        },
        async postMarca(marca) {
            await itensService.postMarca(marca);
            this.getAll();
        },
        async postCategoria(categoria) {
            await itensService.postCategoria(categoria);
            this.getAll();
        },
        async postCor(cor) {
            await itensService.postCor(cor);
            this.getAll();
        },
        async deleteCarro(id) {
            await itensService.deleteCarro(id);
            this.getAll();
        },
        async deleteAcessorio(id) {
            await itensService.deleteAcessorio(id);
            this.getAll();
        },
        async deleteMarca(id) {
            await itensService.deleteMarca(id);
            this.getAll();
        },
        async deleteCategoria(id) {
            await itensService.deleteCategoria(id);
            this.getAll();
        },
        async deleteCor(id) {
            await itensService.deleteCor(id);
            this.getAll();
        }
    }
})