import axios from "axios";

class UserService {
    async login(user) {
        const { data } = await axios.post("/api/user/login/", user);
        return data;
    }
    async register(user) {
        const { data } = await axios.post("/api/user/register/", user);
        return data;
    }
}

export default new UserService;