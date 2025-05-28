import {apiService} from "./apiService";
import {urls} from "../constants/url";

const pizzaService = {
    getAll(){
        return apiService.get(urls.pizzas)
    },
    create(data){
        return apiService.post(urls.pizzas, data)
    }
}

export {pizzaService}