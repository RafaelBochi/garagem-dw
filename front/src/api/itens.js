import axios from "axios";

class ItensService {
    async getCarros() {
        const { data } = await axios.get("/carros/");
        return data;
    }
    async getAcessorios() {
        const { data } = await axios.get("/acessorios/");
        return data;
    }
    async getMarcas() {
        const { data } = await axios.get("/marcas/");
        return data;
    }
    async getCores() {
        const { data } = await axios.get("/cores/");
        return data;
    }
    async getCategorias() {
        const { data } = await axios.get("/categorias/");
        return data;
    }
    async postCarro(carro) {
        await axios.post("/carros/", carro);
    }
    async postAcessorio(acessorio) {
        await axios.post("/acessorios/", acessorio);
    }
    async postMarca(marca) {
        await axios.post("/marcas/", marca);
    }
    async postCategoria(categoria) {
        await axios.post("/categorias/", categoria);
    }
    async postCor(cor) {
        await axios.post("/cores/", cor);
    }
    async deleteCarro(id) {
        await axios.delete(`/carros/${id}`);
    }
    async deleteAcessorio(id) {
        await axios.delete(`/acessorios/${id}`);
    }
    async deleteMarca(id) {
        await axios.delete(`/marcas/${id}`);
    }
    async deleteCategoria(id) {
        await axios.delete(`/categorias/${id}`);
    }
    async deleteCor(id) {
        await axios.delete(`/cores/${id}`);
    }
}

export default new ItensService;